"""New companion utilities. No model training or deployment scoring."""
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATES = ("present", "weak", "absent", "not_assessed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    refs = commands.add_parser("references", help="search the article's bibliography")
    refs.add_argument("--query", default="")
    refs.add_argument("--number", type=int)
    refs.add_argument("--limit", type=int, default=10)
    refs.add_argument("--json", action="store_true")
    sheet = commands.add_parser("worksheet", help="summarise descriptive worksheet entries")
    sheet.add_argument("--file", type=Path, required=True)
    sheet.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "references":
            if args.limit < 1:
                raise ValueError("--limit must be positive")
            records = json.loads((ROOT / "catalogue/references.json").read_text(encoding="utf-8"))
            found = [r for r in records if args.query.casefold() in r["citation_text"].casefold()
                     and (args.number is None or r["reference_number"] == args.number)]
            result = {"matches": len(found), "shown": len(found[:args.limit]), "records": found[:args.limit]}
            if args.json:
                print(json.dumps(result, indent=2, ensure_ascii=False))
            else:
                print(f"Showing {result['shown']} of {result['matches']} matches")
                for r in result["records"]:
                    print(f"[{r['reference_number']}] {r['citation_text']}")
                    print(f"  Article printed page {r['source_printed_page']}; extracted, not independently verified.\n")
        else:
            with args.file.open(encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                if not {"dimension", "state", "evidence_source"} <= set(reader.fieldnames or []):
                    raise ValueError("Worksheet requires dimension, state and evidence_source columns")
                rows = list(reader)
            counts = dict.fromkeys(STATES, 0)
            seen, missing = set(), []
            for row in rows:
                dimension = (row.get("dimension") or "").strip()
                state = (row.get("state") or "").strip() or "not_assessed"
                if not dimension or dimension in seen:
                    raise ValueError("Worksheet dimension names must be non-empty and unique")
                if state not in STATES:
                    raise ValueError(f"Invalid state for {dimension}; choose from {STATES}")
                seen.add(dimension)
                counts[state] += 1
                if state != "not_assessed" and not (row.get("evidence_source") or "").strip():
                    missing.append(dimension)
            result = {"instrument_status": "new_companion_unvalidated",
                      "rows": len(rows), "descriptive_state_counts": counts,
                      "assessed_entries_without_evidence_source": missing,
                      "interpretation": "Descriptive inventory only; no score or deployment verdict is calculated."}
            if args.json:
                print(json.dumps(result, indent=2, ensure_ascii=False))
            else:
                print(result["interpretation"])
                for state, count in counts.items():
                    print(f"{state}: {count}")
                if missing:
                    print("Evidence source missing for: " + ", ".join(missing))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
