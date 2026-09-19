# Improvement Opportunities

This document collects practical improvements that could increase clarity, maintainability, and research value without requiring a major redesign.

## Documentation

- Keep the root `README.md` focused on the benchmark's scope, methodology, limitations, and navigation.
- Record future experiment-specific details close to the corresponding experiment instead of continuously expanding the root README.
- Add a short changelog if the repository begins receiving regular methodological updates.
- Document naming conventions for model directories, experiment identifiers, and prompt versions.

## Repository hygiene

- Keep generated LaTeX intermediate files excluded through `.gitignore`.
- Retain PDFs when they represent experimental evidence or intentionally published compiled outputs.
- If binary artifacts become numerous, consider Git LFS, GitHub Releases, or external archival storage rather than allowing repository history to grow indefinitely.
- Avoid duplicating identical templates across experiments when a shared template plus version identifier is sufficient.

## Evaluation quality

- Convert the main evaluation dimensions into structured data so that Markdown tables can be generated instead of maintained manually.
- Store each finding with a stable identifier, affected model/run, category, evidence location, and severity.
- Distinguish clearly between:
  - source-inherited defects;
  - model-introduced changes;
  - normalization-stage changes;
  - evaluator corrections;
  - unresolved findings.
- Separate descriptive measurements from subjective or heuristic judgments.

## Prompt engineering

- Preserve the original `Prompt.md` as an immutable experiment artifact.
- Introduce future prompt variants under explicit version names rather than editing the original in place.
- Track which instruction classes are followed or ignored, such as:
  - factual preservation;
  - anti-hallucination constraints;
  - bibliography transformations;
  - reporting requirements;
  - output-format compliance.
- Consider decomposing future prompts into reusable modules so individual instruction families can be ablated or tested independently.

## Validation

Potential automated checks include:

- missing required sections;
- unexpected numerical changes;
- altered units;
- dropped paragraphs;
- newly introduced named entities;
- bibliography entries absent from the source;
- malformed BibTeX;
- unresolved citations;
- LaTeX compilation failures;
- inconsistent model metadata.

Automation should assist evaluation, not silently replace human review.
