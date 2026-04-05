from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_PATH = ROOT / "content" / "book.json"


BOOK_UPDATES = {
    "part_title": "Part 3 | Data Complexity in Observational Studies",
    "part_description": "This part focuses on measurement, missingness, temporal ordering, interference, implementation, and aggregation issues in observational data.",
    "homophily_bias": ("4.7", "4.7 Homophily Bias"),
    "ch10-01-covariate-control-limits": ("10", "10. Measurement, Observation, and Missing Data"),
    "ch10-02-s101": ("10.1", "10.1 Measurement Error and Misclassification"),
    "ch10-03-s102": ("10.2", "10.2 Missing Data: MCAR, MAR, MNAR"),
    "ch10-04-s103": ("10.3", "10.3 Strategies for Missingness and Observation Error"),
    "ch11-01-collider-bias": ("11", "11. Time, Dynamics, and Reverse Causality"),
    "ch11-02-s111": ("11.1", "11.1 Temporal Order and Reverse Causality"),
    "ch11-03-s112": ("11.2", "11.2 Baseline Controls, Simultaneity, and Mutual Determination"),
    "ch11-04-s113": ("11.3", "11.3 Cumulative Treatment, Lagged Effects, and Dynamic Causal Effects"),
    "ch12-01-unobserved-confounding-limits": ("12", "12. Interference, Implementation, and Aggregation"),
    "ch12-02-s121": ("12.1", "12.1 Interference and Spillovers: Beyond SUTVA"),
    "ch12-03-s122": ("12.2", "12.2 Implementation Heterogeneity"),
    "ch12-04-s123": ("12.3", "12.3 Aggregated Data, Ecological Fallacy, and Multilevel Context"),
}


FRONT_MATTER_UPDATES = {
    "content/chapters/homophily_bias.md": (
        "4.7 Homophily Bias",
        None,
    ),
    "content/chapters/ch10-01-covariate-control-limits.md": (
        "10. Measurement, Observation, and Missing Data",
        "This chapter explains how measurement error, recording error, and missingness distort observational data before causal analysis even begins.",
    ),
    "content/chapters/ch10-02-s101.md": (
        "10.1 Measurement Error and Misclassification",
        "This section explains how errors in treatment, outcome, and covariate measurement distort causal interpretation.",
    ),
    "content/chapters/ch10-03-s102.md": (
        "10.2 Missing Data: MCAR, MAR, MNAR",
        "This section distinguishes MCAR, MAR, and MNAR and explains why each missingness structure implies a different inferential problem.",
    ),
    "content/chapters/ch10-04-s103.md": (
        "10.3 Strategies for Missingness and Observation Error",
        "This section summarizes multiple imputation, inverse probability weighting, validation data, and sensitivity analysis for data quality problems.",
    ),
    "content/chapters/ch11-01-collider-bias.md": (
        "11. Time, Dynamics, and Reverse Causality",
        "This chapter focuses on temporal ordering, simultaneity, dynamic treatment paths, and reverse causality in observational data.",
    ),
    "content/chapters/ch11-02-s111.md": (
        "11.1 Temporal Order and Reverse Causality",
        "This section explains why apparent causes may actually be consequences and how to diagnose reverse causality.",
    ),
    "content/chapters/ch11-03-s112.md": (
        "11.2 Baseline Controls, Simultaneity, and Mutual Determination",
        "This section explains when baseline adjustment helps and when simultaneity still prevents causal interpretation.",
    ),
    "content/chapters/ch11-04-s113.md": (
        "11.3 Cumulative Treatment, Lagged Effects, and Dynamic Causal Effects",
        "This section explains why treatment can accumulate over time and why delayed effects matter for policy evaluation.",
    ),
    "content/chapters/ch12-01-unobserved-confounding-limits.md": (
        "12. Interference, Implementation, and Aggregation",
        "This chapter explains how spillovers, implementation heterogeneity, and aggregation change the meaning of causal effects.",
    ),
    "content/chapters/ch12-02-s121.md": (
        "12.1 Interference and Spillovers: Beyond SUTVA",
        "This section explains how one unit's treatment can affect another unit's outcome.",
    ),
    "content/chapters/ch12-03-s122.md": (
        "12.2 Implementation Heterogeneity",
        "This section explains why the same policy label can correspond to different realized treatments across places and institutions.",
    ),
    "content/chapters/ch12-04-s123.md": (
        "12.3 Aggregated Data, Ecological Fallacy, and Multilevel Context",
        "This section explains how interpretation changes when evidence is available only at an aggregated level.",
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
    print("fixed toc labels in ascii")


if __name__ == "__main__":
    main()
