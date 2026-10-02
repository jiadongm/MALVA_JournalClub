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
- Three demonstration slides describe planned workflows. They contain no tested Malva output. The client is installed in a project-local `.venv`, and `scripts/query_dnmt3a_r882h.py` prepares a paired DNMT3A R882H/reference search. Live Malva account access is denied as of 2 October 2026, and the anonymous API returns “Authentication required”; no query result has been obtained.
- The figure slides and their neighbouring setup slides were inspected at 1600 × 900 through a local web server after rendering.

## Next step: obtain Malva access and verify the demonstrations

Select exact probes and datasets, obtain Malva API access or a local index, and run each planned demonstration. Save enough information to reproduce every result:

1. Query or probe sequence.
2. Dataset, sample and cell filters.
3. Malva client and index versions.
4. Thresholds, normalisation and denominator.
5. Saved output and the command or notebook that produced it.

Replace each amber “Pending” note only after the corresponding workflow has run successfully. Distinguish a tested result from an illustrative workflow, and keep the RNA-observability caveats already present in the deck.

## DNMT3A R882H query findings (2 October 2026)

- Target: DNMT3A NM_022552.5:c.2645G>A (p.Arg882His), on the transcript strand. The current 47-base reference and R882H probes in `scripts/query_dnmt3a_r882h.py` differ only at base 24. All their 24-mers cross that base. GRCh38 genomic position: chr2:25,234,373 C>T on the opposite strand; verify against the UCSC sequence and ClinVar links in `README.md` before changing probes.
- Paper's variant benchmark: paired 45-base probes centred on each SNV, searched against the corresponding sample index with window size `w=24` and match threshold `tau=1.0`. The 45-base versions of our probes (one base trimmed from each end) are reference `ACTGACGTCTCCAACATGAGCCGCTTGGCGAGGCAGAGACTGCTG` and R882H `ACTGACGTCTCCAACATGAGCCACTTGGCGAGGCAGAGACTGCTG`.
- Important limitation of the prepared runner: `malva-client` 0.3.4 `search_sequences()` submits the paired 47-base probes with `max_kmer_presence=50000` but does not expose `window_size` or `threshold`. Do not describe a result from that runner as a replication of the paper's variant-specific settings. The lower-level client `submit_search()` exposes those two parameters but has not been tested here for paired batch sequences. The local `MalvaIndex.where()` API exposes `sliding_size` and `pct_threshold`.
- Hosted route: the paper says the public API is accessible to academic users through ORCID, but this account was denied access. The unauthenticated search API requires authentication. Request account approval from the Malva team; then test the API and save results. No token or query result exists in this repository.
- Local route: obtain the Malva wheel or Apptainer distribution from the team, select a dataset with raw paired FASTQs and cell barcodes, build a local index, then query the paired probes with `sliding_size=24`, `pct_threshold=1.0`. No dataset or local index has been selected. The installed `malva-client` is only the hosted API client, not the local indexing tool.
- Interpretation: compare R882H and reference hits in the same samples; include a DNMT3A expression/coverage control and sample metadata. RNA hits are sequence evidence, not definitive cell genotypes. No hit can reflect lack of coverage, especially in 3-prime-biased scRNA-seq.
- Primary references: https://www.nature.com/articles/s41586-026-10975-w (Methods: EGFR and scTML variant probes); https://malva.readthedocs.io/en/latest/examples/3_sequence_search.html (local query API); https://malva.readthedocs.io/en/latest/installation.html (local distribution); https://malva-client.readthedocs.io/en/latest/query_parameters.html (hosted client SNV guidance).

Next session: decide whether hosted access can be approved or choose an appropriate raw-read dataset and obtain the local tool. Then adjust the query runner to the paper's 45-base probes and exact search settings, execute the query, inspect controls and cell-level hits, and only then add a result to the demonstration slides.

## Slide conventions

- Plain scientific English; short dot points; minimal full sentences.
- One claim or question per slide. Define unfamiliar terms before use.
- Keep the explanation of the algorithm brief. Prioritise biological questions and interpretation.
- Distinguish sequence evidence from confirmed genotype, isoform or clone assignment. A missing RNA hit is not evidence for a wild-type genotype.
- Do not present untested queries, selected datasets or generated plots as completed demonstrations.
- Prefer Quarto/Pandoc syntax for columns, figures, source notes, emphasis and links; reserve raw HTML for cases that Quarto cannot express.
- Preserve citations, user-approved narrative and unrelated edits.

## Later work

After demonstration verification: insert the saved outputs, rehearse timing and perform a full-deck visual review.
