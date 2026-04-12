from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
ASSETS_DIR = ROOT / "assets"
DIST_DIR = ROOT / "dist"


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text

    try:
        _, raw_meta, body = text.split("---\n", 2)
    except ValueError:
        return {}, text

    meta: dict[str, str] = {}
    for line in raw_meta.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    return meta, body.lstrip()


def normalize_display_title(title: str, label: str) -> str:
    title = title.strip()
    label = label.strip()
    if not label:
        return title

    patterns = [
        rf"^{re.escape(label)}\s*[.:]\s*",
        rf"^{re.escape(label)}\s+",
        rf"^{re.escape(label)}\s*장\s*[.:]?\s*",
        rf"^{re.escape(label)}\s*절\s*[.:]?\s*",
    ]

    for pattern in patterns:
        stripped = re.sub(pattern, "", title)
        if stripped != title and stripped.strip():
            return stripped.strip()

    if title.startswith(label):
        stripped = title[len(label):].lstrip(" .:-–—")
        if stripped:
            return stripped

    return title


def slugify_fragment(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = value.strip().lower()
    value = re.sub(r"[^0-9a-zA-Z가-힣\s-]", "", value)
    value = re.sub(r"\s+", "-", value)
    return value or "section"


def apply_inline(text: str) -> str:
    placeholders: list[str] = []

    def keep(match: re.Match[str]) -> str:
        placeholders.append(match.group(0))
        return f"@@PLACEHOLDER{len(placeholders) - 1}@@"

    text = re.sub(r"`([^`]+)`", keep, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)

    for index, original in enumerate(placeholders):
        text = text.replace(
            f"@@PLACEHOLDER{index}@@",
            f"<code>{html.escape(original[1:-1], quote=False)}</code>",
        )
    return text


def split_table_row(line: str) -> list[str]:
    raw = line.strip()
    if raw.startswith("|"):
      raw = raw[1:]
    if raw.endswith("|"):
      raw = raw[:-1]
    return [cell.strip() for cell in raw.split("|")]


def is_markdown_table(lines: list[str], index: int) -> bool:
    if index + 1 >= len(lines):
        return False
    header = lines[index].strip()
    divider = lines[index + 1].strip()
    if "|" not in header or "|" not in divider:
        return False
    cells = split_table_row(divider)
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def render_markdown_table(lines: list[str], index: int) -> tuple[str, int]:
    header_cells = split_table_row(lines[index])
    body_index = index + 2
    body_rows: list[list[str]] = []

    while body_index < len(lines):
        row = lines[body_index].strip()
        if not row or "|" not in row:
            break
        body_rows.append(split_table_row(row))
        body_index += 1

    thead = "".join(f"<th>{apply_inline(cell)}</th>" for cell in header_cells)
    tbody_rows: list[str] = []
    for row in body_rows:
        padded = row + [""] * max(0, len(header_cells) - len(row))
        cells = padded[: len(header_cells)]
        tbody_rows.append("".join(f"<td>{apply_inline(cell)}</td>" for cell in cells))

    table_html = (
        "<table>"
        f"<thead><tr>{thead}</tr></thead>"
        f"<tbody>{''.join(f'<tr>{row}</tr>' for row in tbody_rows)}</tbody>"
        "</table>"
    )
    return table_html, body_index


def render_markdown(markdown: str) -> tuple[str, list[dict[str, str]]]:
    lines = markdown.splitlines()
    i = 0
    out: list[str] = []
    headings: list[dict[str, str]] = []

    while i < len(lines):
        stripped = lines[i].strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("<"):
            html_lines = [lines[i]]
            i += 1
            while i < len(lines) and lines[i].strip():
                html_lines.append(lines[i])
                i += 1
            out.append("\n".join(html_lines))
            continue

        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            out.append(
                f'<pre><code class="language-{html.escape(lang)}">{html.escape(chr(10).join(code_lines))}</code></pre>'
            )
            i += 1
            continue

        if stripped.startswith(":::"):
            kind = stripped[3:].strip() or "note"
            block_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() != ":::":
                block_lines.append(lines[i])
                i += 1
            inner_html, _ = render_markdown("\n".join(block_lines).strip())
            out.append(
                f'<section class="callout {html.escape(kind)}"><div class="callout-title">{html.escape(kind)}</div>{inner_html}</section>'
            )
            i += 1
            continue

        if is_markdown_table(lines, i):
            table_html, i = render_markdown_table(lines, i)
            out.append(table_html)
            continue

        if stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            text = stripped[level:].strip()
            fragment = slugify_fragment(text)
            if level <= 3:
                headings.append({"level": str(level), "id": fragment, "text": text})
            out.append(f'<h{level} id="{fragment}">{apply_inline(text)}</h{level}>')
            i += 1
            continue

        if stripped.startswith(">"):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_lines.append(lines[i].strip()[1:].strip())
                i += 1
            out.append(f"<blockquote><p>{apply_inline(' '.join(quote_lines))}</p></blockquote>")
            continue

        if re.match(r"[-*]\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"[-*]\s+", lines[i].strip()):
                items.append(re.sub(r"^[-*]\s+", "", lines[i].strip()))
                i += 1
            out.append("".join(["<ul>", *(f"<li>{apply_inline(item)}</li>" for item in items), "</ul>"]))
            continue

        if re.match(r"\d+\.\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"\d+\.\s+", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i].strip()))
                i += 1
            out.append("".join(["<ol>", *(f"<li>{apply_inline(item)}</li>" for item in items), "</ol>"]))
            continue

        paragraph_lines = [stripped]
        i += 1
        while i < len(lines):
            candidate = lines[i].strip()
            if not candidate:
                break
            if candidate.startswith(("```", ":::", ">", "#")):
                break
            if re.match(r"[-*]\s+", candidate) or re.match(r"\d+\.\s+", candidate):
                break
            paragraph_lines.append(candidate)
            i += 1
        out.append(f"<p>{apply_inline(' '.join(paragraph_lines))}</p>")

    return "\n".join(out), headings


def flatten_chapters(book: dict) -> list[dict]:
    flat: list[dict] = []
    for part in book["parts"]:
        for chapter in part["chapters"]:
            item = dict(chapter)
            item["part_title"] = part["title"]
            source_path = (CONTENT_DIR / chapter["source"]).resolve()
            item["source_path"] = str(source_path)
            item["source_uri"] = source_path.as_uri()
            meta, _ = parse_front_matter(source_path.read_text(encoding="utf-8"))
            raw_title = meta.get("title", chapter["title"])
            item["meta_title"] = raw_title
            item["meta_description"] = meta.get("description", "")
            item["display_title"] = normalize_display_title(raw_title, chapter["label"])
            flat.append(item)
    return flat


def build_sidebar(book: dict, current_slug: str | None) -> str:
    flat_by_slug = {chapter["slug"]: chapter for chapter in flatten_chapters(book)}
    part_blocks = []
    for part in book["parts"]:
        chapter_links = []
        for chapter in part["chapters"]:
            current = ' aria-current="page"' if chapter["slug"] == current_slug else ""
            display_title = flat_by_slug[chapter["slug"]]["display_title"]
            label_html = ""
            if chapter["label"]:
                label_html = f'<span class="sidebar-link-label">{html.escape(chapter["label"])}</span>'
            chapter_links.append(
                f"""
                <li class="sidebar-item">
                  <a class="sidebar-link" href="{chapter['slug']}.html"{current}>
                    {label_html}
                    {html.escape(display_title)}
                  </a>
                </li>
                """
            )
        part_blocks.append(
            f"""
            <section class="sidebar-part">
              <div class="sidebar-part-name">{html.escape(part['title'])}</div>
              <p class="sidebar-part-desc">{html.escape(part['description'])}</p>
              <ul class="sidebar-list">{''.join(chapter_links)}</ul>
            </section>
            """
        )

    return f"""
    <aside class="sidebar">
      <a class="brand" href="index.html">
        <span class="brand-kicker">Markdown Edition</span>
        <span class="brand-title">{html.escape(book['title'])}</span>
      </a>
      <div class="sidebar-title">Contents</div>
      {''.join(part_blocks)}
    </aside>
    """


def page_shell(book: dict, sidebar: str, content: str, title: str, editor_config: dict | None = None) -> str:
    editor_script = ""
    if editor_config is not None:
        editor_script = (
            "<script>"
            f"window.__BOOK_EDITOR__ = {json.dumps(editor_config, ensure_ascii=False)};"
            "</script>\n"
        )

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)} | {html.escape(book['title'])}</title>
  <meta name="description" content="{html.escape(book['description'])}" />
  <link rel="stylesheet" href="assets/site.css" />
  <script>
    MathJax = {{
      tex: {{ inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']] }}
    }};
  </script>
  <script defer src="assets/site.js"></script>
  <script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  {editor_script}
</head>
  <body>
  <div class="site-shell">
    {sidebar}
    <main class="page">
      <div class="mobile-bar">
        <strong>{html.escape(book['title'])}</strong>
        <button type="button" data-nav-toggle>목차</button>
      </div>
      {content}
    </main>
  </div>
  <div class="page-credit" aria-label="copyright">
    &copy; 서울대 행정대학원 고길곤
  </div>
  </body>
  </html>
  """


def build_index(book: dict, editable: bool) -> None:
    flat_by_slug = {chapter["slug"]: chapter for chapter in flatten_chapters(book)}
    part_cards = []

    for part in book["parts"]:
        links = []
        for chapter in part["chapters"]:
            flat_chapter = flat_by_slug[chapter["slug"]]
            edit_controls = ""
            if editable:
                edit_controls = (
                    f'<button type="button" class="chapter-edit-link" data-open-source="{flat_chapter["slug"]}" '
                    f'title="{html.escape(flat_chapter["source_path"])}">Markdown 열기</button>'
                    f'<span class="chapter-edit-status" data-open-source-status="{flat_chapter["slug"]}"></span>'
                )
            label_html = ""
            if chapter["label"]:
                label_html = f"<strong>{html.escape(chapter['label'])}</strong><br />"
            links.append(
                f"""
                <li>
                  <a href="{chapter['slug']}.html" class="chapter-card-link">
                    {label_html}
                    {html.escape(flat_chapter['display_title'])}
                  </a>
                  {edit_controls}
                </li>
                """
            )
        part_cards.append(
            f"""
            <section class="part-card">
              <h3>{html.escape(part['title'])}</h3>
              <p>{html.escape(part['description'])}</p>
              <ul class="chapter-list">{''.join(links)}</ul>
            </section>
            """
        )

    hero_editor = ""
    editor_drawer = ""
    editor_config = None
    if editable:
        hero_editor = f"""
      <div class="editor-actions hero-actions">
        <button type="button" class="editor-button secondary" data-editor-open>표지 메타 열기</button>
        <button type="button" class="editor-button" data-open-path="content/book.json" title="{html.escape(str((CONTENT_DIR / 'book.json').resolve()))}">Markdown 열기</button>
        <span class="chapter-edit-status" data-open-path-status="content/book.json"></span>
      </div>
        """
        editor_drawer = """
    <aside class="editor-drawer" data-editor-root hidden>
      <div class="editor-drawer-header">
        <strong>표지 메타 편집기</strong>
        <button type="button" class="editor-close" data-editor-close>닫기</button>
      </div>
      <p class="editor-hint" data-editor-hint>책 제목, 부제, 설명, 리드 문구를 담고 있는 `content/book.json`을 브라우저에서 바로 수정할 수 있습니다.</p>
      <div class="editor-toolbar">
        <button type="button" class="editor-mini-button" data-editor-load>다시 불러오기</button>
        <button type="button" class="editor-mini-button primary" data-editor-save>저장</button>
      </div>
      <textarea class="editor-textarea" data-editor-textarea spellcheck="false"></textarea>
      <div class="editor-status" data-editor-status data-kind="neutral">편집기를 열면 표지 메타 파일을 불러옵니다.</div>
    </aside>
        """
        editor_config = {
            "path": "content/book.json",
            "title": "표지 메타",
            "sourcePath": str((CONTENT_DIR / "book.json").resolve()),
        }

    content = f"""
    <section class="hero">
      <h1>{html.escape(book['title'])}</h1>
      <p class="subtitle">{html.escape(book['subtitle'])}</p>
      <p class="meta">{html.escape(book['description'])}</p>
      <p class="lead">{html.escape(book['lead'])}</p>
      <div
        class="visitor-counter"
        data-visitor-counter
        data-counter-ns="kilkon.github.io"
        data-counter-action="view"
        data-counter-key="causality-homepage"
      >
        <span class="visitor-counter-label">누적 방문</span>
        <strong class="visitor-counter-value" data-visitor-counter-value>불러오는 중...</strong>
        <span class="visitor-counter-note" data-visitor-counter-note>공개 사이트 기준 방문 수를 표시합니다.</span>
      </div>
      {hero_editor}
    </section>
    <section class="section-block">
      <h2>목차</h2>
      {''.join(part_cards)}
    </section>
    {editor_drawer}
    """
    page = page_shell(book, build_sidebar(book, None), content, book["title"], editor_config=editor_config)
    page = page.replace('data-counter-action="view"', "")
    page = re.sub(
        r'<span class="visitor-counter-label">.*?</span>',
        '<span class="visitor-counter-label">누적 방문</span>',
        page,
        count=1,
    )
    page = re.sub(
        r'<strong class="visitor-counter-value" data-visitor-counter-value>.*?</strong>',
        '<strong class="visitor-counter-value" data-visitor-counter-value>불러오는 중...</strong>',
        page,
        count=1,
    )
    page = re.sub(
        r'<span class="visitor-counter-note" data-visitor-counter-note>.*?</span>',
        '<span class="visitor-counter-note" data-visitor-counter-note>공개 사이트 기준 누적 방문 수를 표시합니다.</span>',
        page,
        count=1,
    )
    (DIST_DIR / "index.html").write_text(page, encoding="utf-8")


def write_chapter_page(book: dict, flat: list[dict], index: int, editable: bool) -> None:
    chapter = flat[index]
    markdown_path = CONTENT_DIR / chapter["source"]
    meta, body = parse_front_matter(markdown_path.read_text(encoding="utf-8"))
    rendered, _ = render_markdown(body)

    prev_link = None if index == 0 else flat[index - 1]
    next_link = None if index == len(flat) - 1 else flat[index + 1]
    prev_html = (
        f'<a class="nav-prev" href="{prev_link["slug"]}.html">← {html.escape(prev_link["label"])} {html.escape(prev_link["display_title"])}</a>'
        if prev_link
        else '<span class="disabled">← 첫 장입니다</span>'
    )
    next_html = (
        f'<a class="nav-next" href="{next_link["slug"]}.html">{html.escape(next_link["label"])} {html.escape(next_link["display_title"])} →</a>'
        if next_link
        else '<span class="disabled nav-next">마지막 장입니다 →</span>'
    )

    header_controls = ""
    editor_drawer = ""
    editor_config = None
    if editable:
        header_controls = f"""
        <div class="editor-actions">
          <button type="button" class="editor-button secondary" data-editor-open>브라우저에서 편집</button>
          <button type="button" class="editor-button" data-open-source="{chapter['slug']}" title="{html.escape(chapter['source_path'])}">Markdown 열기</button>
          <span class="editor-path">{html.escape(chapter['source_path'])}</span>
        </div>
        """
        editor_drawer = f"""
    <aside class="editor-drawer" data-editor-root hidden>
      <div class="editor-drawer-header">
        <strong>Markdown 편집기</strong>
        <button type="button" class="editor-close" data-editor-close>닫기</button>
      </div>
      <p class="editor-hint" data-editor-hint>현재 장의 Markdown 원고를 불러와 바로 저장할 수 있습니다.</p>
      <div class="editor-toolbar">
        <button type="button" class="editor-mini-button" data-editor-load>다시 불러오기</button>
        <button type="button" class="editor-mini-button primary" data-editor-save>저장</button>
      </div>
      <textarea class="editor-textarea" data-editor-textarea spellcheck="false"></textarea>
      <div class="editor-status" data-editor-status data-kind="neutral">편집기를 열면 원고를 불러옵니다.</div>
      <div class="chapter-edit-status" data-open-source-status="{chapter['slug']}"></div>
    </aside>
        """
        editor_config = {
            "slug": chapter["slug"],
            "title": chapter["meta_title"],
            "sourcePath": chapter["source_path"],
        }

    content = f"""
    <article class="chapter-card">
      <header class="chapter-header">
        <p class="breadcrumb">{html.escape(chapter['part_title'])} · {html.escape(chapter['label'])}</p>
        <h1>{html.escape(chapter['meta_title'])}</h1>
        <p class="description">{html.escape(chapter['meta_description'])}</p>
        {header_controls}
      </header>
      <section class="chapter-body">
        {rendered}
      </section>
      <nav class="chapter-nav">
        {prev_html}
        {next_html}
      </nav>
    </article>
    {editor_drawer}
    """
    page = page_shell(book, build_sidebar(book, chapter["slug"]), content, chapter["meta_title"], editor_config=editor_config)
    (DIST_DIR / f"{chapter['slug']}.html").write_text(page, encoding="utf-8")


def build_chapters(book: dict, editable: bool) -> None:
    flat = flatten_chapters(book)
    for index in range(len(flat)):
        write_chapter_page(book, flat, index, editable)


def copy_assets() -> None:
    target = DIST_DIR / "assets"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(ASSETS_DIR, target)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--public", action="store_true", help="Build a public, read-only site for publishing.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    for html_file in DIST_DIR.glob("*.html"):
        html_file.unlink()

    book = json.loads((CONTENT_DIR / "book.json").read_text(encoding="utf-8-sig"))
    copy_assets()
    build_index(book, editable=not args.public)
    build_chapters(book, editable=not args.public)

    if args.public:
        (DIST_DIR / ".nojekyll").write_text("", encoding="utf-8")

    flat = flatten_chapters(book)
    expected = len(flat) + 1
    actual = len(list(DIST_DIR.glob("*.html")))
    if actual != expected:
        missing = {f"{chapter['slug']}.html" for chapter in flat} - {path.name for path in DIST_DIR.glob("*.html")}
        for index, chapter in enumerate(flat):
            if f"{chapter['slug']}.html" in missing:
                write_chapter_page(book, flat, index, editable=not args.public)
        actual = len(list(DIST_DIR.glob("*.html")))
        if actual != expected:
            raise RuntimeError(f"Build mismatch: expected {expected} html files, found {actual}")

    print(f"Built site into {DIST_DIR}")


if __name__ == "__main__":
    main()
