# Alex's Notebook — Peer Review

## Week 06 · Tuesday · EDA Peer Review Lab

### Review objective

This review evaluates Alex's EDA notebook against the eight-point pre-submission checklist. The goal is to identify analysis, interpretation, visualization, and reporting issues before the work is treated as a finished analysis.

The dataset setup is correct and is reproduced without modification. The issues below concern the analysis built on top of the `learners` DataFrame.

---

# Part A — Structured Review

## Issue 1 — Course Track is mislabeled as a relationship

**Checklist item:** 1 — Distinguish a genuine relationship chart from a categorical comparison.

**Location:** Course Track chart, cells containing:

```python
order = learners.groupby("course_track")["completion_pct"].mean().sort_values(ascending=False).index
learners.boxplot(
    column="completion_pct",
    by="course_track",
    ax=ax,
    positions=range(len(order))
)
ax.set_title("Relationship Between Course Track and Completion")
```

**Problem:**

`course_track` is a categorical variable with three groups:

- Web Dev
- Data Science
- Design

`completion_pct` is a continuous variable.

Therefore, this chart compares the distribution of completion percentages across categories. It is not a relationship chart between two continuous variables.

**Evidence:**

The x-axis contains course-track categories while the y-axis contains completion percentage. The chart is therefore a group comparison.

**Shuffle-test justification:**

If the `course_track` labels were randomly shuffled among learners, the group assignments would be destroyed and the observed group differences would generally disappear. This indicates that the analysis is comparing categories rather than examining two continuously varying variables.

**Required correction:**

Rename the chart:

```text
Course Completion by Course Track
```

and describe the result as a **categorical comparison**, not a relationship.

**Correct wording:**

> Data Science learners have higher completion than Web Dev and Design learners in this sample.

---

## Issue 2 — Login-hours correlation is described but not quantified

**Checklist item:** 2 — Every correlation should be computed and reported as a number.

**Location:** `Login Hours and Completion` chart and Alex's note.

Alex's chart is:

```python
ax.scatter(
    learners["weekly_login_hours"],
    learners["completion_pct"],
    alpha=0.4
)
```

Alex then writes:

> "There's a strong, obvious upward relationship..."

**Problem:**

The scatterplot is appropriate for examining two numeric variables, but Alex does not calculate or report a correlation coefficient.

A visual impression such as "strong" is not enough when a correlation is being discussed.

**Fresh computation:**

The Pearson correlation is:

```text
r = 0.838
```

**Correct interpretation:**

> Weekly login hours and completion have a strong positive linear correlation (Pearson r = 0.838).

The numerical value should appear in the analysis rather than relying only on visual description.

---

## Issue 3 — Correlation is incorrectly presented as causation

**Checklist item:** 4 — Causal language must not be used without appropriate evidence.

**Location:** Alex's note under `Login Hours and Completion` and the Findings/Conclusion sections.

Alex writes:

> "There's a strong, obvious upward relationship — more login hours clearly causes higher completion."

and:

> "Platforms should push learners to log in more often to drive completion up."

The conclusion similarly states:

> "This analysis shows that increasing login frequency is the clearest lever for improving course completion..."

**Problem:**

The analysis is observational. A strong correlation does not establish that increasing login hours will cause completion to increase.

The Pearson correlation of `r = 0.838` establishes a strong positive association, but it does not establish the direction of causality.

**Plausible confound:**

Learner motivation could influence both variables:

```text
              Learner motivation
                 /         \
                ↓           ↓
       More login hours   Higher completion
```

A highly motivated learner may log in more and also be more likely to finish the course.

**Required correction:**

Replace causal language such as:

- causes
- drive
- increasing ... improves
- lever for improving

with appropriately scoped correlational language.

**Correct wording:**

> Weekly login hours are strongly positively correlated with completion (Pearson r = 0.838), but this observational analysis does not establish causation. Learner motivation is a plausible confound that could influence both login activity and completion.

---

## Issue 4 — Forum-post result is omitted from the findings

**Checklist item:** 3 — Every chart result, including a null result, should appear in the written findings.

**Location:** `Forum Activity` chart.

Alex creates:

```python
ax.scatter(
    learners["forum_posts"],
    learners["completion_pct"],
    alpha=0.4
)
```

but provides no written interpretation before moving to the Findings section.

**Problem:**

The chart represents a separate analysis question, but its result is completely absent from the written findings.

This is particularly important because the result is essentially null. A null result is still a result and should not be omitted simply because it is less interesting than the other findings.

**Fresh computation:**

The Pearson correlation is:

```text
r = 0.039
```

**Correct interpretation:**

> Forum-post count has essentially no linear correlation with course completion (Pearson r = 0.039).

This finding should be explicitly included in the Findings section.

---

## Issue 5 — Course-track ordering is based on the result rather than a deliberate fixed order

**Checklist item:** 5 — Category ordering should be deliberate and justified.

**Location:**

```python
order = learners.groupby("course_track")["completion_pct"].mean().sort_values(ascending=False).index
```

**Problem:**

Alex sorts the categories according to their observed completion means.

This means the category order is determined by the result of the analysis rather than by a stable, deliberate ordering.

The current order is approximately:

```text
Data Science
Design
Web Dev
```

If the underlying data changes, the order can also change.

This makes it harder to consistently locate a category such as `Design` across different versions of the chart.

There is also a technical concern: the calculated `order` is passed only to `positions`; it does not explicitly reorder the category data itself. Therefore, the intended category order is not robustly established by the code.

**Required correction:**

Define an explicit fixed order:

```python
track_order = [
    "Web Dev",
    "Data Science",
    "Design"
]
```

Then explicitly apply that order to the visualization.

**Correct principle:**

The ordering should be chosen because it is meaningful and stable, not because it makes the observed result appear ranked.

---

## Issue 6 — Color choice is not deliberate and the defined colors are not actually used

**Checklist item:** 5 — Colors should be deliberate and justified.

**Location:**

```python
colors = {
    "Data Science": "green",
    "Design": "yellow",
    "Web Dev": "red"
}
```

**Problem:**

Alex defines three colors, but the `colors` variable is never passed into the boxplot.

Therefore, the intended colors do not actually control the chart.

Additionally, assigning arbitrary colors such as red, yellow, and green could unintentionally imply a qualitative judgment such as bad/warning/good when no such meaning exists in the analysis.

**Required correction:**

Use a single deliberate color for the boxplot, or use a multi-color scheme only if each color has a clearly justified meaning.

For this analysis, a single color is preferable because the purpose is simply to compare the distributions across tracks.

**Correct principle:**

> Color should communicate information or remain neutral; it should not introduce an unsupported interpretation.

---

## Issue 7 — Histogram annotation/layout needs visual QA

**Checklist item:** 6 — Saved charts must be opened and checked for layout problems.

**Location:** `Distribution of Weekly Login Hours`.

Alex uses:

```python
ax.annotate(
    f"mean = {learners['weekly_login_hours'].mean():.1f}\nmedian = {learners['weekly_login_hours'].median():.1f}",
    xy=(0.98, 0.95),
    xycoords="axes fraction",
    ha="right",
    va="top",
    fontsize=11,
)
```

**Problem:**

At the specified figure size, the annotation is positioned very close to the upper-right of the axes and overlaps the title/layout when the saved PNG is inspected.

The important issue is not whether the Python code executes successfully. The saved chart itself must be visually inspected.

**Required correction:**

Move the annotation lower within the axes and apply a layout adjustment:

```python
xy=(0.98, 0.82)
```

and:

```python
fig.tight_layout()
```

The resulting PNG should then be opened and visually checked to confirm that the title, annotation, axes, and plot area do not overlap.

**Correct principle:**

> A chart is not considered finished merely because the plotting code runs without an error. The actual saved image must be inspected.

---

## Issue 8 — The reported overall mean is incorrect

**Checklist item:** 7 — Written numbers must match a fresh computation.

**Location:** Findings item #3.

Alex writes:

> "The average completion rate across all learners is approximately 74%."

**Problem:**

A fresh computation of:

```python
learners["completion_pct"].mean()
```

gives:

```text
71.16%
```

or approximately:

```text
71.2%
```

Therefore, Alex's stated value of approximately 74% does not match the dataset.

**Correct wording:**

> The overall mean completion percentage is 71.16% (approximately 71.2%).

The original `~74%` claim should be removed.

---

## Issue 9 — Course-track difference needs statistical uncertainty

**Checklist item:** 8 — A claimed group difference should have statistical backing rather than relying only on a visual impression.

**Location:** Findings item #2 and the course-track boxplot.

Alex writes:

> "Data Science learners have noticeably higher completion than the other two tracks."

**Problem:**

The boxplot provides useful descriptive evidence, but the statement that the difference is meaningful should be supported with uncertainty rather than relying only on visual separation.

The relevant means are:

| Course Track | Mean Completion |
|---|---:|
| Web Dev | 66.96% |
| Data Science | 76.78% |
| Design | 70.69% |

The observed Data Science − Web Dev difference is:

```text
9.82 percentage points
```

**Bootstrap analysis:**

A bootstrap 95% confidence interval for the Data Science − Web Dev completion gap is approximately:

```text
6.39 to 13.25 percentage points
```

**Interpretation:**

Zero is not included in this confidence interval.

Therefore, the bootstrap result supports the existence of a difference between the Data Science and Web Dev groups in this sample.

**Correct wording:**

> Data Science learners have an observed mean completion rate 9.82 percentage points higher than Web Dev learners. A bootstrap 95% confidence interval for this gap is approximately 6.39–13.25 percentage points, which excludes zero and supports a difference between the groups in this sample.

This should still not be interpreted as evidence that being enrolled in the Data Science track causes higher completion.

---

# Numerical Audit Summary

The following values were independently recomputed from the `learners` DataFrame:

| Metric | Verified Result |
|---|---:|
| Overall mean completion | **71.16%** |
| Pearson r: Login Hours vs Completion | **0.838** |
| Pearson r: Forum Posts vs Completion | **0.039** |
| Web Dev mean completion | **66.96%** |
| Data Science mean completion | **76.78%** |
| Design mean completion | **70.69%** |
| Data Science − Web Dev gap | **9.82 percentage points** |
| Bootstrap 95% CI | **6.39 to 13.25 percentage points** |
| Does CI include zero? | **No** |

---

# Review Checklist Coverage

| Checklist | Result | Main Issue |
|---|---|---|
| 1. Relationship vs comparison | ❌ | Course Track is a categorical comparison |
| 2. Correlation reported numerically | ❌ | Login-hours correlation was not reported |
| 3. Every result reported | ❌ | Forum-post result was omitted |
| 4. Causal language controlled | ❌ | Login hours incorrectly described as causing completion |
| 5. Colors/order deliberate | ❌ | Track order is result-based and colors are unused/arbitrary |
| 6. Saved charts visually checked | ❌ | Histogram annotation/layout needs correction |
| 7. Numbers independently verified | ❌ | 74% claim is incorrect; actual mean is 71.16% |
| 8. Comparison statistically supported | ❌ | Data Science vs Web Dev needs uncertainty; bootstrap CI added |

---

# Part C — Reviewer's Note

The original analysis has a good foundation: the scatterplots are appropriate for examining the relationships between the numeric variables, and the course-track comparison is a useful question to investigate. The highest-priority issue is the causal language around login hours, because the observational correlation does not establish that increasing login frequency will cause higher completion. The numerical audit also identified an incorrect overall mean and a missing null result for forum activity, while the course-track comparison needs deliberate ordering and statistical uncertainty. After these corrections, the analysis will communicate its evidence much more accurately and defensibly.