"""
Reproduces Table 1 (Section 4): complementizer/that presence by matrix
verb and language, from the deduplicated extraction output.

Usage:
    python analysis/table1.py --input output/extracted_train_dedup.csv
"""
import argparse
import csv
from collections import defaultdict

VERB_ORDER = ["think", "know", "say", "believe", "feel",
              "hope", "claim", "argue", "admit", "realize"]


def to_bool(v):
    return str(v).strip().lower() in {"1", "true", "yes", "y"}


def table1(input_path):
    counts = defaultdict(lambda: {"n": 0, "vi_present": 0, "en_present": 0})
    with open(input_path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            verb = row["matrix_verb"]
            counts[verb]["n"] += 1
            counts[verb]["vi_present"] += to_bool(row["vi_complementizer_present"])
            counts[verb]["en_present"] += to_bool(row["en_that_present"])

    total_n = total_vi = total_en = 0
    print(f"{'verb':10} {'N':>7} {'VN comp. %':>12} {'EN that %':>10}")
    for verb in VERB_ORDER:
        c = counts.get(verb, {"n": 0, "vi_present": 0, "en_present": 0})
        n = c["n"]
        vi_pct = 100 * c["vi_present"] / n if n else 0.0
        en_pct = 100 * c["en_present"] / n if n else 0.0
        print(f"{verb:10} {n:>7} {vi_pct:>11.1f}% {en_pct:>9.1f}%")
        total_n += n
        total_vi += c["vi_present"]
        total_en += c["en_present"]

    print("-" * 44)
    print(f"{'Overall':10} {total_n:>7} "
          f"{100 * total_vi / total_n:>11.1f}% {100 * total_en / total_n:>9.1f}%")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    table1(args.input)
