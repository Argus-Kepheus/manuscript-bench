# Scalability Roadmap

Manuscript Bench should scale by **adding new experiments**, not by rewriting the original one.

The 2025-10-31 benchmark is a frozen historical evidence set. Its canonical historical state is documented in [`BASELINE.md`](../BASELINE.md) and preserved at commit `47c29f5ccb8231eb7232688d57b865dcf41a039f`.

Concrete candidate experiments are specified in [`experiments.md`](experiments.md).

## Scaling model

The benchmark can expand along independent axes:

- **time** — rerun the original task on later model generations;
- **repetition** — repeat identical conditions to estimate run-to-run variability;
- **documents** — add manuscripts from multiple scientific domains;
- **prompt variants** — introduce controlled prompt ablations or alternative architectures;
- **source defects** — seed known contradictions, numerical traps, and bibliographic corruption;
- **languages** — compare equivalent source content across languages;
- **citation conditions** — vary bibliography quality while holding the manuscript task constant;
- **output schemas** — test compliance with structured reporting requirements;
- **models/products** — compare provider products, model generations, or controlled APIs;
- **settings** — when available, record or manipulate temperature, reasoning effort, tools, browsing, or system prompts.

## Scientific continuity with the baseline

Future work should preserve a stable core task:

> revise an academic manuscript under explicit factual-preservation, anti-hallucination, citation, and output-format constraints.

This continuity allows future experiments to reuse the baseline outcome families:

- factual fidelity;
- unsupported generation;
- completeness;
- citation/reference integrity;
- instruction adherence.

A future experiment may add metrics, but should avoid redefining old metrics in a way that retroactively changes historical interpretation.

## Recommended experiment identity

Each new study should receive a stable identifier:

```text
EXP-YYYY-NNN
```

Each individual execution should receive a run identifier:

```text
RUN-<experiment-id>-NNN
```

Recommended structure:

```text
experiments/
└── EXP-2026-001/
    ├── experiment.md
    ├── experiment.json
    ├── inputs/
    ├── prompts/
    ├── runs/
    ├── normalized/
    └── evaluation/
```

A reusable design template is available at [`experiments/experiment-template.md`](../experiments/experiment-template.md).

## Run metadata

Each run should be associated with:

- experiment ID;
- run ID;
- manuscript/input ID;
- prompt version;
- provider;
- product/interface;
- model identifier/version when known;
- timestamp;
- controllable inference configuration;
- tool/browsing state;
- raw-output content hash.

Unknown metadata must remain explicitly unknown rather than being inferred later.

## Repeated trials

Single runs are useful as observations, but reliability claims require repeated trials.

Repeated runs can estimate:

- probability of factual alteration;
- probability of unsupported additions;
- citation-integrity failure frequency;
- instruction-adherence consistency;
- output-schema reliability;
- between-run textual or structural variance.

Pilot repetitions can be used to characterize variance and validate the protocol. A confirmatory repetition count should then be fixed before the confirmatory stage.

## Controlled comparison

Within one experiment, keep constant whenever possible:

- manuscript;
- prompt text/version;
- evaluation rubric;
- normalization procedure;
- interface/API mode;
- tool access;
- browsing status;
- controllable generation settings.

When provider limitations prevent equivalence, record the difference as metadata instead of assuming conditions are identical.

## Evaluation data formats

Scaled experiments should prefer:

- JSON/YAML for experiment and run metadata;
- CSV/Parquet for aggregate measurements;
- JSON/JSONL for findings;
- Markdown for narrative interpretation;
- checksums/manifests for raw evidence.

Human-readable reports should increasingly be generated from structured data rather than maintained independently.

## Binary artifact growth

The current repository can keep its historical PDFs. If future experiments produce a large volume of captures:

1. keep hashes and lightweight metadata in Git;
2. retain only canonical publication artifacts directly in the repository;
3. use Git LFS, Releases, or archival storage for large evidence collections;
4. never discard provenance linking external evidence to a run.

## Analysis at scale

Once enough observations exist, the project can support:

- per-model and per-prompt error rates;
- confidence intervals for repeated-trial rates;
- prompt-by-model interaction analysis;
- document/domain effects;
- error-category frequencies;
- sensitivity to prompt ablations;
- inter-rater agreement;
- temporal comparison across model generations.

Statistical summaries should be introduced only when the experimental design and sample size make them meaningful.

## Immediate next experiments

The preferred sequence is:

1. temporal replication of the original task;
2. repeated-run reliability;
3. controlled source-defect challenge;
4. citation-integrity stress test;
5. prompt ablation;
6. cross-domain replication;
7. multilingual replication;
8. output-schema/reporting compliance.

Detailed protocols and rationale are in [`roadmap/experiments.md`](experiments.md).
