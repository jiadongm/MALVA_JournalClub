# Malva journal club slides

Quarto/reveal.js slides for the Melbourne Integrative Genomics journal club on 8 October 2026.

## Render

```sh
quarto render slides.qmd
```

Open `slides.html`. The deck uses Quarto's bundled reveal.js resources and a local CSS file.

## Status

The reported examples are based on León-Periñán et al. (Nature, 2026), with cropped paper panels on the result slides. The three demonstration slides still describe planned workflows; no live-query result or plot is claimed yet. Before presenting, verify access to the Malva API, select and test exact probes and datasets, save outputs with the index version and filters, insert the verified demonstration outputs, and rehearse the deck.

Paper: https://doi.org/10.1038/s41586-026-10975-w

## DNMT3A R882H Malva query

The project-local `.venv` has `malva-client` 0.3.4 installed. As of 2 October 2026, Malva account access is denied and the anonymous API returns “Authentication required”; no live result is available. To recreate it:

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-malva.txt
```

[Malva's client](https://malva-client.readthedocs.io/en/latest/quickstart.html) requires an approved account and an API token. Sign in to [Malva](https://malva.mdc-berlin.de/login) with ORCID, then generate a token from the profile menu. Do not commit the token or paste it into the slides. In a local zsh terminal, enter it without echo or shell history:

```zsh
read -s 'MALVA_API_TOKEN?Malva API token: '; echo
export MALVA_API_TOKEN
.venv/bin/python scripts/query_dnmt3a_r882h.py --check
.venv/bin/python scripts/query_dnmt3a_r882h.py
unset MALVA_API_TOKEN
```

The runner submits 47-base reference and R882H sequences in one batch; every 24-base window spans the mutation. This is one base shorter than the documented 48-base SNV example so no shared reference window enters the search. It uses transcript orientation and the [documented SNV filter](https://malva-client.readthedocs.io/en/latest/query_parameters.html) (`max_kmer_presence=50000`). It saves `results/dnmt3a_r882h/aggregate.csv` and `run.json`. To retrieve positive cells for an encoded sample ID from the aggregate output, rerun with `--sample-id ID`; this reuses the saved job and writes `positive_cells_sample_ID.csv`. These are RNA sequence hits, not confirmed cell genotypes; missing hits do not identify reference-genotype cells. The client does not expose an index version in every response, so `run.json` records it only when provided.

The probes use the [GRCh38 reference sequence](https://api.genome.ucsc.edu/getData/sequence?genome=hg38&chrom=chr2&start=25234349&end=25234396) around the [ClinVar R882H locus](https://www.ncbi.nlm.nih.gov/clinvar/variation/375881/). The same mutation appears in the 27-base opening-slide example.

**Mutation-query settings:** The paper's variant benchmark used paired 45-base probes with `w=24` and `tau=1.0` on sample-specific indices. The current `search_sequences()` runner uses 47-base probes and cannot set `w` or `tau`, so it is a prepared exploratory query, not a replication of that benchmark. See `AGENTS.md` for the exact 45-base probes, access routes and next steps.
