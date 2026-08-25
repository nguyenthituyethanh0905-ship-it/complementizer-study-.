# Treebank validation (Section 2.1)

Manual check of *rằng* and *là* usage against
[UD_Vietnamese-VTB](https://github.com/UniversalDependencies/UD_Vietnamese-VTB)
(Nguyen et al., 2009; 3,323 sentences), motivating the asymmetric detection
rule in Section 2.2.

| Form | Total occurrences | Complementizer use | % complementizer |
|---|---:|---:|---:|
| rằng | 33 | 28 | 84.8% |
| là | 595 | 40 | 6.7% |

TODO: paste in the actual annotated sentence list / script used to derive
these counts (e.g., a CoNLL-U query plus manual check) so the check is
auditable, the same way `sample_data/reliability_check_n50.csv` documents
the Section 3 reliability check.

## Illustrative examples cited in the paper

- (i) *Hùng cho rằng đây là chuyện bình thường* ("Hùng thought this was a
  normal matter") — rằng introduces a clause that itself contains the
  copula là.
- (ii) *Vy cười thật tươi khi biết chúng tôi là người VN* ("Vy smiled
  brightly when she found out we were Vietnamese") — là functions only as
  a copula linking the embedded subject to its predicate nominal, not as a
  complementizer.
