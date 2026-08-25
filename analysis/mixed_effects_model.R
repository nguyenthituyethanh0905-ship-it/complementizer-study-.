# Reproduces the illustrative mixed-effects logistic regression reported
# in Section 4 (glmer, lme4; Bates et al., 2015):
#   complementizer_present ~ clause_length + verb_log_freq + subject_continuity
#     + (1 | matrix_verb)
# on N = 15,285 tokens (excluding tokens with indeterminate subjects).
#
# Expects a CSV with columns:
#   complementizer_present (0/1), clause_length, verb_log_freq,
#   subject_continuity, matrix_verb, subject_indeterminate (0/1)

library(lme4)

args <- commandArgs(trailingOnly = TRUE)
input_path <- if (length(args) >= 1) args[[1]] else "output/model_input.csv"

d <- read.csv(input_path)
d <- d[d$subject_indeterminate == 0, ]

# Standardize continuous predictors so coefficients are "per SD", matching
# the paper's reporting (OR = 1.30 per SD for clause length, etc.)
d$clause_length_z <- scale(d$clause_length)
d$verb_log_freq_z <- scale(d$verb_log_freq)

model <- glmer(
  complementizer_present ~ clause_length_z + verb_log_freq_z + subject_continuity + (1 | matrix_verb),
  data = d,
  family = binomial
)

print(summary(model))
cat("\nOdds ratios:\n")
print(exp(fixef(model)))
