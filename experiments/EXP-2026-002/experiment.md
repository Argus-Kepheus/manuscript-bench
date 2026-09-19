# EXP-2026-002 — Run-to-Run Reliability

## Status

`draft`

## Research question

How stable is each LLM-based assistant when the same academic-revision task is repeated under nominally identical conditions?

## Motivation

The frozen baseline and `EXP-2026-001` use one primary observation per system. A single run cannot distinguish systematic behavior from stochastic variation.

## Experimental unit

```text
one product/model × one fixed prompt × one fixed manuscript × one independent run
```

## Design

Select a fixed prompt/manuscript condition. The strongest continuity condition is the frozen 2025 prompt and manuscript, but a later version may be used if explicitly identified.

For each tested system:

1. start independent fresh sessions;
2. submit identical rendered input;
3. preserve each response before any follow-up;
4. keep controllable settings constant;
5. record product/model metadata for every run.

## Repetition strategy

Use two stages:

### Pilot

Run a small set of independent repetitions per system to verify:

- the capture process;
- metric definitions;
- observed variability;
- product limits.

### Confirmatory stage

After the pilot:

- freeze the protocol;
- fix the number of confirmatory repetitions;
- do not change the prompt or primary metric definitions;
- treat additional post-hoc runs as exploratory.

The confirmatory repetition count should be justified by the precision needed for failure-rate estimates and by practical cost constraints, rather than chosen only for convenience.

## Primary outcomes

Per system estimate:

- factual-alteration frequency;
- unsupported-addition frequency;
- citation-integrity failure frequency;
- required-section completion frequency;
- instruction-adherence stability.

## Secondary outcomes

- output length variance;
- between-run lexical/structural similarity;
- variance in number of edits;
- recurrent versus one-off failure types.

## Controls

Keep constant:

- prompt;
- manuscript;
- tool/browsing state;
- product mode;
- available generation controls;
- evaluation rubric;
- normalization pipeline.

## Analysis

Report:

- counts and proportions;
- uncertainty intervals where sample size permits;
- repeated failure patterns;
- within-system variability;
- cross-system comparisons only with explicit caveats about product/API differences.

## Relationship to the baseline

This experiment does not replace the 2025 observation. It tests whether analogous behavior is reproducible within a model/product generation.
