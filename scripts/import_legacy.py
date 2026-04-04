from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
CHAPTERS_DIR = CONTENT_DIR / "chapters"


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", value).strip()


def strip_remaining_tags_preserve_lines(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("&nbsp;", " ")
    value = re.sub(r"\r\n?", "\n", value)
    value = re.sub(r"[ \t]+\n", "\n", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def slug_from_href(href: str) -> str:
    path = Path(href)
    stem = path.stem
    if path.parent.name and path.parent.name != "." and path.parent.name != "chapters":
        return f"{path.parent.name}-{stem}"
    return stem


def chapter_source_name(href: str) -> str:
    return f"{slug_from_href(href)}.md"


def label_from_title(title: str) -> str:
    match = re.match(r"^(\d+(?:\.\d+)*)", title)
    if match:
        return match.group(1)
    chapter_match = re.match(r"^(\d+)장", title)
    if chapter_match:
        return chapter_match.group(1)
    appendix_match = re.match(r"^(부록\s*[A-Z])", title)
    if appendix_match:
        return appendix_match.group(1)
    return ""


def clean_title(title: str) -> str:
    title = strip_tags(title)
    title = re.sub(r"\s*\(본문\)\s*", "", title)
    title = re.sub(r"\s*\(보조 노트\)\s*", "", title)
    return re.sub(r"\s+", " ", title).strip()


def chapter_entry_from_link(href: str, title: str) -> dict:
    return {
        "slug": slug_from_href(href),
        "source": f"chapters/{chapter_source_name(href)}",
        "label": label_from_title(title),
        "title": title,
        "legacy_href": href,
    }


def placeholder_entry(article_id: str, title: str) -> dict:
    return {
        "slug": article_id,
        "source": f"chapters/{article_id}.md",
        "label": label_from_title(title),
        "title": title,
        "legacy_href": None,
    }


def parse_article(article_id: str, article_html: str) -> list[dict]:
    entries: list[dict] = []
    seen: set[str] = set()

    h3_match = re.search(r"<h3>(.*?)</h3>", article_html, re.S)
    plain_title = ""
    if h3_match:
        h3_html = h3_match.group(1)
        plain_title = clean_title(re.sub(r"<a [^>]*>.*?</a>", "", h3_html, flags=re.S))
        for href, anchor_text in re.findall(r'<a href="([^"]+)">(.*?)</a>', h3_html, re.S):
            kind = strip_tags(anchor_text).strip("() ")
            if "보조" in kind:
                title = f"{plain_title} — {kind}"
            else:
                title = plain_title
            if href not in seen and title:
                seen.add(href)
                entries.append(chapter_entry_from_link(href, title))

    list_html_match = re.search(r'<ul class="sec">(.*?)</ul>', article_html, re.S)
    if list_html_match:
        for href, raw_title in re.findall(r'<a href="([^"]+)">(.*?)</a>', list_html_match.group(1), re.S):
            title = clean_title(raw_title)
            if href not in seen and title:
                seen.add(href)
                entries.append(chapter_entry_from_link(href, title))

    if not entries and plain_title:
        entries.append(placeholder_entry(article_id, plain_title))

    return entries


def extract_title(html_text: str) -> str:
    match = re.search(r"<h1>(.*?)</h1>", html_text, re.S)
    if match:
        return clean_title(match.group(1))
    title_match = re.search(r"<title>(.*?)</title>", html_text, re.S)
    if title_match:
        return clean_title(title_match.group(1))
    return "제목 없음"


def extract_description(html_text: str) -> str:
    match = re.search(r'<div class="lead">(.*?)</div>', html_text, re.S)
    if not match:
        match = re.search(r'<p class="lead">(.*?)</p>', html_text, re.S)
    if not match:
        return "기존 HTML에서 자동 변환한 초안입니다. 사람이 한 번 다듬어야 합니다."
    return strip_tags(match.group(1))


def normalize_inline_markdown(text: str) -> str:
    text = re.sub(r"<em>(.*?)</em>", r"*\1*", text, flags=re.S)
    text = re.sub(r"<strong>(.*?)</strong>", r"**\1**", text, flags=re.S)
    text = re.sub(r"<code>(.*?)</code>", r"`\1`", text, flags=re.S)
    text = re.sub(r"<a [^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", r"[\2](\1)", text, flags=re.S)
    return strip_remaining_tags_preserve_lines(text)


def preserve_visual_blocks(fragment: str) -> tuple[str, list[str]]:
    blocks: list[str] = []
    patterns = [
        r'<div class="figure"[\s\S]*?</div>\s*</div>',
        r"<figure[\s\S]*?</figure>",
        r"<table[\s\S]*?</table>",
        r"<svg[\s\S]*?</svg>",
    ]

    def replace(match: re.Match[str]) -> str:
        blocks.append(match.group(0).strip())
        return f"\n\n@@HTMLBLOCK{len(blocks) - 1}@@\n\n"

    result = fragment
    for pattern in patterns:
        result = re.sub(pattern, replace, result, flags=re.S)
    return result, blocks


def extract_main_fragment(html_text: str) -> str:
    match = re.search(r'<main class="chapter-main">(.*?)(?:<nav class="chapter-nav">|</main>)', html_text, re.S)
    if not match:
        match = re.search(r"<main[^>]*>(.*?)</main>", html_text, re.S)
    if not match:
        return ""

    fragment = match.group(1)
    fragment = re.sub(r"<header>.*?</header>", "", fragment, flags=re.S)
    fragment = re.sub(r"<script.*?</script>", "", fragment, flags=re.S)
    fragment = re.sub(r"<style.*?</style>", "", fragment, flags=re.S)
    fragment = re.sub(r'<div class="references">.*?</div>', "", fragment, flags=re.S)
    fragment, visual_blocks = preserve_visual_blocks(fragment)

    replacements = [
        (r'<div class="summary-box">', ":::summary\n"),
        (r'<div class="example">', ":::example\n"),
        (r'<div class="note-box">', ":::note\n"),
        (r'<div class="equation">', "```math\n"),
        (r"</div>", "\n:::\n"),
        (r'<h3 class="sec"[^>]*>(.*?)</h3>', r'## \1'),
        (r"<h2[^>]*>(.*?)</h2>", r"## \1"),
        (r"<h3[^>]*>(.*?)</h3>", r"### \1"),
        (r"<h4[^>]*>(.*?)</h4>", r"#### \1"),
        (r'<blockquote[^>]*>', "> "),
        (r"</blockquote>", ""),
        (r"<pre[^>]*><code[^>]*>", "```\n"),
        (r"</code></pre>", "\n```"),
        (r"<ul[^>]*>", ""),
        (r"</ul>", "\n"),
        (r"<ol[^>]*>", ""),
        (r"</ol>", "\n"),
        (r"<li[^>]*>", "- "),
        (r"</li>", "\n"),
        (r"<p[^>]*>", ""),
        (r"</p>", "\n\n"),
        (r"<br ?/?>", "\n"),
    ]

    markdown = fragment
    for pattern, repl in replacements:
        markdown = re.sub(pattern, repl, markdown, flags=re.S)

    markdown = normalize_inline_markdown(markdown)
    markdown = markdown.replace(":::", "\n:::\n")
    for index, block in enumerate(visual_blocks):
        markdown = markdown.replace(f"@@HTMLBLOCK{index}@@", block)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    return markdown.strip()


def parse_index(legacy_root: Path) -> list[dict]:
    text = (legacy_root / "index.html").read_text(encoding="utf-8")
    split_parts = re.split(r'<p class="part">', text)[1:]
    parts: list[dict] = []

    for index, block in enumerate(split_parts, start=1):
        title_raw, remainder = block.split("</p>", 1)
        title = strip_tags(title_raw)
        before_next_part = remainder.split('<p class="part">', 1)[0]
        desc_match = re.search(r'<p class="part-desc">(.*?)</p>', before_next_part, re.S)
        description = strip_tags(desc_match.group(1)) if desc_match else ""
        articles = re.findall(r'<article class="chapter" id="([^"]+)"[^>]*>(.*?)</article>', before_next_part, re.S)
        chapters = []
        for article_id, article_html in articles:
            chapters.extend(parse_article(article_id, article_html))

        parts.append(
            {
                "id": f"part-{index}",
                "title": title,
                "description": description,
                "chapters": chapters,
            }
        )

    return parts


def write_book_json(legacy_root: Path, parts: list[dict]) -> None:
    index_text = (legacy_root / "index.html").read_text(encoding="utf-8")
    h1_match = re.search(r"<h1>(.*?)</h1>", index_text, re.S)
    source_title = clean_title(h1_match.group(1)) if h1_match else extract_title(index_text)
    subtitle = "대학원 석사·박사 수준 강의용 노트"
    description = "기존 정적 HTML 전자책을 Markdown 원고 + 메타데이터 기반 구조로 옮긴 자동 마이그레이션 결과"
    lead = "이 책 구조는 기존 사이트의 목차 순서를 유지하면서, 각 페이지를 Markdown 원고와 공통 템플릿으로 다시 구성할 수 있게 하기 위해 자동 생성되었다."

    book = {
        "title": source_title,
        "subtitle": subtitle,
        "description": description,
        "lead": lead,
        "parts": [
            {
                "id": part["id"],
                "title": part["title"],
                "description": part["description"],
                "chapters": [
                    {
                        "slug": chapter["slug"],
                        "source": chapter["source"],
                        "label": chapter["label"],
                        "title": chapter["title"],
                    }
                    for chapter in part["chapters"]
                ],
            }
            for part in parts
        ],
    }
    (CONTENT_DIR / "book.json").write_text(
        json.dumps(book, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def import_chapters(legacy_root: Path, parts: list[dict], overwrite: bool) -> int:
    imported = 0
    for part in parts:
        for chapter in part["chapters"]:
            href = chapter.pop("legacy_href")
            if href is None:
                output_path = CHAPTERS_DIR / Path(chapter["source"]).name
                if output_path.exists() and not overwrite:
                    continue
                output_path.write_text(
                    (
                        "---\n"
                        f"title: {chapter['title']}\n"
                        "description: 기존 사이트에는 아직 본문이 없어서 생성한 플레이스홀더입니다.\n"
                        "---\n\n"
                        f"# {chapter['title']}\n\n"
                        "이 장은 기존 사이트 목차에는 포함되어 있었지만, 아직 연결된 HTML 본문은 없었습니다.\n\n"
                        "새 Markdown 워크플로에서는 이 파일을 바로 편집해서 부록 원고를 채워 넣을 수 있습니다.\n"
                    ),
                    encoding="utf-8",
                )
                imported += 1
                print(f"Created placeholder {output_path.name}")
                continue

            output_path = CHAPTERS_DIR / chapter_source_name(href)
            input_path = legacy_root.joinpath(*href.split("/"))

            if output_path.exists() and not overwrite:
                continue

            html_text = input_path.read_text(encoding="utf-8")
            title = extract_title(html_text)
            description = extract_description(html_text)
            body = extract_main_fragment(html_text)
            output_path.write_text(
                (
                    "---\n"
                    f"title: {title}\n"
                    f"description: {description}\n"
                    "---\n\n"
                    f"# {title}\n\n"
                    f"{body}\n"
                ),
                encoding="utf-8",
            )
            imported += 1
            print(f"Imported {href} -> {output_path.name}")
    return imported


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--legacy-root", required=True, help="기존 causal inference 폴더 경로")
    parser.add_argument("--overwrite", action="store_true", help="기존 Markdown 초안을 덮어씁니다")
    args = parser.parse_args()

    legacy_root = Path(args.legacy_root).resolve()
    parts = parse_index(legacy_root)
    write_book_json(legacy_root, parts)
    imported = import_chapters(legacy_root, parts, overwrite=args.overwrite)
    print(f"Wrote book.json with {len(parts)} parts and imported {imported} chapter files.")


if __name__ == "__main__":
    main()
