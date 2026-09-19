# Repository Conventions

These conventions apply to future additions to **Manuscript Bench**. They do not require reorganizing the preserved 2025-10-31 baseline.

## General naming

- Use lowercase kebab-case for new top-level project directories and machine-oriented identifiers.
- Keep established baseline directories such as `LLMs/ChatGPT` unchanged for historical continuity.
- Prefer stable identifiers over descriptive names that may change later.

## Experiments

Recommended identifier:

```text
EXP-YYYY-NNN
```

Example: `EXP-2026-001`.

An experiment groups one research design: defined inputs, prompt version(s), run conditions, and evaluation rules.

## Runs

Recommended identifier:

```text
RUN-<experiment-id>-NNN
```

Example: `RUN-EXP-2026-001-001`.

A run should resolve to one concrete model execution under one defined condition.

## Prompts

The original `Prompt.md` is a preserved baseline artifact and should not be silently edited for future experiments.

Recommended future prompt naming:

```text
prompt-vMAJOR.MINOR.md
```

Examples:

- `prompt-v1.0.md`
- `prompt-v1.1.md`
- `prompt-v2.0.md`

Increment the major version when instruction semantics or expected output structure change substantially. Increment the minor version for compatible refinements that still represent a distinct experimental prompt.

## Model and product names

Record separately, when known:

- provider;
- product/interface;
- model;
- model version.

Do not infer an underlying model identifier when the product did not expose one.

Directory names should identify the tested product or model consistently within a given experiment. The current baseline directory names are preserved as historical labels.

## Evaluation findings

Stable finding IDs should use a category prefix:

- `SRC-` — source-inherited defect;
- `MOD-` — model-introduced change or failure;
- `NORM-` — normalization-stage issue;
- `CORR-` — evaluator correction;
- `UNIV-` — experiment-wide finding.

IDs should never be reused after publication.

## Generated artifacts

- Raw experimental evidence should remain immutable.
- Normalized representations may be corrected, but corrections should be documented.
- Compiled PDFs may be versioned when they are part of the published experimental record.
- Temporary LaTeX build files should remain untracked.

## Commit messages

Prefer concise conventional prefixes where practical:

- `docs:`
- `eval:`
- `fix:`
- `ci:`
- `tooling:`
- `chore:`

These conventions are intentionally lightweight and can be extended if the repository evolves into a larger benchmark suite.
