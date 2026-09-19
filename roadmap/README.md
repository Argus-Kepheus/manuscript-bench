# Manuscript Bench Roadmap

This directory documents possible future improvements to **Manuscript Bench** without altering the historical benchmark snapshot.

The current repository should be treated as a preserved experimental baseline. Roadmap items describe possible extensions for future work in prompt engineering, LLM-assisted academic revision, reproducibility, and automated evaluation.

## Guiding principles

1. **Preserve the baseline** — do not silently rewrite the original prompt, inputs, outputs, or retrospective audit.
2. **Version future experiments** — new prompts, manuscripts, evaluation rules, and model runs should be distinguishable from the 2025-10-31 snapshot.
3. **Separate evidence from transformation** — preserve raw outputs independently from normalized LaTeX or derived audit artifacts.
4. **Prefer structured metadata** — important experimental context should be machine-readable where possible.
5. **Automate repeatable checks** — compilation, schema validation, diff-based checks, and evaluation summaries should be reproducible.
6. **Scale incrementally** — introduce infrastructure only when the number of documents, prompts, models, or repeated trials justifies it.

## Roadmap documents

- [`improvements.md`](improvements.md) — near-term quality and maintainability opportunities.
- [`scalability.md`](scalability.md) — how the repository could evolve from a single-study snapshot into a larger benchmark.
- [`modularity.md`](modularity.md) — proposed separation of prompts, raw outputs, normalized artifacts, metadata, evaluation, and tooling.
- [`reproducibility.md`](reproducibility.md) — metadata, versioning, provenance, validation, and automation recommendations.
- [`experiments.md`](experiments.md) — concrete experiment families for temporal replication, reliability, source-defect challenges, citation stress tests, prompt ablations, cross-domain and multilingual replication, and reporting compliance.

## Suggested priority

### Phase 0 — Preserve
Keep the current study unchanged as the historical baseline.

### Phase 1 — Describe
Add structured metadata and explicit version identifiers for any new experiment.

### Phase 2 — Modularize
Separate raw evidence, normalized outputs, evaluation data, and scripts.

### Phase 3 — Automate
Introduce validation scripts and CI for LaTeX, metadata schemas, and repeatable evaluation checks.

### Phase 4 — Scale
Support multiple manuscripts, repeated trials, prompt variants, controlled APIs, and aggregate analysis.

These phases are recommendations, not commitments. They are intended to keep future changes scientifically traceable and proportionate to the project's size.
