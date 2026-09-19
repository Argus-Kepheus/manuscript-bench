# EXP-YYYY-NNN — Experiment Title

## Status

`draft | pilot | frozen-protocol | running | complete | archived`

## Research question

State one primary question.

## Motivation

Explain how this experiment relates to the frozen 2025 baseline and which limitation or finding it addresses.

## Hypothesis / exploratory objective

For confirmatory experiments, state the hypothesis before running the confirmatory dataset.

For exploratory experiments, state the objective without retrofitting a hypothesis after observing results.

## Experimental unit

```text
one model × one prompt version × one manuscript × one run
```

Modify only if the experiment requires a different unit.

## Independent variables

- Variable 1:
- Variable 2:

## Controlled variables

- source manuscript:
- prompt version:
- interface/API mode:
- tools:
- browsing:
- normalization pipeline:
- evaluation rubric:

## Systems

| Provider | Product | Model | Version | Interface | Notes |
|---|---|---|---|---|---|

Do not infer unknown model versions.

## Inputs

List source documents and content hashes.

## Prompt(s)

List prompt versions and rendered-prompt hashes.

## Repetition strategy

Define pilot and confirmatory repetitions before running the corresponding stage.

## Primary metrics

Choose the smallest set that answers the main research question.

Candidate core metrics:

- factual alteration count/rate;
- unsupported addition count/rate;
- proposition retention/completeness;
- citation-integrity error count/rate;
- instruction-adherence categories;
- schema-compliance rate.

## Secondary metrics

Optional exploratory measures.

## Ground truth

Document how factual/citation ground truth is established and who reviewed it.

## Raw evidence policy

Raw outputs are immutable after capture. Corrections belong only in normalization or audit layers.

## Normalization

Describe transformations from raw response to normalized Markdown/LaTeX/BibTeX.

## Evaluation procedure

Specify:

- automated checks;
- human review;
- blinding, if any;
- adjudication process;
- finding schema.

## Analysis plan

Specify comparisons, aggregation, uncertainty estimates, and treatment of missing/invalid runs.

## Exclusion criteria

Define conditions under which a run is invalid or excluded.

## Protocol deviations

Populate only after execution.

## Results

Populate after execution.

## Limitations

Populate after execution.

## Provenance

Record repository commit, experiment version, and evidence-manifest location.
