# Structured Evaluation Data

This directory provides machine-readable companions to the human-readable `EVALUATION.md` and `HALLUCINATIONS.md`.

The Markdown documents remain the narrative source for interpretation. The structured files exist to reduce manual duplication and make future automation possible.

## Files

- `results.csv` — one row per tested system, mirroring the current comparative table.
- `findings.json` — stable, categorized audit findings with identifiers and provenance.
- `baseline-manifest.json` — content-addressed manifest protecting baseline prompt/input/raw-output evidence.

## Scope

These files describe the single 2025-10-31 benchmark snapshot. They are **not** a general model leaderboard.

## Finding origins

- `source_inherited` — the defect existed in the source manuscript.
- `model_introduced` — a stored model output added, altered, omitted, or failed to perform something relative to the prompt/source.
- `normalization_stage` — an issue was introduced during downstream normalization rather than by the model.
- `evaluator_correction` — a repository maintainer corrected a derived/normalized artifact after audit.
- `experiment_wide` — the finding applies across the benchmark.

## Severity

Severity is descriptive within this experiment:

- `info` — contextual or traceability information.
- `minor` — limited formatting/hygiene issue.
- `major` — substantive task-compliance, factual-fidelity, completeness, or citation-integrity issue.

Severity does not represent medical or real-world risk.
