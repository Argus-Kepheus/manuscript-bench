# Candidate Experiments for Scaling Manuscript Bench

This document turns the scalability roadmap into a concrete research program. Every proposed experiment preserves the central logic of the original benchmark: **the same controlled academic-editing task is presented to multiple LLM-based systems and their outputs are evaluated for fidelity, unsupported changes, completeness, citation integrity, and instruction adherence**.

The frozen 2025-10-31 study remains the historical baseline and must not be modified.

## Common experimental unit

The basic unit of analysis should be:

```text
one model × one prompt version × one manuscript × one run
```

Each unit should preserve:

- rendered prompt;
- source manuscript;
- exact raw response;
- product/model metadata;
- run timestamp;
- available inference settings;
- normalization log;
- evaluation records;
- content hashes.

## Common outcome families

Future experiments should reuse a stable core of metrics whenever applicable.

### Factual fidelity

Measure whether the revision:

- preserves numbers;
- preserves ranges and units;
- preserves named entities;
- preserves case-specific facts;
- preserves conclusions and causal claims;
- avoids silently resolving ambiguity.

### Unsupported generation

Count or classify:

- invented facts;
- invented subtitles;
- unsupported terminology substitutions;
- fabricated references;
- unsupported DOI/URL additions;
- merged or synthesized citations.

### Completeness

Measure:

- retained source propositions;
- retained required sections;
- omissions of clinically/scientifically relevant details;
- compliance with requested output sections.

### Citation/reference integrity

Measure:

- citation-key validity;
- source-to-output bibliography coverage;
- author/title/year fidelity;
- invented bibliographic fields;
- unresolved or malformed references.

### Instruction adherence

Reuse the current classes:

- factual preservation;
- anti-hallucination constraints;
- bibliography transformations;
- reporting requirements;
- output-format compliance.

Additional classes can be added without changing historical data.

---

# Experiment family A — Temporal Replication

## EXP-A1 — Same task, later model generation

**Question:** How does performance on the exact 2025 task change when contemporary model/product versions are tested later?

**Design:**

- reuse the original manuscript;
- reuse the original prompt exactly;
- test currently available systems;
- preserve the 2025 outputs as the historical comparison group;
- do not replace unavailable historical systems with assumed equivalents.

**Primary comparisons:**

- factual alterations per run;
- unsupported additions per run;
- citation-integrity failures;
- instruction-adherence profile;
- completion of the required Processing Report.

**Value:** This is the cleanest longitudinal continuation of the original experiment and directly measures behavioral change over time.

---

# Experiment family B — Run-to-Run Reliability

## EXP-B1 — Repeated identical runs

**Question:** Is a system's behavior stable when the same prompt and manuscript are submitted repeatedly under nominally identical conditions?

**Design:**

- same model/product;
- same prompt;
- same manuscript;
- same controllable settings;
- multiple independent fresh conversations/runs.

Start with a pilot number of repetitions and increase it if the observed variability justifies more sampling. For API experiments, predefine the number of repetitions before the confirmatory phase.

**Outcomes:**

- probability of factual alteration;
- variability in citation handling;
- variability in omitted content;
- frequency of fabricated additions;
- instruction-adherence consistency;
- between-run text similarity.

**Value:** Separates a model's characteristic behavior from a single lucky or unlucky response.

---

# Experiment family C — Cross-Domain Replication

## EXP-C1 — Multiple academic domains

**Question:** Are the failure modes observed in the medical case report specific to that domain, or do they recur across academic writing tasks?

**Candidate manuscript domains:**

- mechanical engineering;
- materials science;
- electrical/power systems;
- computer science;
- social science;
- biomedical/clinical writing.

**Design requirements:**

- manuscripts of comparable scope where possible;
- known ground-truth facts;
- explicit bibliography;
- documented source defects;
- common revision prompt;
- blinded or source-aware audit depending on the metric.

**Outcomes:** Same core metrics as the baseline, plus domain-specific failure categories if needed.

**Value:** Tests generalizability without abandoning the original benchmark structure.

---

# Experiment family D — Controlled Source-Defect Challenge

## EXP-D1 — Seeded factual and bibliographic traps

**Question:** Can models preserve questionable source content while correctly flagging uncertainty, rather than silently “fixing” it?

Create controlled manuscript variants containing known, pre-registered defects such as:

- conflicting numerical values;
- unusual but intentional ranges;
- inconsistent sample counts;
- malformed author lists;
- missing bibliography fields;
- terminology that looks wrong but must be preserved;
- duplicated or uncited references.

Each seeded defect must have a ground-truth record before any model is tested.

**Primary outcomes:**

- preserve-and-flag success rate;
- silent correction rate;
- fabrication rate;
- defect detection rate;
- false-positive correction rate.

**Value:** Directly tests the behavior that produced the strongest finding in the original benchmark: models silently normalizing a case-specific value.

---

# Experiment family E — Prompt Ablation

## EXP-E1 — Which prompt modules actually matter?

**Question:** Which instruction classes reduce factual drift or improve reporting compliance?

Create a future modular prompt and test controlled variants such as:

- full prompt;
- minus anti-hallucination module;
- minus factual-preservation module;
- minus bibliography rules;
- minus output-schema rules;
- reordered instruction blocks;
- concise versus detailed constraints.

Do **not** decompose or rewrite the historical prompt in place. This experiment requires a new prompt generation/version.

**Primary outcomes:**

- change in factual-fidelity failures;
- change in unsupported additions;
- change in Processing Report compliance;
- change in citation-integrity failures;
- token/output-length cost.

**Value:** Converts the project from model comparison into a genuine prompt-engineering experiment.

---

# Experiment family F — Citation Integrity Stress Test

## EXP-F1 — Clean versus corrupted bibliography

**Question:** How do models behave when citation metadata ranges from clean to partially corrupted?

Prepare matched manuscript conditions:

1. clean bibliography;
2. minor typographic corruption;
3. missing fields;
4. malformed author strings;
5. conflicting metadata;
6. deliberately ambiguous citation.

Models should be instructed to preserve evidence, flag uncertainty, and avoid unsupported completion.

**Primary outcomes:**

- correct transformation rate;
- unsupported metadata completion rate;
- citation fabrication rate;
- safe uncertainty-flagging rate.

**Value:** Isolates one of the clearest weaknesses observed in the original experiment.

---

# Experiment family G — Multilingual Academic Revision

## EXP-G1 — Same content, different input languages

**Question:** Does factual preservation change when equivalent academic content is supplied in different languages and normalized to English?

Candidate languages already compatible with the project's original intent:

- Portuguese;
- Spanish;
- English.

Use semantically equivalent source versions reviewed by a human bilingual evaluator.

**Primary outcomes:**

- factual fidelity;
- terminology preservation;
- omission rate;
- citation integrity;
- translation-induced semantic drift.

**Value:** Tests an explicit capability claimed by the original prompt framework but not systematically benchmarked.

---

# Experiment family H — Output-Schema and Reporting Compliance

## EXP-H1 — Structured reporting reliability

**Question:** Why did none of the original systems produce the complete mandated Processing Report?

Test a future task with a strict, machine-checkable schema.

Conditions may compare:

- prose instructions only;
- explicit Markdown schema;
- JSON schema;
- short schema versus long schema;
- schema repeated at the beginning and end of the prompt.

**Primary outcomes:**

- required-field completion;
- schema validity;
- missing-section frequency;
- factual-fidelity trade-off;
- output truncation or refusal behavior.

**Value:** Directly investigates the universal failure recorded as `UNIV-001`.

---

# Suggested execution order

The most informative next sequence is:

1. **EXP-A1 Temporal Replication** — closest possible replication of the original study.
2. **EXP-B1 Run-to-Run Reliability** — determine whether single-run comparisons are stable.
3. **EXP-D1 Source-Defect Challenge** — test the main factual-fidelity failure mechanism.
4. **EXP-F1 Citation Integrity Stress Test** — isolate bibliography behavior.
5. **EXP-E1 Prompt Ablation** — move from observation to causal prompt-engineering analysis.
6. **EXP-C1 Cross-Domain Replication** — test external validity.
7. **EXP-G1 Multilingual Revision** — test language-transfer robustness.
8. **EXP-H1 Reporting Compliance** — isolate schema/instruction-following behavior.

This ordering keeps early experiments maximally comparable with the frozen baseline before introducing broader domain and prompt changes.

## Exploratory versus confirmatory work

For each experiment:

- use a small pilot to validate the protocol and data pipeline;
- freeze the protocol before the confirmatory runs;
- predefine primary metrics;
- separate exploratory observations from confirmatory claims;
- do not tune the prompt on the same runs later used as confirmatory evidence.

## What should remain constant

When comparing models within one experiment, keep constant whenever technically possible:

- source manuscript;
- prompt text/version;
- interface/API mode;
- enabled tools;
- browsing status;
- output-format requirement;
- evaluation rubric;
- normalization procedure.

Any unavoidable differences should be recorded explicitly rather than treated as equivalent.
