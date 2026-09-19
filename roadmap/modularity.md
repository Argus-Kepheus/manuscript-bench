# Modularity Roadmap

The current repository is easy to inspect because each system directory contains its corresponding artifacts. If the project grows, stronger modular boundaries would make experiments easier to reproduce and extend.

## Proposed logical modules

### 1. Inputs

Responsible for source manuscripts and immutable input data.

Possible contents:

- source manuscript;
- source bibliography;
- document metadata;
- source checksum.

### 2. Prompts

Responsible for reusable prompt definitions.

Possible contents:

- prompt template;
- prompt version;
- instruction modules;
- change history;
- rendered prompt used for each run.

Future prompt modules could separate:

- editorial rules;
- factual-preservation rules;
- citation rules;
- security/anti-injection rules;
- output-schema requirements;
- reporting requirements.

This would support controlled ablation studies without rewriting the whole prompt.

### 3. Raw runs

Responsible for preserving evidence exactly as returned by a provider/interface.

Possible contents:

- raw text;
- browser capture or API response;
- metadata;
- timestamp;
- provider/model identifiers;
- checksum.

Raw evidence should not be edited after capture.

### 4. Normalization

Responsible for converting heterogeneous raw responses into a common representation.

Possible contents:

- normalized Markdown;
- LaTeX;
- BibTeX;
- compiled PDF;
- transformation log.

Changes made during normalization should be distinguishable from changes made by the model.

### 5. Evaluation

Responsible for findings and derived measurements.

Possible contents:

- structured finding records;
- scoring data;
- human annotations;
- generated summaries;
- hallucination/data-fidelity reports.

### 6. Tooling

Responsible for repeatable processing.

Potential scripts:

- prompt rendering;
- metadata validation;
- diff extraction;
- number/unit comparison;
- BibTeX validation;
- LaTeX compilation;
- report generation.

## Dependency direction

A useful rule is:

```text
inputs + prompts
      ↓
   raw runs
      ↓
 normalization
      ↓
  evaluation
      ↓
   reports
```

Derived artifacts should depend on upstream evidence, never the other way around.

## Compatibility with the current repository

The existing 2025-10-31 benchmark does not need to be reorganized immediately. It can remain a historical snapshot.

A modular architecture is most useful when a second experiment is introduced. At that point, the current study can be designated as a baseline and new experiments can follow the improved structure.
