# Evaluation Report — Loan Default Classification

## The task

Predict whether a loan applicant will default, using four pieces of information available at
application time: credit score, income, requested loan amount, and employment type. 1,200
applicants, 60% of whom defaulted — "will default" is the majority class here, which matters for
how accuracy should be read below. Credit score was missing for 90 applicants; the first real
decision in this pipeline was filling those gaps without letting test-set information leak into
that decision.

## The baseline

A dummy classifier that always predicts "will default" scores:

- Accuracy: 0.600
- Precision: 0.600
- Recall: 1.000
- F1: 0.750
- ROC-AUC: 0.500

The recall of 1.0 is not a real signal — it's free from always guessing the bigger class. ROC-AUC
of exactly 0.5 is the honest number: zero ability to tell defaulters from non-defaulters, which is
what a baseline should show.

## Model comparison

Logistic regression's `C` and the tree/forest's depth and leaf size were tuned with 5-fold
`GridSearchCV` on F1; the tree and forest were also fit with `class_weight="balanced"`.

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| Baseline | 0.600 | 0.600 | 1.000 | 0.750 | 0.500 |
| Logistic Regression (C=0.1) | 0.742 | 0.766 | 0.819 | 0.792 | 0.844 |
| Decision Tree (depth=4, leaf=10) | 0.713 | 0.826 | 0.660 | 0.734 | 0.819 |
| Random Forest (200 trees, depth=4, leaf=5) | 0.758 | 0.821 | 0.764 | 0.791 | 0.854 |

All three real models clear the baseline's ROC-AUC by a wide margin (0.82–0.85 vs. 0.50). Within
the three, there's a genuine trade-off rather than one model winning outright: the random forest
has the best ROC-AUC and precision, but logistic regression has meaningfully higher recall (0.819
vs. 0.764) — a 5.5-point gap that isn't noise. The decision tree is the weakest on recall and F1
despite class-balancing, and its higher precision comes at the cost of missing more actual
defaulters.

## Final model: Logistic Regression

The automatic ranking (by F1, then recall, then ROC-AUC) already lands on logistic regression, by
the narrowest possible margin on F1 (0.7919 vs. random forest's 0.7914). But the more important
reason to prefer it here is recall: for a loan-default decision, missing an actual defaulter is
more costly than the reverse (see defense Q3), and logistic regression catches 82% of defaulters
in the test set against the random forest's 76%. It also comes with directly interpretable
coefficients — "credit score costs you this much, loan-to-income costs you this much" — which the
forest cannot offer despite its structurally better ROC-AUC. If ROC-AUC (overall ranking ability)
were the priority instead of recall, the random forest would be the defensible pick; that trade-off
is spelled out fully in the defense.

## Error analysis

62 of 240 test applicants were misclassified (25.8%): 26 false negatives (missed actual defaulters)
and 36 false positives (flagged applicants who didn't actually default).

- **Loan-to-income ratio** was higher on average among misclassified applicants (0.365) than among
  correctly classified ones (0.325).
- **Self-employed applicants** were over-represented among the errors (35.5% of misclassifications)
  relative to their share of the test set (28.3%); salaried applicants were correspondingly
  under-represented (45.2% of errors vs. 50.0% of the test set).
- **The false negatives and false positives fail in opposite, informative directions.** Missed
  defaulters (false negatives) had a noticeably *higher* average credit score than the test-set
  average (692.7 vs. 648.7) — these are applicants who looked safe on paper but defaulted anyway.
  False positives, by contrast, had an average credit score right at the test-set mean (648.4) but
  a higher loan amount (17,055 vs. 15,711) and lower income (52,577 vs. 55,896) — a higher
  loan-to-income ratio pushing the model to over-predict risk for people who ultimately repaid.

Both patterns track the underlying data-generating process: self-employment and loan-to-income
ratio both nudge true default probability without a hard cutoff, and credit score alone can't
explain away noise from those other factors — so the model's blind spot is exactly where those
influences pull in different directions from what the credit score alone would suggest.

## Calibration

The calibration curve for logistic regression tracks the diagonal reasonably well at the extremes
(low predicted-probability bins under-predict slightly less than 0.2 off the diagonal; high bins
near 0.9–1.0 sit almost exactly on it), but it is not monotonic through the middle: the bin around
0.71 predicted probability shows an *observed* default rate of only 0.46 — lower than the
neighboring 0.62-predicted bin's observed rate of 0.58. That's the model being locally
overconfident in that band. With test-set bins built from only ~24 applicants each, some of this
non-monotonicity is expected sampling noise rather than a systematic flaw, but it means the
probabilities in that middle band shouldn't be read too literally.

## Limitation

This model has no information about an applicant's existing debt load or payment history beyond a
single credit-score snapshot. Two applicants with identical credit score, income, and loan amount
get identical risk scores here even if one is carrying several other loans and the other has none.
Real underwriting would need that fuller financial picture before this model's output should
influence an actual lending decision.
