from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_PATH = ROOT / "content" / "book.json"


def u(text: str) -> str:
    return text.encode("ascii").decode("unicode_escape")


BOOK_UPDATES = {
    "part_title": u("\\uc81c3\\ubd80 | \\uad00\\uce21\\uc790\\ub8cc\\uc640 \\ud604\\uc2e4 \\ub370\\uc774\\ud130\\uc758 \\ubcf5\\uc7a1\\uc131"),
    "part_description": u("\\uad00\\uce21\\uc790\\ub8cc\\uac00 \\uc65c \\uc778\\uacfc\\ucd94\\ub860\\uc744 \\uc5b4\\ub835\\uac8c \\ub9cc\\ub4dc\\ub294\\uc9c0, \\uce21\\uc815\\u00b7\\uacb0\\uce21\\u00b7\\uc2dc\\uac04\\u00b7\\uac04\\uc12d\\u00b7\\uc9d1\\uacc4 \\uc218\\uc900\\uc758 \\ubb38\\uc81c\\ub97c \\uc911\\uc2ec\\uc73c\\ub85c \\uc815\\ub9ac\\ud569\\ub2c8\\ub2e4."),
    "homophily_bias": (
        "4.7",
        u("4.7 \\ub3d9\\uc9c8\\uc131 \\ud3b8\\uc758"),
    ),
    "ch10-01-covariate-control-limits": (
        "10",
        u("10. \\uce21\\uc815, \\uad00\\uce21, \\uacb0\\uce21\\uc758 \\ubb38\\uc81c"),
    ),
    "ch10-02-s101": (
        "10.1",
        u("10.1 \\uce21\\uc815\\uc624\\ucc28\\uc640 \\ubd84\\ub958\\uc624\\ucc28"),
    ),
    "ch10-03-s102": (
        "10.2",
        u("10.2 \\uacb0\\uce21\\uc790\\ub8cc: MCAR, MAR, MNAR"),
    ),
    "ch10-04-s103": (
        "10.3",
        u("10.3 \\uacb0\\uce21\\uacfc \\uad00\\uce21\\uc624\\ub958\\uc5d0 \\ub300\\ud55c \\ub300\\uc751 \\uc804\\ub7b5"),
    ),
    "ch11-01-collider-bias": (
        "11",
        u("11. \\uc2dc\\uac04, \\ub3d9\\ud0dc\\uc131, \\uc5ed\\uc778\\uacfc\\uc131"),
    ),
    "ch11-02-s111": (
        "11.1",
        u("11.1 \\uc2dc\\uac04 \\uc21c\\uc11c\\uc640 \\uc5ed\\uc778\\uacfc\\uc131"),
    ),
    "ch11-03-s112": (
        "11.2",
        u("11.2 \\uc0ac\\uc804\\uac12 \\ud1b5\\uc81c, \\ub3d9\\uc2dc\\uc131, \\uc0c1\\ud638\\uacb0\\uc815"),
    ),
    "ch11-04-s113": (
        "11.3",
        u("11.3 \\ub204\\uc801\\ucc98\\uce58, \\uc9c0\\uc5f0\\ud6a8\\uacfc, \\ub3d9\\ud0dc\\uc801 \\uc778\\uacfc\\ud6a8\\uacfc"),
    ),
    "ch12-01-unobserved-confounding-limits": (
        "12",
        u("12. \\uac04\\uc12d, \\uc9d1\\ud589, \\uc9d1\\uacc4 \\uc218\\uc900\\uc758 \\ubb38\\uc81c"),
    ),
    "ch12-02-s121": (
        "12.1",
        u("12.1 \\uac04\\uc12d\\uacfc \\ud30c\\uae09\\ud6a8\\uacfc: SUTVA\\ub97c \\ub118\\uc5b4\\uc11c"),
    ),
    "ch12-03-s122": (
        "12.2",
        u("12.2 \\uc815\\ucc45\\uc9d1\\ud589\\uc758 \\uc774\\uc9c8\\uc131"),
    ),
    "ch12-04-s123": (
        "12.3",
        u("12.3 \\uc9d1\\uacc4\\uc790\\ub8cc, \\uc0dd\\ud0dc\\ud559\\uc801 \\uc624\\ub958, \\ub2e4\\uc218\\uc900 \\ub9e5\\ub77d"),
    ),
    "ch13-01-regression-matching-ipw": (
        "13",
        u("13. \\uc870\\uac74\\ubd80 \\ub3c5\\ub9bd \\uac00\\uc815\\ud558\\uc758 \\uc778\\uacfc\\ud6a8\\uacfc \\ucd94\\ub860"),
    ),
    "ch13-02-s131": (
        "",
        u("13.1.1 \\uc870\\uac74\\ubd80 \\ub3c5\\ub9bd \\uac00\\uc815(CIA / ignorability)\\uc758 \\uc758\\ubbf8"),
    ),
    "ch13-03-s132": (
        "",
        u("13.1.2 \\ud68c\\uadc0 \\uc870\\uc815\\uc758 \\uc778\\uacfc\\uc801 \\ud574\\uc11d \\uc870\\uac74"),
    ),
    "ch13-04-s133": (
        "",
        u("13.1.3 \\ub9e4\\uce6d\\uc758 \\uc9c1\\uad00 - \\uc774\\uc6c3 \\ub9e4\\uce6d \\u00b7 \\uc131\\ud5a5\\uc810\\uc218 \\ub9e4\\uce6d \\u00b7 \\uce7c\\ud37c \\ubc18\\uacbd"),
    ),
    "ch13-05-s134": (
        "",
        u("13.1.4 \\uc5ed\\ud655\\ub960\\uac00\\uc911(IPW)\\uacfc \\uc548\\uc815\\ud654 \\uac00\\uc911(SIPW)"),
    ),
    "ch13-06-s135": (
        "",
        u("13.1.5 \\uacf5\\ud1b5 \\uc9c0\\uc9c0(common support) - \\uc678\\uc0bd \\uc704\\ud5d8\\uacfc \\uc9c4\\ub2e8"),
    ),
}


FRONT_MATTER_UPDATES = {
    "content/chapters/homophily_bias.md": (
        u("4.7 \\ub3d9\\uc9c8\\uc131 \\ud3b8\\uc758"),
        None,
    ),
    "content/chapters/ch10-01-covariate-control-limits.md": (
        u("10. \\uce21\\uc815, \\uad00\\uce21, \\uacb0\\uce21\\uc758 \\ubb38\\uc81c"),
        None,
    ),
    "content/chapters/ch10-02-s101.md": (
        u("10.1 \\uce21\\uc815\\uc624\\ucc28\\uc640 \\ubd84\\ub958\\uc624\\ucc28"),
        None,
    ),
    "content/chapters/ch10-03-s102.md": (
        u("10.2 \\uacb0\\uce21\\uc790\\ub8cc: MCAR, MAR, MNAR"),
        None,
    ),
    "content/chapters/ch10-04-s103.md": (
        u("10.3 \\uacb0\\uce21\\uacfc \\uad00\\uce21\\uc624\\ub958\\uc5d0 \\ub300\\ud55c \\ub300\\uc751 \\uc804\\ub7b5"),
        None,
    ),
    "content/chapters/ch11-01-collider-bias.md": (
        u("11. \\uc2dc\\uac04, \\ub3d9\\ud0dc\\uc131, \\uc5ed\\uc778\\uacfc\\uc131"),
        None,
    ),
    "content/chapters/ch11-02-s111.md": (
        u("11.1 \\uc2dc\\uac04 \\uc21c\\uc11c\\uc640 \\uc5ed\\uc778\\uacfc\\uc131"),
        None,
    ),
    "content/chapters/ch11-03-s112.md": (
        u("11.2 \\uc0ac\\uc804\\uac12 \\ud1b5\\uc81c, \\ub3d9\\uc2dc\\uc131, \\uc0c1\\ud638\\uacb0\\uc815"),
        None,
    ),
    "content/chapters/ch11-04-s113.md": (
        u("11.3 \\ub204\\uc801\\ucc98\\uce58, \\uc9c0\\uc5f0\\ud6a8\\uacfc, \\ub3d9\\ud0dc\\uc801 \\uc778\\uacfc\\ud6a8\\uacfc"),
        None,
    ),
    "content/chapters/ch12-01-unobserved-confounding-limits.md": (
        u("12. \\uac04\\uc12d, \\uc9d1\\ud589, \\uc9d1\\uacc4 \\uc218\\uc900\\uc758 \\ubb38\\uc81c"),
        None,
    ),
    "content/chapters/ch12-02-s121.md": (
        u("12.1 \\uac04\\uc12d\\uacfc \\ud30c\\uae09\\ud6a8\\uacfc: SUTVA\\ub97c \\ub118\\uc5b4\\uc11c"),
        None,
    ),
    "content/chapters/ch12-03-s122.md": (
        u("12.2 \\uc815\\ucc45\\uc9d1\\ud589\\uc758 \\uc774\\uc9c8\\uc131"),
        None,
    ),
    "content/chapters/ch12-04-s123.md": (
        u("12.3 \\uc9d1\\uacc4\\uc790\\ub8cc, \\uc0dd\\ud0dc\\ud559\\uc801 \\uc624\\ub958, \\ub2e4\\uc218\\uc900 \\ub9e5\\ub77d"),
        None,
    ),
    "content/chapters/ch13-01-regression-matching-ipw.md": (
        u("13. \\uc870\\uac74\\ubd80 \\ub3c5\\ub9bd \\uac00\\uc815\\ud558\\uc758 \\uc778\\uacfc\\ud6a8\\uacfc \\ucd94\\ub860"),
        None,
    ),
    "content/chapters/ch13-02-s131.md": (
        u("13.1.1 \\uc870\\uac74\\ubd80 \\ub3c5\\ub9bd \\uac00\\uc815(CIA / ignorability)\\uc758 \\uc758\\ubbf8"),
        None,
    ),
    "content/chapters/ch13-03-s132.md": (
        u("13.1.2 \\ud68c\\uadc0 \\uc870\\uc815\\uc758 \\uc778\\uacfc\\uc801 \\ud574\\uc11d \\uc870\\uac74"),
        None,
    ),
    "content/chapters/ch13-04-s133.md": (
        u("13.1.3 \\ub9e4\\uce6d\\uc758 \\uc9c1\\uad00 - \\uc774\\uc6c3 \\ub9e4\\uce6d \\u00b7 \\uc131\\ud5a5\\uc810\\uc218 \\ub9e4\\uce6d \\u00b7 \\uce7c\\ud37c \\ubc18\\uacbd"),
        None,
    ),
    "content/chapters/ch13-05-s134.md": (
        u("13.1.4 \\uc5ed\\ud655\\ub960\\uac00\\uc911(IPW)\\uacfc \\uc548\\uc815\\ud654 \\uac00\\uc911(SIPW)"),
        None,
    ),
    "content/chapters/ch13-06-s135.md": (
        u("13.1.5 \\uacf5\\ud1b5 \\uc9c0\\uc9c0(common support) - \\uc678\\uc0bd \\uc704\\ud5d8\\uacfc \\uc9c4\\ub2e8"),
        None,
    ),
}


def fix_book_json() -> None:
    book = json.loads(BOOK_PATH.read_text(encoding="utf-8-sig"))
    for part in book["parts"]:
        if part.get("id") == "part-3":
            part["title"] = BOOK_UPDATES["part_title"]
            part["description"] = BOOK_UPDATES["part_description"]
        for chapter in part["chapters"]:
            if chapter["slug"] in BOOK_UPDATES:
                label, title = BOOK_UPDATES[chapter["slug"]]
                chapter["label"] = label
                chapter["title"] = title
    BOOK_PATH.write_text(json.dumps(book, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fix_front_matter() -> None:
    for rel_path, (title, description) in FRONT_MATTER_UPDATES.items():
        path = ROOT / rel_path
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        for i, line in enumerate(lines):
            if line.startswith("title: "):
                lines[i] = f"title: {title}"
                break
        if description is not None:
            for i, line in enumerate(lines):
                if line.startswith("description: "):
                    lines[i] = f"description: {description}"
                    break
        for i, line in enumerate(lines):
            if line.startswith("# "):
                lines[i] = f"# {title}"
                break
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    fix_book_json()
    fix_front_matter()
    print("fixed part 3 and chapter 13 labels in Korean")


if __name__ == "__main__":
    main()
