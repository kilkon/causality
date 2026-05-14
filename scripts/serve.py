from __future__ import annotations

import json
import os
import subprocess
import sys
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parents[1]
DIST_DIR = ROOT / "dist"
CONTENT_DIR = ROOT / "content"
BOOK_JSON = CONTENT_DIR / "book.json"
BUILD_SCRIPT = ROOT / "scripts" / "build.py"
CHAPTERS_DIR = CONTENT_DIR / "chapters"
EDITOR_HEADER = "X-Book-Editor"
EDITOR_HEADER_VALUE = "1"
LOCAL_HOSTS = {"127.0.0.1", "localhost"}


def load_book() -> dict:
    return json.loads(BOOK_JSON.read_text(encoding="utf-8-sig"))


def flatten_chapters(book: dict) -> dict[str, dict]:
    mapped: dict[str, dict] = {}
    for part in book["parts"]:
        for chapter in part["chapters"]:
            mapped[chapter["slug"]] = chapter
    return mapped


def run_build() -> tuple[bool, str]:
    result = subprocess.run(
        [sys.executable, str(BUILD_SCRIPT)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode == 0, output.strip()


def normalize_content(value) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, indent=2)
    if value is None:
        return ""
    return str(value)


def is_allowed_editor_path(path: Path) -> bool:
    try:
        resolved = path.resolve()
    except OSError:
        return False

    if resolved == BOOK_JSON.resolve():
        return True

    try:
        resolved.relative_to(CHAPTERS_DIR.resolve())
    except ValueError:
        return False

    return resolved.suffix.lower() == ".md"


class BookHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIST_DIR), **kwargs)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/__api/chapter":
            if not self.require_editor_request():
                return
            self.handle_get_chapter(parsed)
            return
        if parsed.path == "/__api/file":
            if not self.require_editor_request():
                return
            self.handle_get_file(parsed)
            return
        super().do_GET()

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/__api/chapter":
            if not self.require_editor_request(require_json=True):
                return
            self.handle_save_chapter()
            return
        if parsed.path == "/__api/file":
            if not self.require_editor_request(require_json=True):
                return
            self.handle_save_file()
            return
        if parsed.path == "/__api/open":
            if not self.require_editor_request(require_json=True):
                return
            self.handle_open_chapter()
            return
        self.send_error(HTTPStatus.NOT_FOUND, "Not found")

    def resolve_safe_path(self, path_value: str) -> Path | None:
        if not path_value:
            return None

        path = (ROOT / path_value).resolve()
        try:
            path.relative_to(ROOT)
        except ValueError:
            return None
        return path

    def is_allowed_local_url(self, candidate: str) -> bool:
        parsed = urlparse(candidate)
        if parsed.scheme not in {"http", "https"}:
            return False
        return (parsed.hostname or "").lower() in LOCAL_HOSTS

    def require_editor_request(self, require_json: bool = False) -> bool:
        if self.headers.get(EDITOR_HEADER) != EDITOR_HEADER_VALUE:
            self.send_json({"ok": False, "error": "missing_editor_header"}, HTTPStatus.FORBIDDEN)
            return False

        origin = self.headers.get("Origin")
        referer = self.headers.get("Referer")
        if origin and not self.is_allowed_local_url(origin):
            self.send_json({"ok": False, "error": "invalid_origin"}, HTTPStatus.FORBIDDEN)
            return False
        if referer and not self.is_allowed_local_url(referer):
            self.send_json({"ok": False, "error": "invalid_referer"}, HTTPStatus.FORBIDDEN)
            return False

        if require_json:
            content_type = self.headers.get("Content-Type", "")
            if "application/json" not in content_type.lower():
                self.send_json({"ok": False, "error": "invalid_content_type"}, HTTPStatus.BAD_REQUEST)
                return False

        return True

    def handle_get_chapter(self, parsed) -> None:
        slug = parse_qs(parsed.query).get("slug", [""])[0]
        if not slug:
            self.send_json({"ok": False, "error": "missing_slug"}, HTTPStatus.BAD_REQUEST)
            return

        book = load_book()
        chapter = flatten_chapters(book).get(slug)
        if not chapter:
            self.send_json({"ok": False, "error": "unknown_slug"}, HTTPStatus.NOT_FOUND)
            return

        path = CONTENT_DIR / chapter["source"]
        self.send_json(
            {
                "ok": True,
                "slug": slug,
                "source": str(path.resolve()),
                "content": path.read_text(encoding="utf-8"),
            }
        )

    def handle_get_file(self, parsed) -> None:
        path_value = parse_qs(parsed.query).get("path", [""])[0]
        path = self.resolve_safe_path(path_value)
        if not path:
            self.send_json({"ok": False, "error": "invalid_path"}, HTTPStatus.BAD_REQUEST)
            return
        if not is_allowed_editor_path(path):
            self.send_json({"ok": False, "error": "path_not_allowed"}, HTTPStatus.FORBIDDEN)
            return
        if not path.exists():
            self.send_json({"ok": False, "error": "missing_path"}, HTTPStatus.NOT_FOUND)
            return

        self.send_json(
            {
                "ok": True,
                "path": path_value,
                "source": str(path),
                "content": path.read_text(encoding="utf-8-sig"),
            }
        )

    def handle_save_chapter(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length)
        try:
            payload = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self.send_json({"ok": False, "error": "invalid_json"}, HTTPStatus.BAD_REQUEST)
            return

        slug = payload.get("slug", "")
        content = normalize_content(payload.get("content", ""))
        book = load_book()
        chapter = flatten_chapters(book).get(slug)
        if not chapter:
            self.send_json({"ok": False, "error": "unknown_slug"}, HTTPStatus.NOT_FOUND)
            return

        path = (CONTENT_DIR / chapter["source"]).resolve()
        path.write_text(content, encoding="utf-8")
        ok, output = run_build()
        if not ok:
            self.send_json({"ok": False, "error": "build_failed", "output": output}, HTTPStatus.INTERNAL_SERVER_ERROR)
            return

        self.send_json({"ok": True, "output": output})

    def handle_save_file(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length)
        try:
            payload = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self.send_json({"ok": False, "error": "invalid_json"}, HTTPStatus.BAD_REQUEST)
            return

        path_value = payload.get("path", "")
        content = normalize_content(payload.get("content", ""))
        path = self.resolve_safe_path(path_value)
        if not path:
            self.send_json({"ok": False, "error": "invalid_path"}, HTTPStatus.BAD_REQUEST)
            return
        if not is_allowed_editor_path(path):
            self.send_json({"ok": False, "error": "path_not_allowed"}, HTTPStatus.FORBIDDEN)
            return

        path.write_text(content, encoding="utf-8")
        ok, output = run_build()
        if not ok:
            self.send_json({"ok": False, "error": "build_failed", "output": output}, HTTPStatus.INTERNAL_SERVER_ERROR)
            return

        self.send_json({"ok": True, "output": output})

    def handle_open_chapter(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length)
        try:
            payload = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self.send_json({"ok": False, "error": "invalid_json"}, HTTPStatus.BAD_REQUEST)
            return

        path_value = payload.get("path", "")
        if path_value:
            path = self.resolve_safe_path(path_value)
            if not path:
                self.send_json({"ok": False, "error": "invalid_path"}, HTTPStatus.BAD_REQUEST)
                return
            if not is_allowed_editor_path(path):
                self.send_json({"ok": False, "error": "path_not_allowed"}, HTTPStatus.FORBIDDEN)
                return
        else:
            slug = payload.get("slug", "")
            book = load_book()
            chapter = flatten_chapters(book).get(slug)
            if not chapter:
                self.send_json({"ok": False, "error": "unknown_slug"}, HTTPStatus.NOT_FOUND)
                return
            path = (CONTENT_DIR / chapter["source"]).resolve()

        if not path.exists():
            self.send_json({"ok": False, "error": "missing_path"}, HTTPStatus.NOT_FOUND)
            return

        try:
            os.startfile(str(path))  # type: ignore[attr-defined]
        except Exception as exc:
            self.send_json({"ok": False, "error": "open_failed", "detail": str(exc)}, HTTPStatus.INTERNAL_SERVER_ERROR)
            return

        self.send_json({"ok": True, "path": str(path)})

    def send_json(self, payload: dict, status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    ok, output = run_build()
    if output:
        print(output)
    if not ok:
        raise SystemExit(1)

    server = ThreadingHTTPServer(("127.0.0.1", 8000), BookHandler)
    print("Serving book at http://127.0.0.1:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")


if __name__ == "__main__":
    main()
