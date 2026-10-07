# MALVA Journal Club slide handoff

## Purpose and audience

This project contains Quarto/reveal.js slides for the Melbourne Integrative Genomics journal club on 8 October 2026. The audience includes statisticians, bioinformaticians and biologists. Some attendees may only have skimmed the paper.

Source paper: León-Periñán, Karaiskos & Rajewsky, *Nature* (2026), https://doi.org/10.1038/s41586-026-10975-w.

The presentation asks what direct sequence search adds to gene-count analysis. It introduces the concepts needed to interpret MALVA, then uses biological case studies.

## Division of the presentation

JD introduces the biological and sequencing concepts before Xiaochen's section. Xiaochen covers the technical explanation of MALVA. The shared deck contains one section-divider slide as the placeholder for his material.

JD resumes with concepts and case studies after Xiaochen's section. Do not duplicate Xiaochen's technical explanation unless the user requests it.

## Current deck structure

The main deck has 23 Reveal slides, including the title slide and two section-divider slides.

Before Xiaochen's section:

- The question: which cells contain this sequence?
- Reference genome, illustrated with the Human Genome Project.
- Transcript ends and 3-prime or 5-prime biased single-cell RNA sequencing.

After Xiaochen's section:

- What MALVA adds.
- Allele, genotype and wild type.
- Variant, single-nucleotide variant and single-nucleotide polymorphism.
- Germline, somatic and clonal variation.
- Germline screening and cancer somatic mutation cases.
- Transcript, splice junction and isoform.
- Isoform cases.
- Sequence-based cell clustering and marker sequences.
- Research uses and limitations.
- References and backup slides.

## Current files and style

- `slides.qmd`: presentation source.
- `styles.css`: presentation styling and diagrams.
- `reference.css`: additional generated or supporting styles.
- `slides.html` and `slides_files/`: rendered presentation.
- `figs/`: presentation figures and cropped paper panels.
- `Malva_Xiaochen_part.pptx`: Xiaochen's technical slides for reference.

The current style follows `/Users/jmao1/Library/CloudStorage/Dropbox/Slides/Slides - JD/MonashSpatialCoP_Oct2026`.

The deck uses Source Sans Pro, a white background, navy headings, orange title rules, and blue or peach callouts. Section dividers use a navy background. The canvas is 1280 by 720 pixels.

`quarto render slides.qmd` succeeds. A browser review found no slide-content overflow and no console errors across all 23 slides.

## Working rule during detailed review

The user is reviewing the slides one by one and asking conceptual questions.

Answer conceptual questions in the chat. Do not change the slides unless the user explicitly requests a slide edit. Preserve user-approved wording, narrative order, citations and unrelated edits.

## Scientific interpretation rules

- A reference allele is the base in the chosen reference assembly. It is not necessarily the wild-type or most common allele.
- Wild type depends on the biological comparison and study convention. Do not define it only from the reference genome.
- In common 0, 1 and 2 genotype coding, the value counts copies of the allele defined as the alternate allele. Metadata must define the reference and alternate alleles.
- A sequence hit in RNA provides evidence that the sequence was observed. It does not by itself prove the complete cellular genotype.
- A missing RNA hit does not prove a wild-type genotype. The transcript may be absent, weakly expressed or unsampled at that locus.
- Standard 3-prime single-cell RNA sequencing concentrates reads near polyadenylated transcript ends. It often misses internal coding sites, including DNMT3A codon 882.
- DNMT3A R882H is a useful somatic mutation example. Detecting it in standard single-cell RNA sequencing usually needs suitable coverage or targeted enrichment.
- A negative control sequence is an artificial probe with another base altered. It estimates nonspecific or background matches.
- The concept slide focuses on transcript ends and end-biased sequencing. Introduce unannotated sequences later through the KLK10 and bacterial ribosomal RNA results.

## Known content-review items

These items need a slide edit only when the user requests one:

1. The allele and wild-type slide says that most individuals carry A, then defines T as wild type. This appears internally inconsistent and likely should define A as wild type.
2. The Ptprc exon A source note cites Figure 4. The example is in Figure 3c.
3. The germline case could define “negative control sequence” directly on the slide if the audience needs the term.

Continue to check scientific wording, figure citations and examples during the slide-by-slide review.

## Deferred MALVA demonstration work

The current main deck has no live demonstration slides. Keep the earlier query work as optional future material.

Do not present an untested query, selected dataset or generated plot as a completed result. If a demonstration returns, save the query sequence, dataset, filters, software and index versions, thresholds, denominator, output and reproducible command.

## DNMT3A R882H query notes

Target: DNMT3A `NM_022552.5:c.2645G>A (p.Arg882His)` on the transcript strand. The prepared 47-base reference and R882H probes in `scripts/query_dnmt3a_r882h.py` differ only at base 24. Their 24-mers cross that base.

The GRCh38 genomic change is chr2:25,234,373 C>T on the opposite strand. Verify the coordinate against the UCSC sequence and ClinVar links in `README.md` before changing the probes.

The paper's variant benchmark used paired 45-base probes centred on each single-nucleotide variant. It searched the matching sample index with window size `w=24` and match threshold `tau=1.0`.

The 45-base reference probe is:

`ACTGACGTCTCCAACATGAGCCGCTTGGCGAGGCAGAGACTGCTG`

The 45-base R882H probe is:

`ACTGACGTCTCCAACATGAGCCACTTGGCGAGGCAGAGACTGCTG`

The installed `malva-client` 0.3.4 runner submits paired 47-base probes with `max_kmer_presence=50000`. Its `search_sequences()` method does not expose window size or threshold. A result from that runner would not replicate the paper's variant settings.

The lower-level `submit_search()` client exposes these parameters but has not been tested here for paired batch sequences. The local `MalvaIndex.where()` interface exposes `sliding_size` and `pct_threshold`.

Hosted access was denied on 2 October 2026. The anonymous application programming interface also required authentication. No access token or query result exists in this repository.

The local route requires the MALVA distribution, raw paired FASTQ files, cell barcodes and a built index. No local dataset or index has been selected.

If this work resumes, compare R882H and reference hits within the same samples. Include DNMT3A expression or locus-coverage evidence and relevant sample metadata.

Primary references:

- https://www.nature.com/articles/s41586-026-10975-w
- https://malva.readthedocs.io/en/latest/examples/3_sequence_search.html
- https://malva.readthedocs.io/en/latest/installation.html
- https://malva-client.readthedocs.io/en/latest/query_parameters.html

## Slide conventions

- Use plain scientific English and short points.
- Put one main claim or question on each slide.
- Define unfamiliar terms before using them.
- Keep the algorithm explanation brief.
- Emphasise the biological question and interpretation.
- Distinguish sequence evidence from confirmed genotype, isoform or clone assignment.
- Use Quarto or Pandoc syntax for columns, figures, source notes, emphasis and links where practical.
- Use raw HTML only when Quarto cannot express the layout.
- Preserve citations, user-approved narrative and unrelated edits.

## Next steps

Continue the slide-by-slide wording and scientific review. Apply edits only when the user explicitly requests them.

After the content review, rehearse the timing and perform one final full-deck visual review.
