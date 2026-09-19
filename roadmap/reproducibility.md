# Reproducibility Roadmap

Reproducibility becomes increasingly important if Manuscript Bench is reused for future prompt-engineering research.

## Run metadata

Each future run should record, when available:

```yaml
experiment_id:
run_id:
date:
provider:
product:
model:
model_version:
interface:
prompt_version:
input_id:
temperature:
reasoning_effort:
tools_enabled:
web_access:
system_prompt_control:
notes:
raw_output_sha256:
```

Unknown values should be explicitly recorded as unknown rather than inferred later.

## Provenance

For each derived artifact, preserve enough information to answer:

- Which raw output produced it?
- Which normalization procedure was used?
- Was any manual correction introduced?
- Which prompt and source document were used?
- Which evaluator or script produced the finding?
- Which software/tool version was used?

## Versioning

Recommended versioning layers:

- repository release/tag;
- experiment version;
- prompt version;
- input/document version;
- evaluation-schema version.

The existing experiment should remain identifiable as a fixed baseline.

## Checksums

Hashes are useful for verifying that experimental evidence has not changed.

Candidate files for checksums:

- source manuscript;
- rendered prompt;
- raw output;
- normalized output;
- evaluation dataset.

## Structured evaluation findings

Instead of storing only prose, future findings could use a record such as:

```yaml
finding_id: F-0001
run_id: RUN-...
category: data_fidelity
severity: major
source_excerpt: ...
output_excerpt: ...
status: confirmed
reviewer: ...
notes: ...
```

Human-readable Markdown reports can then be generated from these records.

## Continuous integration

A lightweight CI workflow could eventually check:

- required files exist;
- metadata validates against a schema;
- Markdown links resolve;
- BibTeX parses;
- LaTeX compiles;
- generated reports are up to date;
- evaluation records reference valid runs.

CI should validate reproducibility and repository consistency, not modify raw experimental evidence.

## Controlled future studies

For stronger research claims, future studies should consider:

- multiple manuscripts;
- repeated trials;
- frozen prompt versions;
- controlled API settings where possible;
- blinded human evaluation;
- predefined metrics;
- preregistered evaluation criteria when appropriate;
- explicit separation of exploratory and confirmatory analysis.

The goal is not to make a small repository unnecessarily complex, but to ensure that additional complexity is introduced only when it improves scientific traceability.
