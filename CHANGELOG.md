# Changelog

This file records methodological and repository-level changes. It does not reinterpret historical model outputs.

## 2026-09-24

### Repository maintenance

- Removed the `archive/baseline-2025-10-31` branch, whose history was already fully contained in `main`.
- Updated baseline references to point to canonical commit `47c29f5ccb8231eb7232688d57b865dcf41a039f` directly instead of the archive branch.

## 2026-09-19

### Repository identity

- Renamed the repository from `iTec` to `manuscript-bench`.
- Reframed the root documentation around the repository's actual role as a small comparative benchmark for LLM-assisted academic manuscript revision.
- Clarified that the current results come from one manuscript and one observed run per system and are not general model-performance claims.

### Documentation

- Updated `README.md`, `EVALUATION.md`, and `HALLUCINATIONS.md` to align terminology and scope.
- Added `roadmap/` documentation covering improvements, scalability, modularity, and reproducibility.
- Added repository naming and versioning conventions.

### Frozen baseline and experiment planning

- Declared the 2025-10-31 experiment a frozen historical evidence set in `BASELINE.md`.
- Created `archive/baseline-2025-10-31` pointing to canonical historical commit `47c29f5ccb8231eb7232688d57b865dcf41a039f`.
- Added an experiment-driven scalability roadmap and a reusable experiment template.
- Formulated draft protocols for temporal replication, run-to-run reliability, and controlled source-defect testing.

### Evaluation infrastructure

- Added machine-readable evaluation summaries and stable finding identifiers.
- Added a baseline evidence manifest for immutable prompt/input/raw-output artifacts.
- Added repository validation tooling and lightweight continuous integration.

## 2026-09-11

### Audit and normalization maintenance

- Added/updated the comparative evaluation and hallucination/data-fidelity audit.
- Applied documented LaTeX/BibTeX normalization fixes while preserving the original model-output evidence used for comparison.

## 2025-10-31

### Baseline experiment

- Captured the 12-system academic-revision comparison represented by the current benchmark snapshot.

Dates describe repository history as documented by the available artifacts and commits.
