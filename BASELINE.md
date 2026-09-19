# Frozen Baseline — 2025-10-31

The original Manuscript Bench experiment is preserved as historical evidence of the tested systems and their observed behavior at the time of execution.

## Canonical historical state

- **Date:** 2025-10-31
- **Canonical commit:** `47c29f5ccb8231eb7232688d57b865dcf41a039f`
- **Archive branch:** `archive/baseline-2025-10-31`

The archive branch points directly to the last repository state committed on 2025-10-31. It is intended as a human-readable reference to the original experiment before later audit, normalization, documentation, and infrastructure work.

## Evidence policy

The original experiment should be treated as **frozen evidence**, not as a living implementation.

The following principles apply:

1. Do not rewrite the historical prompt to make it better in hindsight.
2. Do not replace model outputs with corrected versions.
3. Do not regenerate historical browser captures and present them as originals.
4. Do not silently repair factual, bibliographic, structural, or formatting failures in raw evidence.
5. Record later corrections only in derived/normalized artifacts and audit documentation.
6. Preserve enough provenance to distinguish:
   - original source/input;
   - original model output;
   - browser/interface evidence;
   - normalization-stage output;
   - retrospective audit;
   - evaluator correction.

## Two preservation layers

Manuscript Bench now uses two complementary preservation mechanisms.

### 1. Historical repository snapshot

`archive/baseline-2025-10-31` preserves the complete repository state as it existed at the end of the original experiment date.

### 2. Evidence manifest on the current branch

`evaluation/baseline-manifest.json` records content hashes for the prompt, shared input, model text outputs, and captured reports that remain part of the active repository.

The CI validator checks these hashes and fails if protected evidence is modified.

## Current `main` branch

The `main` branch may contain later work such as:

- documentation improvements;
- structured evaluation data;
- normalization corrections;
- validation tooling;
- continuous integration;
- scalability and modularity plans.

These later additions do not redefine the historical experiment. When interpreting model behavior, consult the frozen evidence and the retrospective audit together.

## Future experiments

New experiments must receive new identifiers, prompts, inputs, run metadata, and evaluation records. They should never overwrite the 2025 baseline.

The 2025 experiment is therefore the **baseline evidence set**, while future studies are replications, extensions, ablations, or new benchmark instances.
