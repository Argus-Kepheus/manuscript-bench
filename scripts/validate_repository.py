#!/usr/bin/env python3
"""Lightweight consistency checks for Manuscript Bench.

The validator intentionally avoids changing repository content. It treats the
2025-10-31 prompt/input/raw-output evidence as immutable and reports known
scientific/task-compliance gaps as warnings rather than rewriting evidence.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SYSTEMS = [
    "ChatGPT",
    "Claude",
    "Copilot",
    "DeepSeek",
    "Gemini",
    "Grok",
    "Le-Chat",
    "Maritaca",
    "Meta",
    "Perplexity",
    "Qwen",
    "You",
]

REQUIRED_ROOT = [
    "README.md",
    "Prompt.md",
    "EVALUATION.md",
    "HALLUCINATIONS.md",
    "CHANGELOG.md",
    "CONVENTIONS.md",
    "evaluation/results.csv",
    "evaluation/instruction-adherence.csv",
    "evaluation/findings.json",
    "evaluation/baseline-manifest.json",
    "roadmap/README.md",
]

TRANSIENT_SUFFIXES = {
    ".aux",
    ".bbl",
    ".bcf",
    ".blg",
    ".log",
    ".out",
    ".run.xml",
    ".synctex.gz",
    ".fdb_latexmk",
    ".fls",
    ".toc",
    ".lof",
    ".lot",
    ".nav",
    ".snm",
    ".vrb",
}

errors: list[str] = []
warnings: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def check_required_structure() -> None:
    for relative in REQUIRED_ROOT:
        if not (ROOT / relative).exists():
            fail(f"Missing required repository file: {relative}")

    input_path = ROOT / "LLMs" / "Prompt-input.md"
    if not input_path.exists():
        fail("Missing baseline input: LLMs/Prompt-input.md")

    for system in SYSTEMS:
        base = ROOT / "LLMs" / system
        if not base.is_dir():
            fail(f"Missing system directory: LLMs/{system}")
            continue
        for relative in [
            "corrected-text.md",
            "input-corrected-text-report.pdf",
            "LaTeX-output/main.tex",
            "LaTeX-output/reference.bib",
            "LaTeX-output/main.pdf",
        ]:
            if not (base / relative).exists():
                fail(f"Missing expected artifact: LLMs/{system}/{relative}")


def check_baseline_manifest() -> None:
    path = ROOT / "evaluation" / "baseline-manifest.json"
    if not path.exists():
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"Cannot parse baseline manifest: {exc}")
        return

    if data.get("hash_algorithm") != "git_blob_sha1":
        fail("baseline-manifest.json must use hash_algorithm=git_blob_sha1")
        return

    files = data.get("files")
    if not isinstance(files, dict) or not files:
        fail("baseline-manifest.json has no file map")
        return

    for relative, expected in files.items():
        target = ROOT / relative
        if not target.exists():
            fail(f"Baseline evidence missing: {relative}")
            continue
        actual = git_blob_sha1(target)
        if actual != expected:
            fail(
                f"Baseline evidence changed: {relative} "
                f"(expected {expected}, got {actual})"
            )


def check_results_csv() -> None:
    path = ROOT / "evaluation" / "results.csv"
    if not path.exists():
        return
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    except Exception as exc:
        fail(f"Cannot parse evaluation/results.csv: {exc}")
        return

    systems = [row.get("system", "") for row in rows]
    if len(rows) != len(SYSTEMS):
        fail(
            f"evaluation/results.csv should contain {len(SYSTEMS)} rows; "
            f"found {len(rows)}"
        )
    if set(systems) != set(SYSTEMS):
        fail(
            "evaluation/results.csv system set differs from baseline directories: "
            f"{sorted(set(systems) ^ set(SYSTEMS))}"
        )

    ranks = []
    for row in rows:
        try:
            ranks.append(int(row["rank"]))
        except Exception:
            fail(f"Invalid rank for system {row.get('system')}")
    if ranks and sorted(ranks) != list(range(1, len(SYSTEMS) + 1)):
        fail("evaluation/results.csv ranks are not a complete 1..12 sequence")



def check_instruction_adherence_csv() -> None:
    path = ROOT / "evaluation" / "instruction-adherence.csv"
    if not path.exists():
        return
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    except Exception as exc:
        fail(f"Cannot parse evaluation/instruction-adherence.csv: {exc}")
        return

    systems = [row.get("system", "") for row in rows]
    if len(rows) != len(SYSTEMS):
        fail(
            f"evaluation/instruction-adherence.csv should contain {len(SYSTEMS)} rows; "
            f"found {len(rows)}"
        )
    if set(systems) != set(SYSTEMS):
        fail(
            "instruction-adherence system set differs from baseline directories: "
            f"{sorted(set(systems) ^ set(SYSTEMS))}"
        )

    allowed = {"pass", "partial", "fail", "unknown"}
    fields = [
        "factual_preservation",
        "anti_hallucination",
        "bibliography_transformations",
        "reporting_requirements",
        "output_format_compliance",
    ]
    for row in rows:
        for field in fields:
            if row.get(field) not in allowed:
                fail(
                    f"Invalid adherence value for {row.get('system')} / {field}: "
                    f"{row.get(field)!r}"
                )


def check_findings_json() -> None:
    path = ROOT / "evaluation" / "findings.json"
    if not path.exists():
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"Cannot parse evaluation/findings.json: {exc}")
        return

    findings = data.get("findings")
    if not isinstance(findings, list):
        fail("evaluation/findings.json must contain a findings list")
        return

    required = {"id", "origin", "category", "severity", "systems", "status", "summary", "evidence"}
    allowed_origins = {
        "source_inherited",
        "model_introduced",
        "normalization_stage",
        "evaluator_correction",
        "experiment_wide",
    }
    allowed_severity = {"info", "minor", "major"}

    ids: set[str] = set()
    for finding in findings:
        missing = required - set(finding)
        if missing:
            fail(f"Finding missing fields {sorted(missing)}: {finding.get('id')}")
            continue
        fid = finding["id"]
        if fid in ids:
            fail(f"Duplicate finding id: {fid}")
        ids.add(fid)
        if finding["origin"] not in allowed_origins:
            fail(f"Unknown finding origin in {fid}: {finding['origin']}")
        if finding["severity"] not in allowed_severity:
            fail(f"Unknown finding severity in {fid}: {finding['severity']}")
        systems = finding["systems"]
        if not isinstance(systems, list) or not systems:
            fail(f"Finding {fid} has invalid systems list")
        else:
            unknown = [s for s in systems if s != "all" and s not in SYSTEMS]
            if unknown:
                fail(f"Finding {fid} references unknown systems: {unknown}")


def bib_keys(text: str) -> set[str]:
    return set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", text))


def citation_keys(tex: str) -> set[str]:
    keys: set[str] = set()
    for group in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}", tex):
        keys.update(k.strip() for k in group.split(",") if k.strip())
    return keys


def check_latex_and_bibtex() -> None:
    for system in SYSTEMS:
        base = ROOT / "LLMs" / system / "LaTeX-output"
        tex_path = base / "main.tex"
        bib_path = base / "reference.bib"
        if not tex_path.exists() or not bib_path.exists():
            continue

        tex = tex_path.read_text(encoding="utf-8", errors="replace")
        bib = bib_path.read_text(encoding="utf-8", errors="replace")

        if bib.count("{") != bib.count("}"):
            fail(f"Unbalanced braces in LLMs/{system}/LaTeX-output/reference.bib")

        defined = bib_keys(bib)
        cited = citation_keys(tex)
        missing = sorted(cited - defined)
        if missing:
            fail(
                f"Undefined citation keys in {system} main.tex: "
                + ", ".join(missing)
            )

        if not bib.strip():
            warn(f"{system}: reference.bib is empty (known baseline behavior).")

        corrected = ROOT / "LLMs" / system / "corrected-text.md"
        if corrected.exists():
            text = corrected.read_text(encoding="utf-8", errors="replace")
            if "PROCESSING REPORT" not in text.upper():
                warn(
                    f"{system}: mandated PROCESSING REPORT is absent "
                    "(known benchmark finding UNIV-001)."
                )


def check_transient_files() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        name = path.name
        for suffix in TRANSIENT_SUFFIXES:
            if name.endswith(suffix):
                fail(f"Tracked/generated LaTeX transient detected: {path.relative_to(ROOT)}")
                break


def main() -> int:
    check_required_structure()
    check_baseline_manifest()
    check_results_csv()
    check_instruction_adherence_csv()
    check_findings_json()
    check_latex_and_bibtex()
    check_transient_files()

    print("Manuscript Bench repository validation")
    print(f"Errors: {len(errors)}")
    for item in errors:
        print(f"  ERROR: {item}")

    print(f"Warnings: {len(warnings)}")
    for item in warnings:
        print(f"  WARN: {item}")

    if errors:
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
