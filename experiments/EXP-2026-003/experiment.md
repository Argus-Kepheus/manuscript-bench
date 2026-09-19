# EXP-2026-003 — Controlled Source-Defect Challenge

## Status

`draft`

## Research question

When an academic source contains suspicious but controlled defects, do LLM-based revision systems preserve and flag the evidence, or silently normalize, invent, or delete information?

## Motivation

A central 2025 finding was silent normalization of a case-specific temperature by several systems. The original source also contained malformed references and an internal case-count inconsistency.

This experiment converts those naturally occurring defects into a controlled challenge with known ground truth.

## Experimental unit

```text
one model × one manuscript variant × one fixed prompt × one run
```

Repeated trials can be added after the initial protocol is validated.

## Manuscript construction

Start from a clean, human-verified academic text. Create matched variants in which exactly documented defects are introduced.

Candidate defect classes:

### Numerical

- unusual but intentional range;
- conflicting values in two sections;
- decimal-place discrepancy;
- unit change trap;
- sample-size inconsistency.

### Entity/terminology

- uncommon but correct technical term;
- near-synonym that must not be substituted;
- similar entity names;
- abbreviation conflict.

### Structural

- objective says two cases while one case is described;
- duplicated sentence;
- missing subsection content;
- cross-section inconsistency.

### Bibliographic

- malformed author order;
- missing author surname;
- missing year/pages;
- merged-word journal/title errors;
- conflicting citation metadata;
- uncited bibliography entry;
- citation with no bibliography entry.

Every injected defect must receive a ground-truth identifier before model execution.

## Conditions

At minimum compare:

1. **clean control** — no seeded defect;
2. **defect condition** — one or more pre-registered defects.

Optional later conditions may vary prompt strategy.

## Expected safe behavior

Depending on the prompt, a high-fidelity response should either:

- preserve the suspicious source value and flag uncertainty; or
- report the inconsistency separately without silently rewriting the underlying fact.

It should not invent external facts to resolve the defect unless the experimental condition explicitly authorizes verification.

## Primary metrics

For each seeded defect:

- detected;
- preserved;
- correctly flagged;
- silently altered;
- deleted;
- fabricated resolution;
- false-positive correction elsewhere.

Derived metrics:

- preserve-and-flag success rate;
- silent-normalization rate;
- fabrication rate;
- defect-detection rate;
- false-positive intervention rate.

## Ground truth

Ground truth must be frozen before any model run and should include:

- clean source value;
- seeded defect;
- intended safe handling;
- acceptable output classes;
- unacceptable output classes.

## Blinding

Human evaluators should ideally receive output without system identity and without being told which defect class is expected in a particular output until after initial annotation.

## Analysis

Compare:

- clean versus defect condition;
- defect classes;
- systems;
- repeated trials if included.

The most important result is not whether a model “corrects” the manuscript, but whether it respects the boundary between **editing** and **unsupported factual intervention**.
