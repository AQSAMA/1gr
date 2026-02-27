# Plan — Drafting the Thesis Abstract

## Objective
Create a single, Word-conversion-friendly Markdown abstract (`abstraction_head.md`) that accurately reflects the thesis scope in `allv2.md` (AI across the drug discovery and development pipeline), with a crisp academic tone and no stylistic imitation of specific authors.

## Constraints (Must Follow)
- Do **not** rewrite, paraphrase, or alter thesis chapter content; the abstract must be a faithful high-level overview.
- Avoid generic filler (“this paper explores…”) and avoid marketing language.
- Keep the abstract neither too short nor too long (target: ~180–260 words unless the thesis guidelines require otherwise).
- Maintain academic tone and terminology consistent with the thesis (AI/ML/DL, target identification, virtual screening, docking, de novo design, ADMET, AlphaFold, ethics/regulation, limitations).
- Word-conversion compatibility: plain Markdown, no complex formatting, no tables.

## Inputs to Use
- `1gr/allv2.md` as the source of truth for scope, chapter ordering, and key themes.
- Use Section 1–2 as stylistic reference (clarity and definitions), and ensure the abstract reflects Sections 3–4 emphasis.

## Drafting Steps (Todo-Style)
1. Extract the thesis “through-line”:
   - Traditional discovery constraints (time/cost/attrition; chemical space; translation gaps).
   - Where AI provides leverage: target ID/validation; screening/design; ADMET; platform case studies.
   - Boundaries/limitations: data quality, black-box, need for experimental validation, bias/privacy/regulation.
2. Choose 4–6 core claims to include, each traceable to a chapter:
   - Chapter 1: motivation + definitions.
   - Chapter 2: target discovery + omics/networks + AlphaFold.
   - Chapter 3: screening/docking/generative design + ADMET prediction.
   - Chapter 4: real-world platforms + constraints + future directions.
3. Write a first abstract draft (~200–230 words) with this structure:
   - 1 sentence: problem statement (drug discovery bottlenecks).
   - 2–3 sentences: what AI enables across the pipeline (targets → candidates → safety).
   - 1–2 sentences: real-world exemplars (AlphaFold + end-to-end platforms) without overclaiming.
   - 2 sentences: limitations + need for validation + governance/ethics.
   - Final sentence: concluding thesis claim (AI as augmentative tool; data- and experiment-coupled workflow).
4. Polish for:
   - Precision (no absolute claims; avoid “revolutionizes” unless already supported in text).
   - Density (each sentence carries information; remove filler).
   - Consistency in terms and abbreviations.
5. Save the final abstract into `1gr/abstraction_head.md`.

## Definition of Done
- `abstraction_head.md` exists and contains a clean, single-paragraph abstract (or two short paragraphs if needed for readability).
- Abstract aligns with `allv2.md` scope and avoids unsupported specifics (no new statistics, no new citations).
- Tone: clear, restrained, academically credible.

## Review Notes (to be written after completion)
- Record final word count.
- Note any scope decisions (what was intentionally not mentioned to avoid over-specificity).
- Confirm the abstract does not introduce new facts beyond `allv2.md`.