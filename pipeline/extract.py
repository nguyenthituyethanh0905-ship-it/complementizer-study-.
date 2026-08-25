"""
Extraction step described in Section 2.2 of the paper.

This is a SCAFFOLD, not a working implementation: paste in your actual
matching/detection logic below so that the released code matches exactly
what produced the reported baseline (18,929 tokens before deduplication).
Do not publish a "cleaned up" reimplementation that behaves differently
from what generated the numbers in the paper -- reviewers and future users
should be able to reproduce Table 1 from this code as-is.

Expected pipeline, per Section 2.2:
  1. Parse the English sentence with spaCy (en_core_web_sm).
  2. Flag a matrix-verb hit: a token is a candidate if a dependent carries
     the `ccomp` relation.
  3. Flag English complementizer presence: True if that ccomp child has a
     `mark` child with lemma "that".
  4. Look up the matrix verb in lexicon.csv and check the aligned
     Vietnamese sentence for a lexicon match.
  5. Apply the asymmetric rằng/là detection rule (Section 2.1-2.2):
       - "rằng": present if it occurs within 4 words of the matched verb
         (tolerating a short intervening oblique/dative phrase).
       - "là": present only if it occurs immediately following the verb.
     Lexicon entries that are themselves fixed verb+complementizer
     collocations (e.g. "cho rằng") are coded complementizer-present by
     construction.
  6. Exclude pairs lacking a matched verb, or with fewer than two
     remaining words after it.

Output columns should match what analysis/table1.py expects:
  matrix_verb, en_sentence, vi_sentence, en_that_present, vi_complementizer_present
"""
import argparse
import csv


def load_lexicon(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def extract(input_path, lexicon_path, output_path):
    lexicon = load_lexicon(lexicon_path)  # noqa: F841

    # TODO: paste your actual spaCy-based extraction logic here.
    raise NotImplementedError(
        "Replace this with the extraction logic that produced the "
        "18,929 tokens reported in Section 4 before deduplication."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="PhoMT-format aligned English-Vietnamese file")
    parser.add_argument("--lexicon", required=True, default="lexicon/lexicon.csv")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    extract(args.input, args.lexicon, args.out)
