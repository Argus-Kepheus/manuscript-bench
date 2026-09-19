#!/usr/bin/env python3
"""Generate or verify the ranking table in EVALUATION.md from evaluation/results.csv."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "evaluation" / "results.csv"
DOC_PATH = ROOT / "EVALUATION.md"

BEGIN = "<!-- BEGIN GENERATED RESULTS TABLE -->"
END = "<!-- END GENERATED RESULTS TABLE -->"


def escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def render() -> str:
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    lines = [
        "| Rank | Model | Data fidelity | Fabrication | Completeness | Citation integrity | Notable issue |",
        "|---:|---|---|---|---|---|---|",
    ]
    for row in sorted(rows, key=lambda r: int(r["rank"])):
        lines.append(
            "| {rank} | {system} | {data_fidelity} | {fabrication} | {completeness} | "
            "{citation_integrity} | {notable_issue} |".format(
                **{key: escape(value) for key, value in row.items()}
            )
        )
    return "\n".join(lines)


def expected_document(current: str) -> str:
    table = render()
    replacement = f"{BEGIN}\n{table}\n{END}"
    if BEGIN not in current or END not in current:
        raise RuntimeError("Generated-table markers are missing from EVALUATION.md")
    before, rest = current.split(BEGIN, 1)
    _, after = rest.split(END, 1)
    return before + replacement + after


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if EVALUATION.md is out of sync")
    parser.add_argument("--write", action="store_true", help="update EVALUATION.md in place")
    args = parser.parse_args()

    current = DOC_PATH.read_text(encoding="utf-8")
    expected = expected_document(current)

    if args.write:
        DOC_PATH.write_text(expected, encoding="utf-8")
        print("Updated EVALUATION.md")
        return 0

    if args.check:
        if current != expected:
            print("EVALUATION.md generated table is out of sync with evaluation/results.csv")
            return 1
        print("Evaluation table is in sync.")
        return 0

    print(render())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
