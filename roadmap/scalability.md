# Scalability Roadmap

The current benchmark contains one manuscript and one observed run per system. That is appropriate for a compact case study, but a larger research program would need stronger experimental structure.

## Scaling dimensions

The benchmark could grow independently along several axes:

- **Manuscripts** — multiple documents, disciplines, lengths, and writing qualities.
- **Prompts** — alternative prompt architectures, instruction orderings, and constraint sets.
- **Models** — multiple providers, model generations, hosted products, and APIs.
- **Trials** — repeated runs of the same condition to measure output variance.
- **Settings** — temperature, reasoning effort, system prompts, tool access, or other controllable inference parameters.
- **Evaluation methods** — automated checks, blinded human review, citation verification, and task-specific metrics.

## Recommended experiment identity

Each future run should have a stable experiment/run identifier derived from explicit metadata rather than its directory name alone.

Example conceptual hierarchy:

```text
experiments/
└── EXP-2026-001/
    ├── experiment.yaml
    ├── prompts/
    ├── inputs/
    ├── runs/
    ├── normalized/
    └── evaluation/
```

A run could then be uniquely associated with:

- experiment ID;
- manuscript ID;
- prompt version;
- provider;
- product/interface;
- model identifier;
- run timestamp;
- inference configuration;
- raw-output checksum.

## Repeated trials

If future claims concern model reliability rather than one observed response, use repeated runs per condition.

Repeated trials would allow analysis of:

- rate of factual alteration;
- variance in editing choices;
- frequency of instruction non-compliance;
- consistency of citations;
- stability of structured output;
- between-run hallucination frequency.

## Binary artifact growth

The present PDF footprint is manageable. If experiments scale significantly:

1. keep lightweight textual artifacts in Git;
2. keep only canonical or publication-ready PDFs in the repository;
3. move high-volume raw captures to Git LFS, Releases, or archival storage;
4. retain hashes and provenance metadata in Git.

## Data formats

Markdown remains useful for human inspection, but scaled analysis benefits from machine-readable files:

- YAML/JSON for run metadata;
- CSV/Parquet for tabular evaluation results;
- JSONL for event/finding records;
- Markdown generated from structured evaluation data for human-readable summaries.

## Aggregate analysis

A future analysis layer could calculate:

- per-model error rates;
- per-prompt adherence rates;
- per-document difficulty patterns;
- bootstrap confidence intervals;
- inter-rater agreement for human evaluations;
- error-category frequencies;
- sensitivity to prompt variants.

Aggregate statistics should only be introduced once the dataset size supports them.
