# MALVA Journal Club slide handoff

## Purpose and audience

Quarto/reveal.js slides for the Melbourne Integrative Genomics journal club on 8 October 2026. The audience includes statisticians, bioinformaticians and biologists; some will only have skimmed the paper.

Source paper: León-Periñán, Karaiskos & Rajewsky, *Nature* (2026), https://doi.org/10.1038/s41586-026-10975-w.

The agreed narrative is: what sequence search adds to gene-count analysis; a short explanation of Malva; germline variants, isoforms, somatic mutations and cell-by-sequence analysis; tool demonstrations; research uses in integration, lineage tracing and HCA clonal haematopoiesis screening.

## Current state

- `slides.qmd`: first content draft, 26 slides including title and references.
- `styles.css`: slide styling and simple diagrams.
- `slides.html` and `slides_files/`: Quarto render output. `quarto render slides.qmd` succeeds.
- Three demonstration slides describe planned workflows. They contain no tested Malva output. The client is not configured on this machine.
- The generated HTML has been checked for slide structure. Visual inspection of the local HTML was blocked by the browser's local-file policy, so layout still needs review in an allowed viewer.

## Next step: insert figures

Add selected, legible paper figure panels to the result slides before expanding the demonstrations. Suggested mapping:

1. Germline screening: Fig. 3b, on “Germline screening · result and boundary”.
2. Isoform usage: Fig. 3c for *Ptprc* and Fig. 3d for *Add2*.
3. Cancer mutations: Fig. 4a–c, focusing on the result and feature-context comparison.
4. Cell-by-sequence analysis: Fig. 5a–c for representation and clustering; Fig. 5e–h for cluster-specific marker sequences.

Use only panels that remain readable at presentation size. Put figure files in `figs/`; cite the paper and panel on each slide. If redrawing or simplifying a panel, label it as adapted and preserve axes, units, groups and statistical meaning. Replace redundant dot points where a figure communicates the result. Render and inspect each changed slide and its neighbours at the intended 16:9 size.

## Slide conventions

- Plain scientific English; short dot points; minimal full sentences.
- One claim or question per slide. Define unfamiliar terms before use.
- Keep the explanation of the algorithm brief. Prioritise biological questions and interpretation.
- Distinguish sequence evidence from confirmed genotype, isoform or clone assignment. A missing RNA hit is not evidence for a wild-type genotype.
- Do not present untested queries, selected datasets or generated plots as completed demonstrations.
- Preserve citations, user-approved narrative and unrelated edits.

## Later work

After figure insertion: select exact probes and datasets; obtain Malva API access or a local index; run and save each demo with its query, filters, sample, index version and denominator; insert verified outputs; rehearse timing and perform full visual QA.
