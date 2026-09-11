# Hallucination & Data-Fidelity Audit

This document flags every place where a model's output in `LLMs/` diverges from the
original source text in `LLMs/Prompt-input.md`, in violation of `Prompt.md`'s own
anti-hallucination rule:

> **PRESERVE:** All original data, conclusions, terminology | Flag `[UNCLEAR: reason]` vs assuming

It was produced by diffing each model's `corrected-text.md` and `LaTeX-output/main.tex`
against the raw input line-by-line. Findings are split into two categories:

- **Source-inherited defects** — errors that already exist in the human-authored draft.
  These are not hallucinations; they're listed so that a model *catching and flagging* one
  isn't confused with a model *causing* one, and so a model that quietly repeats one isn't
  wrongly accused of inventing it.
- **Model-introduced alterations** — content a specific model changed, added, or dropped
  relative to the source, without the `[UNCLEAR]`/`[MISSING]` flag Prompt.md requires.

A companion comparative ranking is in [`EVALUATION.md`](EVALUATION.md).

---

## 1. Source-inherited defects (not hallucinations)

These already exist in `LLMs/Prompt-input.md` and predate every model's involvement:

1. **Garbled citation #4 (Azzopardi et al. 2014).** The source's author list ends
   `HALLIDAY, Henry L.; THE NEW ENGLAND JOURNAL O F MEDICINE, Edmund` — the journal name has
   been spliced into the author list, most likely from a broken citation-manager export. The
   real paper almost certainly has a co-author named Edmund (plausibly "Edmund Juszczak", a
   statistician on the actual TOBY-register NEJM 2014 trial), but this is **not independently
   verified here** — see how each model handled it in §2.
2. **Reference #6 (Thayyil et al. 2021)** has typos in the source itself: double commas in
   two author names (`PANT, , Stuti`; `IVAIN, , Phoebe`) and no page numbers given at all.
3. **Reference #7 (Abate et al. 2021)** has merged-word typos in the source itself:
   `hypoxic-ischemicencephalopathy`, `randomized controltrials`, and journal name `PloSone`.
4. **Reference #1 (Machado & Lavor 2018)** gives its month in abbreviated Portuguese,
   `jul./set.`, in the source itself — not a model invention.
5. **"Two clinical cases" vs. one case described.** The Objective, Methods, and Conclusion
   all say "two clinical cases" / "two children", but the source's "Case description" section
   only ever describes **one** patient. This inconsistency is in the raw draft. Prompt.md
   requires flagging `INCOMPLETE DESCRIPTIONS` — none of the 12 outputs flagged it (see §3).
6. **Case-specific incubator temperature.** The source's Case description gives the target
   temperature for *this specific infant* as `32° - 35°C`, distinct from the general
   literature figure `33ºC - 34ºC` cited in the Introduction. The 32–35°C figure is unusually
   wide for a therapeutic-hypothermia protocol and may itself be an imprecision in the
   original human draft — but Prompt.md's rule is to preserve it and flag `[UNCLEAR]`, not
   silently correct it. Whether each model preserved or altered it is tracked in §2.

## 2. Model-introduced alterations

### Case-specific temperature (source: 32–35°C)

| Model | Case temperature reported | Verdict |
|---|---|---|
| ChatGPT | 32–35°C | preserved |
| Claude | 33–34°C | **altered, unflagged** |
| Copilot | 32–35°C | preserved |
| DeepSeek | 33–34°C | **altered, unflagged** |
| Gemini | 32–35°C | preserved |
| Grok | 33–35°C | **altered, unflagged** (hybrid: kept upper bound, changed lower bound) |
| Le-Chat | 33–34°C | **altered, unflagged** |
| Maritaca | 32–35°C | preserved |
| Meta | *(not reported — Case section truncated)* | dropped, not altered |
| Perplexity | 32–35°C | preserved |
| Qwen | 32–35°C | preserved |
| You | 32–35°C | preserved |

4 of 12 models silently conformed the patient-specific figure to the literature-average
figure from the Introduction, with no `[UNCLEAR]` flag anywhere in their output.

### Garbled source citation (Azzopardi et al. 2014 author list)

| Model | Resulting author list ending | Verdict |
|---|---|---|
| ChatGPT | `...Halliday, Henry L. and Edmund, The New England Journal of Medicine` | kept the source defect verbatim |
| Claude | `...Halliday, Henry L. and others` | safe truncation |
| Copilot | `...Goodwin, Julia and Halliday, Henry L.` | safe truncation |
| DeepSeek | `...Halliday, Henry L. and Edmund, [MISSING: first name]` | confused flag — mislabels "Edmund" (already a first name) as missing its first name |
| Gemini | `...Halliday, Henry L. and Edmund` | partial cleanup, still a dangling fragment |
| Grok | `...Halliday, Henry L. and Juszczak, Edmund` | **resolved to a plausible real name** — unverified against the published paper, but the only model to recognize "Edmund" as a stray first name and pair it with a surname rather than drop or repeat it |
| Le-Chat | `...Halliday, Henry L. and New England Journal of Medicine, Edmund` | kept the source defect verbatim |
| Maritaca | `...Eddama, Oya and The New England Journal of Medicine, Edmund` (also dropped Goodwin and Halliday) | kept the source defect verbatim, plus lost two real authors |
| Perplexity | `Azzopardi, Denis et al.` | truncated after the first author |
| Qwen | `...Goodwin, Julia and Halliday, Henry L.` | safe truncation |
| You | *(same pattern as Qwen/Copilot)* | safe truncation |

### Invented title subtitles (not present in the source)

- **Grok**: `Neonatal Hypothermia and Neonatal Anoxia: Clinical Outcomes and Motor Development Following Therapeutic Hypothermia`
- **Le-Chat**: same subtitle as Grok, verbatim
- **Maritaca**: `Therapeutic Hypothermia and Neonatal Anoxia: Case Reports on Neuroprotection and Motor Development`

None of these subtitles appear in the source title (`NEONATAL HIPOTERMIA AND NEONATAL ANOXIA`) or anywhere in the input text.

### Unflagged terminology change

- **Gemini** retitled the paper `Neonatal Hypothermia and Hypoxic-Ischemic Encephalopathy`,
  replacing "Neonatal Anoxia" with a related but different diagnosis-adjacent term, with no flag.

### Unflagged data additions

- **Le-Chat** added DOI fields to four bibliography entries (`Azzopardi2014`, `Thayyil2021`,
  `Abate2021`, `Silveira2015`) that are absent from the source reference list. The DOIs look
  plausible but are unverified additions, not confirmed facts, and were added with no
  `[UNCLEAR]`/`[MISSING]` flag.

### Citation fabrication via merging

- **Maritaca**'s `Laptook2017` BibTeX entry combined Laptook et al.'s real author list with
  Thayyil et al.'s real author list (`Montaldo, Shukla, Oliveira, Ivain`) into one entry —
  attributing four people to a paper they didn't write. The source has both papers as
  separate, correctly-formed references. (This has been corrected in the working tree as
  part of the LaTeX bug-fix pass; flagged here as the citation-integrity error it originally was.)

### Internal inconsistency between a model's own two output stages

- **Maritaca**: the "late neonatal sepsis... six days of antibiotic therapy" detail (which
  *is* present in the true source) is missing from Maritaca's own `corrected-text.md`, then
  reappears in its `main.tex`. Not a fabricated fact, but a sign the two stages of Maritaca's
  own pipeline weren't consistent with each other.
- **Meta**: titled the paper `NEONATAL HIPOTERMIA AND PERINATAL ASPHYXIA` in its own
  `corrected-text.md`, then `Neonatal Hypothermia and Neonatal Anoxia` in its own `main.tex` —
  the title changed between Meta's own two stages.

### Citation conversion never performed

- **Meta** left `reference.bib` completely empty and never converted the source's raw
  numeric markers (`[4,6,7]`) into `\cite{}` calls anywhere in the text — a direct violation
  of Prompt.md's `INLINE_TRANSFORMS` rule, not a data alteration but a task-completion failure.

## 3. Universal, repo-wide gap

**None of the 12 outputs include the `## PROCESSING REPORT` section** that Prompt.md's
Output Structure mandates (a Summary, Security issues, a full Changes table/list, and an
Issues section specifically meant to surface `INCOMPLETE DESCRIPTIONS`, `MISSING DETAILS`,
`NUMERICAL MISMATCHES`, and `UNCITED REFERENCES`). Every `corrected-text.md` in the repo
contains only the "CORRECTED TEXT" half of the required output. This is very likely *why*
the "two cases but one described" inconsistency (§1.5) was never surfaced by any model — the
mechanism Prompt.md designed specifically to catch it was never produced by any of them.
