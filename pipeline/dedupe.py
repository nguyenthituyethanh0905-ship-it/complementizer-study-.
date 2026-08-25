"""
Deduplication step described in Section 4.

"Exact duplicate" = extracted (English matrix-clause, Vietnamese-clause)
pairs identical after whitespace normalization. Applying this to the raw
18,929 extracted tokens should remove 974 (5.1%) duplicates, leaving
17,955 (16,348 training, 878 test, 729 development) -- these exact counts
are a useful self-check that this script matches what was actually run.
"""
import argparse
import csv
import re


def normalize_whitespace(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def dedupe(input_path, output_path):
    with open(input_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    seen = set()
    kept = []
    for row in rows:
        key = (
            normalize_whitespace(row["en_sentence"]),
            normalize_whitespace(row["vi_sentence"]),
        )
        if key in seen:
            continue
        seen.add(key)
        kept.append(row)

    removed = len(rows) - len(kept)
    print(f"{len(rows)} tokens before dedup; removed {removed} "
          f"({removed / len(rows):.1%}); {len(kept)} remain.")

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(kept)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    dedupe(args.input, args.out)
