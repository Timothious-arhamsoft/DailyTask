# Evaluation Report — Week 6 Thu: Iterate, Diagnose, Defend
*Students exam-score dataset — regression & distinction classification*

**Task.** Predict `exam_score` (regression) and whether a student earns a `distinction`
(`exam_score ≥ 85`, classification) from `study_hours_per_week`, `sleep_hours_per_night`,
`attendance_pct`, and `class_section`, on a synthetic 600-student dataset.

**Baseline.** A `DummyRegressor` predicting the training-set mean (test RMSE 10.30, R² ≈ 0), and a
`DummyClassifier` predicting the majority class (Accuracy 0.650, F1 0.788 — inflated by 100% recall
on a class that makes up 65% of the test set).

**Models compared.** Regression: baseline, Linear Regression, an unconstrained Decision Tree, a
depth-3 Decision Tree, and a 200-tree Random Forest. Classification: baseline, Logistic Regression,
a depth-3 Decision Tree, and a 200-tree Random Forest.

**Metrics table.**

| Regression model | Test RMSE | Test R² |
|---|---|---|
| Linear Regression | **7.058** | **0.526** |
| Tree (max_depth=3) | 7.103 | 0.520 |
| Random Forest | 7.401 | 0.479 |
| Tree (unconstrained) | 9.840 | 0.078 |
| Dummy Baseline | 10.298 | −0.010 |

| Classification model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Tree (max_depth=3) | 0.742 | 0.724 | **0.974** | **0.831** |
| Logistic Regression | **0.767** | **0.813** | 0.833 | 0.823 |
| Random Forest | 0.725 | 0.771 | 0.821 | 0.795 |
| Dummy Baseline | 0.650 | 0.650 | 1.000 | 0.788 |

**Chosen final model and why.** For regression, **Linear Regression** is the model I'd ship: it has
the lowest test RMSE (7.06) and highest R² (0.526) of every model tried, including the random
forest and both decision trees. Neither extra complexity helped here — the unconstrained tree
overfit badly (train RMSE 0.00 vs test RMSE 9.84), and even the well-tuned forest and depth-3 tree
couldn't beat plain least squares, most likely because `exam_score` was generated as a roughly
linear function of the features, so linear regression is already close to the correct hypothesis
class. For classification, I'd ship **Logistic Regression** over the depth-3 tree despite the
tree's marginally higher F1 (0.831 vs 0.823): the tree's F1 is inflated by very high recall (0.974)
paired with the lowest precision of the three real models (0.724), meaning it over-predicts
"distinction" and would flag many false positives in practice. Logistic Regression has the best
accuracy (0.767) and a much more balanced precision/recall trade-off, which matters more than F1
alone for a decision that's likely to be acted on.

**Error-analysis finding.** For Linear Regression, the five worst-predicted rows (residuals of
16–19 exam points) don't share an obvious extreme feature value — their study hours (7–14) and
attendance (69–88%) sit inside the normal range for the test set. What they do share is being
outliers *relative to the linear trend*: e.g. a student with only 6.8 study hours and 87% attendance
who actually scored 98.4 (predicted 80.9), and one with 8.9 study hours and 75% attendance who
actually scored only 65.3 (predicted 84.1). This is the residual noise the data-generating process
built in (`+ noise` in the simulation) — essentially irreducible error a linear model can't capture,
not a systematic blind spot in a particular section. For Logistic Regression, 28 of 120 test rows
(23%) were misclassified, and their average study hours (8.75) sits noticeably below the full test
set's average (9.82, close to the decision boundary around the 85-point distinction cutoff) —
consistent with the classifier's errors clustering near the threshold rather than being random
across the whole range.

**Calibration finding.** The calibration curve for Logistic Regression stays reasonably close to
the diagonal across most probability bins, but its worst gap (0.18) is in the bin centered near a
predicted probability of ≈24% — there the model is actually right about 42% of the time, meaning
it's noticeably **underconfident** for borderline-low-probability students. A "70% confident"
prediction from this model is fairly trustworthy; a "20–25% confident" prediction should be treated
as less certain than the number suggests.
