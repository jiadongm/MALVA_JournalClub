# MALVA Journal Club slide handoff

## Purpose and audience

Quarto/reveal.js slides for the Melbourne Integrative Genomics journal club on 8 October 2026. The audience includes statisticians, bioinformaticians and biologists; some will only have skimmed the paper.

Source paper: León-Periñán, Karaiskos & Rajewsky, *Nature* (2026), https://doi.org/10.1038/s41586-026-10975-w.

The agreed narrative is: what sequence search adds to gene-count analysis; a short explanation of Malva; germline variants, isoforms, somatic mutations and cell-by-sequence analysis; tool demonstrations; research uses in integration, lineage tracing and HCA clonal haematopoiesis screening.

## Current state

- `slides.qmd`: 26 slides including title and references.
- `styles.css`: slide styling and simple diagrams.
- `slides.html` and `slides_files/`: Quarto render output. `quarto render slides.qmd` succeeds.
- `figs/`: cropped, presentation-sized panels from paper Figs. 3–5. Result slides now show Fig. 3b–d, Fig. 4a–c and selected Fig. 5 panels with on-slide citations.
- Three demonstration slides describe planned workflows. They contain no tested Malva output. The client is not configured on this machine.
- The figure slides and their neighbouring setup slides were inspected at 1600 × 900 through a local web server after rendering.

## Next step: verify the demonstrations

Select exact probes and datasets, obtain Malva API access or a local index, and run each planned demonstration. Save enough information to reproduce every result:

1. Query or probe sequence.
2. Dataset, sample and cell filters.
3. Malva client and index versions.
4. Thresholds, normalisation and denominator.
5. Saved output and the command or notebook that produced it.

Replace each amber “Pending” note only after the corresponding workflow has run successfully. Distinguish a tested result from an illustrative workflow, and keep the RNA-observability caveats already present in the deck.

## Slide conventions

- Plain scientific English; short dot points; minimal full sentences.
- One claim or question per slide. Define unfamiliar terms before use.
- Keep the explanation of the algorithm brief. Prioritise biological questions and interpretation.
- Distinguish sequence evidence from confirmed genotype, isoform or clone assignment. A missing RNA hit is not evidence for a wild-type genotype.
- Do not present untested queries, selected datasets or generated plots as completed demonstrations.
- Preserve citations, user-approved narrative and unrelated edits.

## Later work

After demonstration verification: insert the saved outputs, rehearse timing and perform a full-deck visual review.
