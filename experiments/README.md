# Future Experiments

This directory is reserved for new Manuscript Bench studies.

The original 2025-10-31 experiment is **not** being moved here. It remains preserved in its historical layout and is additionally referenced by `BASELINE.md` and canonical commit `47c29f5ccb8231eb7232688d57b865dcf41a039f`.

## Rule

A new experiment must never overwrite baseline evidence.

Each future experiment should receive a stable identifier such as:

```text
EXP-2026-001
```

Recommended structure:

```text
experiments/
└── EXP-YYYY-NNN/
    ├── experiment.md
    ├── experiment.json
    ├── inputs/
    ├── prompts/
    ├── runs/
    ├── normalized/
    └── evaluation/
```

## Minimum experiment record

Before data collection, document:

- research question;
- hypothesis or exploratory objective;
- independent variables;
- dependent variables/metrics;
- control condition;
- inclusion/exclusion rules;
- target systems/models;
- repetition strategy;
- normalization procedure;
- evaluation procedure;
- planned analysis.

After data collection, add:

- exact run metadata;
- raw evidence hashes;
- deviations from protocol;
- structured findings;
- analysis outputs;
- limitations.

Use `experiment-template.md` when creating a new study.

## Draft studies

The following protocols are formulated but not yet executed:

- [`EXP-2026-001`](EXP-2026-001/experiment.md) — temporal replication of the frozen 2025 task on later product/model generations.
- [`EXP-2026-002`](EXP-2026-002/experiment.md) — repeated identical runs to measure run-to-run reliability.
- [`EXP-2026-003`](EXP-2026-003/experiment.md) — controlled source defects to measure preserve-and-flag behavior versus silent normalization.

Additional experiment families are described in [`roadmap/experiments.md`](../roadmap/experiments.md).
