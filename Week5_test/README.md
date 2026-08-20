# Week 05 · Thursday Review — Full EDA Pipeline

## Overview

This project is the Week 05 Thursday Review assignment focused on building a complete
**Exploratory Data Analysis (EDA) pipeline** on a synthetic orders dataset.

The analysis follows the complete workflow:

**Dataset Generation → Initial Confirmation → Diagnosis → Cleaning → Cleaning Verification → Visualization → Findings → Technical Summary**

The dataset intentionally contains several data-quality problems. The purpose of the
assignment is to identify these problems independently, make justified cleaning
decisions, verify the results, and communicate the findings clearly.

---

## Project Files

```text
.
├── eda_pipeline.ipynb
├── orders_cleaned.csv
├── orders_raw.csv
├── requirements.txt
├── technical_summary.md
└── README.md
```

### `eda_pipeline.ipynb`

The main Jupyter Notebook containing the complete EDA process:

1. Dataset Generation
2. Initial Confirmation
3. Diagnosis
4. Cleaning
5. Cleaning Verification
6. Visualization
7. Findings
8. Technical Summary

### `orders_raw.csv`

A CSV export of the original dataset before cleaning. It preserves the raw data and
the intentionally introduced data-quality problems.

### `orders_cleaned.csv`

A CSV export of the dataset after the documented cleaning operations have been applied.

### `technical_summary.md`

A short standalone technical summary describing the dataset, major findings, cleaning
decisions, and limitations of the analysis.

### `requirements.txt`

Contains the Python dependencies required to run the notebook.

---

## Dataset

The dataset represents synthetic order records containing information such as:

- Order ID
- Order date
- Customer ID
- Product category
- Quantity
- Unit price
- Region

The dataset was generated using the exact specification provided in the assignment
with a fixed random seed.

The raw dataset intentionally contains several data-quality issues, including:

- Missing customer IDs
- Missing regions
- Inconsistent product-category capitalization
- Negative quantities representing returns
- Implausible unit-price values
- Duplicate records

Additional data-quality issues were also investigated during diagnosis.

---

## EDA Workflow

### 1. Dataset Generation

The required synthetic orders dataset is generated using NumPy and Pandas.

### 2. Initial Confirmation

The dataset shape and first few records are checked to confirm that the required
dataset was generated correctly.

### 3. Diagnosis

The raw dataset is inspected before any cleaning is performed using:

- `.head()`
- `.info()`
- `.describe()`
- `.isna().sum()`
- `.value_counts()`
- Additional targeted checks

The purpose is to identify and document every relevant data-quality problem.

### 4. Cleaning

Each identified problem is handled separately rather than applying one blanket
cleaning operation.

Cleaning decisions are documented and justified according to the meaning of each
column and the characteristics of the problem.

### 5. Cleaning Verification

The cleaned dataset is checked again to confirm that the identified problems have
been addressed.

### 6. Visualization

Matplotlib is used to explore the cleaned dataset through charts representing:

- A distribution
- A category comparison
- A relationship between numerical variables

The visualizations use the `fig, ax = plt.subplots()` approach.

### 7. Findings

The main findings are written as complete sentences and supported by specific
statistics or visual evidence from the analysis.

### 8. Technical Summary

A separate summary communicates the main results and limitations for a
non-technical reader.

---

## Installation

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Notebook

Start Jupyter:

```bash
jupyter notebook
```

Open:

```text
eda_pipeline.ipynb
```

Run the notebook from beginning to end.

Before submitting, use:

**Kernel → Restart Kernel and Run All**

to confirm that the notebook runs successfully without relying on previously stored
variables or execution state.

---

## Reproducibility

The dataset generation uses a fixed random seed, making the analysis reproducible.

The raw and cleaned datasets are also included in the repository so that the
transformation from the original data to the cleaned data can be inspected.

---


## Technologies

- Python
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook

---

## Learning Outcomes

This assignment demonstrates the ability to:

- Perform an end-to-end EDA workflow
- Diagnose data-quality problems before modifying data
- Identify problems beyond missing values
- Make and justify column-specific cleaning decisions
- Verify that cleaning operations were successful
- Select appropriate visualizations for analytical questions
- Support findings with numerical and visual evidence
- Communicate technical results clearly
- Follow a structured Git workflow
