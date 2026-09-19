# Improvement Opportunities

This document tracks practical improvements that increase clarity, maintainability, and research value without redesigning the preserved benchmark.

Status legend:

- **Implemented** — present in the repository.
- **Partial** — useful infrastructure exists, but the full opportunity remains open.
- **Future** — intentionally deferred until the project grows or a new experiment is created.

## Documentation

- **Implemented** — Keep the root `README.md` focused on benchmark scope, methodology, limitations, and navigation.
- **Implemented** — Maintain a repository-level `CHANGELOG.md`.
- **Implemented** — Document naming conventions for experiments, runs, prompts, findings, artifacts, and commit messages in `CONVENTIONS.md`.
- **Future** — Put future experiment-specific documentation close to each experiment rather than expanding the root README indefinitely.

## Repository hygiene

- **Implemented** — Ignore common LaTeX, editor, operating-system, and Python temporary files.
- **Implemented** — Retain PDFs that function as experimental evidence or intentional compiled outputs rather than ignoring all PDFs globally.
- **Future** — Move high-volume binary evidence to Git LFS, Releases, or archival storage if the benchmark becomes materially larger.
- **Future** — Avoid template duplication across multiple future experiments by using explicit template versions or shared template references.

## Evaluation quality

- **Implemented** — Store the comparative results in `evaluation/results.csv`.
- **Implemented** — Generate/check the ranking table in `EVALUATION.md` from structured results.
- **Implemented** — Store stable findings with IDs, origin, affected systems, category, severity, status, summary, and evidence reference in `evaluation/findings.json`.
- **Implemented** — Distinguish source-inherited, model-introduced, normalization-stage, evaluator-correction, and experiment-wide findings.
- **Partial** — Separate descriptive measurements from heuristic judgments. Current structured files improve the distinction, but the historical ranking still reflects a retrospective weighting scheme.

## Prompt engineering

- **Implemented** — Protect `Prompt.md`, the shared input, stored model text, and captured reports through `evaluation/baseline-manifest.json`.
- **Implemented** — Define explicit conventions for future prompt versions instead of replacing the baseline prompt.
- **Implemented** — Track factual preservation, anti-hallucination behavior, bibliography transformation, reporting requirements, and output-format compliance in `evaluation/instruction-adherence.csv`.
- **Future** — Decompose a future prompt generation into reusable modules for controlled ablation studies. This should be introduced with a new experiment rather than retrofitted into the historical prompt.

## Validation

### Implemented automated checks

The lightweight validator and CI currently check:

- required repository structure;
- immutability of baseline evidence through content hashes;
- structured evaluation file consistency;
- unique and valid finding identifiers;
- instruction-adherence values;
- expected system coverage;
- basic BibTeX brace consistency;
- undefined LaTeX citation keys;
- accidental tracked LaTeX intermediate files;
- synchronization between `evaluation/results.csv` and the generated table in `EVALUATION.md`.

Known experimental failures, such as the missing `PROCESSING REPORT`, are surfaced as warnings rather than rewritten.

### Future automated checks

These remain useful candidates for a future research iteration:

- semantic detection of unexpected numerical changes;
- altered units;
- dropped paragraphs or propositions;
- newly introduced named entities;
- bibliography entries unsupported by the source;
- deeper BibTeX semantic validation;
- full LaTeX compilation in CI;
- schema validation for future run metadata;
- automated comparison across repeated trials.

Automation should assist evaluation, not silently replace human review.

## Current implementation boundary

The changes implemented in 2026-09-19 deliberately improve infrastructure around the baseline while leaving the original experiment evidence unchanged. More invasive modularization belongs to a future experiment and is tracked separately in `roadmap/modularity.md`.
