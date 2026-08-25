# Rằng/Là Complementizer Extraction Pipeline

Extraction and annotation pipeline for detecting Vietnamese complementizer
(*rằng* / *là*) presence in aligned English–Vietnamese sentence pairs from
[PhoMT](https://github.com/VinAIResearch/PhoMT) (Doan et al., 2021).

Companion code and lexicon for the short paper *"An extraction and
annotation pipeline for Vietnamese complementizer optionality (rằng/là) in
parallel corpora: methodology and a descriptive baseline,"* submitted to the
*International Journal of Corpus Linguistics*.

> **Status:** this repository accompanies a manuscript currently under
> anonymous peer review. Identifying information (author names, affiliation,
> acknowledgements) has been withheld — see [`ANONYMOUS_REVIEW.md`](ANONYMOUS_REVIEW.md).

## What this repository contains

| Folder | Contents |
|---|---|
| `pipeline/` | English parsing (spaCy `ccomp`/`mark` detection), Vietnamese lexicon matching, the *rằng*/*là* proximity rule, deduplication |
| `lexicon/` | The ten-verb English→Vietnamese matrix-verb lexicon (`lexicon.csv`) used for alignment matching |
| `sample_data/` | A small sample of coded (English, Vietnamese, label) triples for inspecting the output format and for the manual-review reliability check — **not** the full 17,955-token dataset (see *Data availability* below) |
| `analysis/` | Scripts to reproduce Table 1 and the illustrative `glmer` mixed-effects model reported in Section 4 |
| `docs/` | Treebank validation notes (UD_Vietnamese-VTB check reported in Section 2.1) |

## What this repository does *not* contain

The full 17,955-token extracted dataset is **not** redistributed here,
because it is derived from PhoMT sentence pairs under PhoMT's own release
terms. To reproduce it: download PhoMT yourself, then run the pipeline
against it (see *Reproducing the dataset* below).

## Requirements

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

R (≥ 4.0) with `lme4` is needed only for `analysis/mixed_effects_model.R`.

## Reproducing the dataset

1. Download PhoMT from the [official release](https://github.com/VinAIResearch/PhoMT) and place the training/dev/test files under `data/phomt/` (not tracked by this repo).
2. Run the extraction step:
   ```bash
   python pipeline/extract.py --input data/phomt/train.envi --lexicon lexicon/lexicon.csv --out output/extracted_train.csv
   ```
3. Run deduplication:
   ```bash
   python pipeline/dedupe.py --input output/extracted_train.csv --out output/extracted_train_dedup.csv
   ```
4. Reproduce Table 1:
   ```bash
   python analysis/table1.py --input output/extracted_train_dedup.csv
   ```

Random sampling of the 40,000-pair working subset (Section 2.1) did **not**
use a fixed seed in the version reported in the paper; running `extract.py`
against the full training set reproduces the full 309,910-pair eligible
pool deterministically, but the specific 40,000-pair draw will differ
unless you use the `sample_ids.txt` file included under `sample_data/` (the
actual IDs used for the reported baseline).

## Treebank validation (Section 2.1)

`docs/treebank_check.md` documents the manual check of *rằng* (28/33
complementizer uses) and *là* (40/595) against UD_Vietnamese-VTB, and the
asymmetric detection rule it motivates.

## Reliability check (Section 3)

`sample_data/reliability_check_n50.csv` contains the final N = 50 subsample
used for the reported 98% automated-vs-manual agreement figure, with both
codings included, so the check is auditable.

## Citation

See [`CITATION.cff`](CITATION.cff). Please also cite PhoMT (Doan et al.,
2021) when using data derived from it.

## License

Code: MIT (see [`LICENSE`](LICENSE)). The included lexicon and sample data
are released under CC-BY-4.0. This does **not** cover PhoMT itself — consult
PhoMT's own license for any data derived from it.
