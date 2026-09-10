# Defense Answers

**1. Your random forest's accuracy is probably close to, or below, your logistic regression's.
Does that mean logistic regression should always be the answer for a problem shaped like this?
Defend your actual final model choice.**

In this run the random forest is actually *ahead* on accuracy (0.758 vs. 0.742), precision (0.821
vs. 0.766), and ROC-AUC (0.854 vs. 0.844) — so "logistic regression wins on the numbers" isn't even
the true story here. What decides it is recall: logistic regression catches 81.9% of actual
defaulters in the test set, the random forest only 76.4%. For a lending decision, a missed
defaulter (a loan that gets funded and then isn't repaid) is a direct financial loss in a way a
wrongly-denied safe applicant is not (see Q3). So the choice isn't "simpler model because its
numbers happened to win" — it's "the model with the better recall on the class that's expensive to
miss, which also happens to be interpretable." If the priority were overall ranking quality
(ROC-AUC) rather than catching defaulters specifically, the random forest would be the defensible
pick instead — that's a genuine, close trade-off here, not a landslide either way.

**2. A colleague suggests computing the credit_score fill value from the entire dataset before
splitting, since "it's just imputation, not modeling." Explain specifically why that's wrong, using
your own train-only vs. full-dataset numbers.**

In this run the train-only median (649.0) and the full-dataset median (650.0) are one point apart —
close enough that it's tempting to call the difference meaningless. But that's exactly the trap:
computing the fill value on the full dataset means the value used to fill *test-set* rows was
partly derived from those same test-set rows' own (other) credit scores. It's a small leak here
because the median is a stable statistic and only 90 of 1,200 rows were missing, fairly evenly
distributed. A different imputation choice — a group-wise mean by employment type, a
model-based imputer, or simply a smaller or more skewed dataset — could turn that same "it's just
imputation" shortcut into a fill value that meaningfully shifts predictions for the applicants who
actually had missing scores. The rule doesn't change because the leak happened to be small this
time: compute the statistic only from what the model is allowed to see at train time.

**3. For a loan-default decision, is overall accuracy or recall on the "will default" class more
important? Defend your answer, and explain what goes wrong in practice if you optimized for the
wrong one.**

Recall on the default class matters more, and the baseline demonstrates exactly why relying on
accuracy is dangerous: it reaches 0.600 accuracy and a *perfect* 1.0 recall on the default class
simply by predicting "will default" for everyone, while being useless as a decision tool (ROC-AUC
0.500, precision only 0.600). That shows recall in isolation isn't the fix either — but between
the two, optimizing purely for accuracy is the costlier mistake: a model can raise accuracy by
leaning on the majority class and quietly missing borderline defaulters, and each one it misses (a
false negative) becomes a loan that's funded and then not repaid — an unrecoverable loss. The
decision tree in this comparison illustrates the failure mode directly: it has the highest
precision of the three (0.826) but the lowest recall (0.660) — it's "confident" about the
defaulters it flags but silently lets more of them through than either other model, which is the
wrong trade for this decision even though its accuracy (0.713) looks respectable next to logistic
regression's (0.742).

**4. Walk through your calibration curve — would you trust this model's predicted probabilities
directly to set a risk-based interest rate? Why or why not?**

Not directly, not yet. The curve tracks the diagonal reasonably closely at the low end (around 0.08
predicted probability, applicants defaulted about 12% of the time — close) and the high end (0.9+
predicted bins cluster near an observed rate of 1.0), but it's not monotonic through the middle:
the bin centered near 0.71 predicted probability shows an observed default rate of only 0.46 —
*lower* than the neighboring 0.62-predicted bin's observed rate of 0.58. That's the model being
locally overconfident in that band, and it's not a small gap — it's the difference between the
model claiming "more likely than not to default" and that group actually defaulting less than half
the time. With roughly 24 test applicants per bin, some of that is sampling noise, but it's exactly
the kind of noise that would produce inconsistent, hard-to-justify interest rates if applied
directly. I'd want calibration re-checked on a much larger holdout, and likely a calibration
wrapper (Platt scaling or isotonic regression) fit on that larger holdout, before using these
specific probability values — rather than just the model's relative ranking of applicants — to set
a price.

**5. Name one real-world factor this pipeline doesn't have that you'd want before this model made
actual lending decisions, and explain concretely why its absence should limit how much the model is
trusted.**

Existing debt load / current payment history is missing entirely. The error analysis makes the cost
of that concrete: the applicants this model missed (false negatives, the actual defaulters it
cleared) had a *higher* average credit score than the test set overall (692.7 vs. 648.7) — they
looked safe by the one signal this model has, and defaulted anyway. A debt-to-income ratio or a
record of recent missed payments elsewhere is exactly the kind of feature that could catch an
applicant who looks good on a single lagging credit-score snapshot but is already overextended
elsewhere. Without it, this model will systematically underestimate risk for anyone whose financial
situation has changed more recently than their credit score reflects — which is precisely the
pattern showing up in its worst errors, and why this pipeline should inform, not replace, an
underwriting process with access to that fuller picture.
