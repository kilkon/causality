from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = ROOT / "scripts" / "build.py"
WATCH_PATHS = [
    ROOT / "content",
    ROOT / "assets",
    BUILD_SCRIPT,
]
WATCH_SUFFIXES = {".md", ".json", ".css", ".js", ".py"}


def iter_files(paths: list[Path]) -> list[Path]:
    collected: list[Path] = []
    for path in paths:
        if path.is_file():
            collected.append(path)
            continue
        if path.is_dir():
            for file_path in path.rglob("*"):
                if file_path.is_file() and file_path.suffix.lower() in WATCH_SUFFIXES:
                    collected.append(file_path)
    return sorted(set(collected))


def snapshot(paths: list[Path]) -> dict[str, float]:
    state: dict[str, float] = {}
    for file_path in iter_files(paths):
        try:
            state[str(file_path)] = file_path.stat().st_mtime
        except FileNotFoundError:
            continue
    return state


def run_build() -> bool:
    print("[watch] rebuilding...")
    result = subprocess.run([sys.executable, str(BUILD_SCRIPT)], cwd=ROOT)
    if result.returncode == 0:
        print("[watch] build succeeded")
        return True
    print(f"[watch] build failed with exit code {result.returncode}")
    return False


def watch(interval: float) -> None:
    previous = snapshot(WATCH_PATHS)
    run_build()
    print("[watch] watching for changes. Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(interval)
            current = snapshot(WATCH_PATHS)
            changed = [
                path
                for path, mtime in current.items()
                if previous.get(path) != mtime
            ]
            deleted = [path for path in previous if path not in current]

            if changed or deleted:
                touched = changed + deleted
                print("[watch] change detected:")
                for path in touched[:10]:
                    print(f"  - {path}")
                if len(touched) > 10:
                    print(f"  - ... and {len(touched) - 10} more")
                run_build()
                previous = current
    except KeyboardInterrupt:
        print("\n[watch] stopped")


def main() -> None:
    parser = argparse.ArgumentParser(description="Watch Markdown/book files and rebuild the site automatically.")
    parser.add_argument("--interval", type=float, default=1.0, help="Polling interval in seconds")
    args = parser.parse_args()
    watch(args.interval)


if __name__ == "__main__":
    main()
