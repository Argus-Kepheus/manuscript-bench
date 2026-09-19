# Manuscript Bench

**Manuscript Bench** is a small, reproducible benchmark for studying how LLM-based assistants revise academic manuscripts under a shared prompt and a common output format.

The repository originated as a prompt-engineering experiment and currently captures one comparative study: the same academic manuscript and revision instructions were submitted to 12 public LLM-based systems/interfaces. Their outputs were normalized into a common LaTeX workflow and audited for factual fidelity, unsupported additions, completeness, and citation/reference integrity.

The project is intentionally narrow. It is useful as a documented case study and as a possible foundation for future research on prompt engineering and LLM-assisted academic editing, but the current results should **not** be interpreted as a general benchmark of model capability.

## Current benchmark

- **Task:** academic manuscript revision and normalization into English.
- **Input:** one retrospective medical case-report draft.
- **Prompt:** one shared revision prompt, preserved in [`Prompt.md`](Prompt.md).
- **Systems compared:** 12 public LLM-based assistants/interfaces.
- **Run date represented by the stored outputs:** 2025-10-31.
- **Evaluation focus:** data fidelity, unsupported fabrication, completeness, and citation/reference integrity.
- **Presentation:** per-system Markdown output, LaTeX source/BibTeX, compiled PDF, and a captured input/output report where available.

Because the benchmark contains **one document and one run per system**, its findings are descriptive of this experiment only. Differences in provider interface, model version visibility, inference settings, and product behavior were not fully controlled.

## Key documents

For a fast review of the study:

- [`EVALUATION.md`](EVALUATION.md) — comparative analysis of the 12 stored outputs and the scoring rationale used in this repository.
- [`HALLUCINATIONS.md`](HALLUCINATIONS.md) — source defects and model-introduced alterations identified during the audit.
- [`Prompt.md`](Prompt.md) — the original academic-revision prompt used as the benchmark instruction artifact.
- [`LLMs/Prompt-input.md`](LLMs/Prompt-input.md) — the shared prompt-plus-manuscript input used for the comparison.
- Each `LLMs/<system>/corrected-text.md` — the stored text produced by that system.
- Each `LLMs/<system>/input-corrected-text-report.pdf` — a browser-captured record of the corresponding interaction/output.
- Each `LLMs/<system>/LaTeX-output/` — normalized LaTeX/BibTeX representation and compiled manuscript.

## Repository structure

```text
manuscript-bench/
├── README.md
├── Prompt.md
├── EVALUATION.md
├── HALLUCINATIONS.md
├── .gitignore
├── LaTeX-template/
│   ├── main.tex
│   ├── reference.bib
│   └── main.pdf
└── LLMs/
    ├── Prompt-input.md
    ├── ChatGPT/
    ├── Claude/
    ├── Copilot/
    ├── DeepSeek/
    ├── Gemini/
    ├── Grok/
    ├── Le-Chat/
    ├── Maritaca/
    ├── Meta/
    ├── Perplexity/
    ├── Qwen/
    └── You/
```

Each system directory follows the same basic layout:

```text
LLMs/<system>/
├── corrected-text.md
├── input-corrected-text-report.pdf
└── LaTeX-output/
    ├── main.tex
    ├── reference.bib
    └── main.pdf
```

## Systems represented

| Directory | Provider / product context | Country |
|---|---|---|
| `ChatGPT` | OpenAI | United States |
| `Claude` | Anthropic | United States |
| `Copilot` | Microsoft | United States |
| `DeepSeek` | DeepSeek | China |
| `Gemini` | Google | United States |
| `Grok` | xAI | United States |
| `Le-Chat` | Mistral AI | France |
| `Maritaca` | Maritaca AI | Brazil |
| `Meta` | Meta AI | United States |
| `Perplexity` | Perplexity | United States |
| `Qwen` | Alibaba | China |
| `You` | You.com | United States |

Specific underlying model identifiers were not consistently exposed by every interface. Where an identifier was recorded in the stored output, it is documented in [`EVALUATION.md`](EVALUATION.md).

## Experimental workflow

The stored benchmark was produced with the following general workflow:

1. Define the academic-revision rules in `Prompt.md`.
2. Couple the source manuscript to the common prompt, producing `LLMs/Prompt-input.md`.
3. Submit that same input through each target LLM-based interface.
4. Preserve the returned text in the corresponding `corrected-text.md`.
5. Normalize the manuscript into a common LaTeX/BibTeX layout.
6. Compile the normalized output to PDF.
7. Audit the outputs against the source text and prompt requirements.
8. Record data-fidelity and citation/reference findings in `HALLUCINATIONS.md` and the comparative analysis in `EVALUATION.md`.

The repository preserves the original prompt as an experimental artifact. Changing that prompt after the benchmark would weaken reproducibility, so future prompt variants should be versioned separately rather than silently replacing it.

## What is being evaluated

The audit emphasizes four dimensions:

1. **Data fidelity** — whether manuscript-specific facts are preserved.
2. **Unsupported fabrication** — whether content, bibliographic data, or terminology is introduced without support from the source.
3. **Completeness** — whether relevant source content and required output structure survive the revision.
4. **Citation/reference integrity** — whether citations and bibliography entries are transformed without corrupting or inventing information.

The current comparison also exposes a useful prompt-engineering question: a prompt can explicitly prohibit unsupported changes and still fail to elicit all requested safeguards or reporting sections. This makes the repository potentially useful as a seed for later research on instruction adherence, output validation, and hallucination control in academic-editing workflows.

## Important limitations

- The benchmark uses only **one manuscript** and one domain.
- Each stored output represents a single observed run, not repeated trials.
- Provider interfaces and inference settings were not standardized.
- Several interfaces did not expose an exact model version.
- The benchmark was conducted through public-facing products rather than a controlled API harness.
- The evaluation documents were created retrospectively by comparing outputs with the source and prompt.
- Rankings in `EVALUATION.md` describe this experiment only and should not be generalized to overall model quality.
- The source manuscript itself contains documented defects; these are separated from model-introduced changes in `HALLUCINATIONS.md`.

## LaTeX normalization

The [`LaTeX-template/`](LaTeX-template/) directory provides the common presentation layer used to normalize the different model outputs. Its purpose is to reduce formatting variability so that manuscript content can be inspected in a consistent form.

The LaTeX files inside each system directory are **normalized representations of the stored model output**, not necessarily verbatim raw responses from the provider interface. The corresponding `corrected-text.md` and browser-captured report should be consulted when provenance matters.

## Research use

The current repository is best treated as:

- a documented case study of LLM-assisted academic revision;
- a small comparative benchmark of instruction following and factual preservation;
- an experimental artifact for prompt-engineering analysis;
- a starting point for future work involving repeated trials, multiple manuscripts, controlled model versions, automated metrics, or API-based evaluation.

It is **not** intended to establish general performance claims about any provider or model.

## Maintenance

Additional project-maintenance material:

- [`BASELINE.md`](BASELINE.md) — frozen 2025-10-31 evidence policy and canonical historical snapshot.
- [`CONVENTIONS.md`](CONVENTIONS.md) — naming and versioning conventions.
- [`CHANGELOG.md`](CHANGELOG.md) — repository and methodology changes.
- [`evaluation/`](evaluation/) — machine-readable evaluation data and the baseline manifest.
- [`roadmap/`](roadmap/) — planned improvements, scalability, modularity, reproducibility, and candidate experiment designs.
- [`experiments/`](experiments/) — workspace and template for future experiments.

A lightweight repository validator is available at `scripts/validate_repository.py`.

## Repository status

The benchmark is currently a completed snapshot rather than an actively expanding dataset. Future work, if added, should preserve the existing 2025-10-31 study as a versioned baseline and introduce new experiments in a way that keeps prompts, inputs, model identifiers, run settings, and evaluation criteria traceable.
