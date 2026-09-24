# EXP-2026-001 — Temporal Replication of the 2025 Benchmark

## Status

`draft`

## Research question

How do currently available LLM-based assistants behave on the **exact academic-revision task used in the frozen 2025-10-31 benchmark**, and which observed failure modes persist, disappear, or newly appear?

## Motivation

This is the closest possible replication of the original Manuscript Bench experiment. It provides a longitudinal comparison while leaving the historical evidence untouched.

## Baseline reference

- Historical date: 2025-10-31
- Historical commit: `47c29f5ccb8231eb7232688d57b865dcf41a039f`
- Protected prompt hash: see `evaluation/baseline-manifest.json`
- Protected input hash: see `evaluation/baseline-manifest.json`

The prompt and shared input must be reproduced from the frozen evidence, not from a rewritten version.

## Experimental unit

```text
one product/model × original prompt × original manuscript × one fresh run
```

## Primary objective

Replicate the original single-run comparison as faithfully as contemporary products permit.

Repeated-run reliability is intentionally separated into `EXP-2026-002`.

## Independent variable

Tested system/product/model at the replication date.

## Controlled variables

Keep constant whenever possible:

- original prompt content;
- original source manuscript;
- fresh conversation/session;
- no additional user follow-up before the captured response;
- same requested output;
- same normalization and evaluation rubric;
- same evidence-capture procedure across products.

Any product-imposed differences must be recorded rather than hidden.

## Target systems

Attempt to include the same product families represented in 2025 where they remain publicly available:

- ChatGPT;
- Claude;
- Copilot;
- DeepSeek;
- Gemini;
- Grok;
- Le Chat;
- Maritaca;
- Meta AI;
- Perplexity;
- Qwen;
- You.com.

The exact current model must be recorded only when the product exposes it. A product that no longer exists or cannot reproduce the interaction mode should be recorded as unavailable rather than replaced silently.

## Primary metrics

1. factual preservation;
2. unsupported fabrication;
3. completeness;
4. citation/reference integrity;
5. instruction-adherence profile;
6. presence/absence of the mandated Processing Report.

## Direct longitudinal comparisons

At minimum, compare:

- case-specific temperature preservation;
- title alteration;
- unsupported subtitle generation;
- DOI/reference invention;
- citation-list corruption or repair;
- missing source details;
- bibliography conversion;
- Processing Report completion.

These are directly connected to documented 2025 findings.

## Raw evidence

For every system preserve:

- timestamp;
- provider/product;
- exposed model identifier;
- exact rendered input;
- raw output;
- interface capture where feasible;
- content hashes;
- notes on product features that could affect comparability.

## Evaluation

Use the current structured finding categories and instruction-adherence matrix.

Where feasible, human reviewers should evaluate de-identified outputs before seeing the system identity.

## Exclusion criteria

A run is invalid for the primary replication if:

- the wrong prompt/input was submitted;
- the response was manually edited before preservation;
- the session contained unrelated prior context;
- a product failure prevented a substantive response;
- tools/browsing materially changed the task when the comparison condition required them to be absent.

Invalid runs remain documented but are not used as the primary replication observation.

## Analysis

The primary output is descriptive:

- per-system finding set;
- 2025 versus replication differences by finding category;
- persistence/new-resolution/new-failure labels;
- instruction-adherence comparison.

Do not interpret one new run as a statistically stable estimate of model reliability.

## Protocol freeze

Before executing any model:

1. finalize the target date/window;
2. freeze this protocol;
3. record current product availability;
4. freeze the evaluation rubric;
5. record the exact prompt/input hashes used.

After the protocol is frozen, substantive changes require a documented amendment.
