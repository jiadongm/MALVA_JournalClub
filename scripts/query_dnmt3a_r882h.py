#!/usr/bin/env python3
"""Search Malva for DNMT3A R882H and its reference sequence."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

# GRCh38 chr2:25,234,350-25,234,396, reverse-complemented into
# DNMT3A transcript orientation. Variant at chr2:25,234,373 (C>T on the
# genomic plus strand), NM_022552.5:c.2645G>A.
REFERENCE = "TACTGACGTCTCCAACATGAGCCGCTTGGCGAGGCAGAGACTGCTGG"
R882H = "TACTGACGTCTCCAACATGAGCCACTTGGCGAGGCAGAGACTGCTGG"
VARIANT_INDEX = 23  # zero-based; position 24 in the 47-base probe
K = 24
SERVER = "https://malva.mdc-berlin.de"


def validate_probes():
    differences = [(i, a, b) for i, (a, b) in enumerate(zip(REFERENCE, R882H)) if a != b]
    assert len(REFERENCE) == len(R882H) == 47
    assert differences == [(VARIANT_INDEX, "G", "A")]
    assert all(start <= VARIANT_INDEX < start + K for start in range(len(R882H) - K + 1))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate and print probes without querying")
    parser.add_argument("--sample-id", type=int, help="retrieve positive cells for one encoded Malva sample ID")
    parser.add_argument("--output-dir", type=Path, default=Path("results/dnmt3a_r882h"))
    args = parser.parse_args()
    validate_probes()
    probes = {"seq_1_reference": REFERENCE, "seq_2_R882H": R882H}
    if args.check:
        print(json.dumps({"probes": probes, "variant_position_1_based": VARIANT_INDEX + 1,
                          "k": K, "mutation_spanning_kmers_per_probe": len(REFERENCE) - K + 1}, indent=2))
        return

    import malva_client
    from malva_client import MalvaClient
    from malva_client.config import Config
    from malva_client.exceptions import AuthenticationError

    config = Config.load()
    try:
        client = MalvaClient(base_url=config.server_url or SERVER, api_token=config.api_token)
        run_path = args.output_dir / "run.json"
        if args.sample_id is not None:
            if not run_path.exists():
                raise SystemExit("Run the aggregate query first; no saved run.json was found.")
            run = json.loads(run_path.read_text())
            if run.get("probes") != probes:
                raise SystemExit("Saved job uses different probes; run the aggregate query again.")
            cells = client.retrieve_cells(
                run["job_id"], sample_ids=[args.sample_id], include_sample_metadata=True
            )
            positive = cells.to_dataframe(include_sample_metadata=True)
            args.output_dir.mkdir(parents=True, exist_ok=True)
            output = args.output_dir / f"positive_cells_sample_{args.sample_id}.csv"
            positive.to_csv(output, index=False)
            run.setdefault("retrieved_samples", {})[str(args.sample_id)] = {
                "positive_cell_rows": len(positive), "file": output.name
            }
            run_path.write_text(json.dumps(run, indent=2) + "\n")
            print(f"Saved {len(positive)} positive-cell rows to {output}")
            return

        result = client.search_sequences(
            [REFERENCE, R882H],
            stranded=True,
            min_kmer_presence=0,
            max_kmer_presence=50000,
            max_wait=600,
        )
        aggregate = result.df
        if "results" not in result.raw_data:
            raise RuntimeError("Search completed, but the aggregate result could not be fetched")

        args.output_dir.mkdir(parents=True, exist_ok=True)
        aggregate.to_csv(args.output_dir / "aggregate.csv", index=False)
        run = {
            "run_utc": datetime.now(timezone.utc).isoformat(),
            "variant": "DNMT3A NM_022552.5:c.2645G>A (p.Arg882His)",
            "reference": "GRCh38 chr2:25234350-25234396, reverse complement",
            "reference_url": "https://api.genome.ucsc.edu/getData/sequence?genome=hg38&chrom=chr2&start=25234349&end=25234396",
            "clinvar_url": "https://www.ncbi.nlm.nih.gov/clinvar/variation/375881/",
            "probes": probes,
            "k": K,
            "stranded": True,
            "min_kmer_presence": 0,
            "max_kmer_presence": 50000,
            "client_version": malva_client.__version__,
            "server_url": client.base_url,
            "job_id": result.job_id,
            "job_status": result.status,
            "index_version": result.raw_data.get("index_version"),
            "result_feature_keys": list(result.results.keys()),
            "aggregate_rows": len(aggregate),
        }
        run_path.write_text(json.dumps(run, indent=2) + "\n")
        print(f"Malva job {result.job_id}; {len(aggregate)} aggregate rows")
        print(f"Saved {args.output_dir}")
        print("Select an encoded sample_id from aggregate.csv to retrieve positive cells.")
    except AuthenticationError as exc:
        raise SystemExit(f"Malva authentication required: {exc}. Sign in and set MALVA_API_TOKEN locally.") from None


if __name__ == "__main__":
    main()
