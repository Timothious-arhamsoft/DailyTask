# test_friday_sample.py — run with: python -m pytest test_friday_sample.py
"""
Sample self-check for Week 06 assessment.

Includes the brief's structural checks plus extra invariants that catch common
submission mistakes (wrong paths, bad baseline, full-data imputation leak,
empty docs, non-PNG charts). Hyperparameter choices are intentionally not locked.

Tip: run via the project venv so numpy/sklearn resolve correctly:
    python -m pytest test_friday_sample.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

REQUIRED_MODELS = {"baseline", "logistic_regression", "decision_tree", "random_forest"}
REQUIRED_METRIC_KEYS = {"accuracy", "precision", "recall", "f1", "roc_auc"}
REAL_MODELS = REQUIRED_MODELS - {"baseline"}

ROOT = Path(__file__).resolve().parent

BASELINE_EXPECTED = {
    "accuracy": 0.6,
    "precision": 0.6,
    "recall": 1.0,
    "f1": 0.75,
    "roc_auc": 0.5,
}


@pytest.fixture(scope="module")
def metrics():
    path = ROOT / "model_metrics.json"
    assert path.exists(), "model_metrics.json must live next to this test file (project root)"
    data = json.loads(path.read_text())
    return data


def _build_split_frame():
    """Rebuild the exact assessment dataset + train/test split (no modeling)."""
    np = pytest.importorskip("numpy")
    pd = pytest.importorskip("pandas")
    train_test_split = pytest.importorskip("sklearn.model_selection").train_test_split

    rng = np.random.default_rng(seed=55)
    n = 1200

    employment_type = rng.choice(
        ["Salaried", "Self-Employed", "Contract"], size=n, p=[0.5, 0.28, 0.22]
    )
    credit_score = rng.normal(650, 60, size=n).clip(300, 850).round(0)
    applicant_income = rng.normal(55000, 20000, size=n).clip(15000, None).round(0)
    loan_amount = rng.normal(15000, 7000, size=n).clip(1000, None).round(0)

    loan_to_income = loan_amount / applicant_income
    emp_risk = (
        pd.Series(employment_type)
        .map({"Salaried": 0, "Self-Employed": 0.3, "Contract": 0.6})
        .values
    )
    z = (
        -0.035 * (credit_score - 650)
        + 4.5 * loan_to_income
        + emp_risk * 1.2
        - 1.0
        + rng.normal(0, 1.1, size=n)
    )
    prob_default = 1 / (1 + np.exp(-z))
    default = (rng.uniform(size=n) < prob_default).astype(int)

    missing_idx = rng.choice(n, 90, replace=False)
    credit_score[missing_idx] = np.nan

    loans = pd.DataFrame(
        {
            "applicant_id": np.arange(1, n + 1),
            "employment_type": employment_type,
            "credit_score": credit_score,
            "applicant_income": applicant_income,
            "loan_amount": loan_amount,
            "default": default,
        }
    )

    X = loans[["credit_score", "applicant_income", "loan_amount", "employment_type"]]
    X = pd.get_dummies(X, columns=["employment_type"], drop_first=True)
    y = loans["default"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    return loans, X, X_train, X_test, y_train, y_test


# ---------------------------------------------------------------------------
# Original structural checks from the brief
# ---------------------------------------------------------------------------

def test_model_metrics_shape(metrics):
    assert REQUIRED_MODELS <= metrics.keys()
    for m in REQUIRED_MODELS:
        assert REQUIRED_METRIC_KEYS <= metrics[m].keys()
    assert "credit_score_imputation_value" in metrics
    assert metrics["final_model"] in REQUIRED_MODELS


def test_charts_exist():
    for name in ["chart_model_comparison.png", "chart_calibration.png"]:
        p = ROOT / name
        assert p.exists() and p.stat().st_size > 1000


def test_report_and_defense_exist():
    assert (ROOT / "evaluation_report.md").exists()
    assert (ROOT / "defense_answers.md").exists()


# ---------------------------------------------------------------------------
# Extra structural / type checks
# ---------------------------------------------------------------------------

def test_metric_values_are_plain_floats_in_unit_interval(metrics):
    for model in REQUIRED_MODELS:
        for key in REQUIRED_METRIC_KEYS:
            value = metrics[model][key]
            assert isinstance(value, float), f"{model}.{key} must be a plain float, got {type(value)}"
            assert 0.0 <= value <= 1.0, f"{model}.{key}={value} outside [0, 1]"


def test_imputation_value_is_numeric(metrics):
    fill = metrics["credit_score_imputation_value"]
    assert isinstance(fill, (int, float))
    assert 300 <= float(fill) <= 850


def test_charts_are_valid_png_files():
    for name in ["chart_model_comparison.png", "chart_calibration.png"]:
        header = (ROOT / name).read_bytes()[:8]
        assert header == b"\x89PNG\r\n\x1a\n", f"{name} is not a valid PNG"


def test_notebook_exists():
    notebooks = list(ROOT.glob("*.ipynb"))
    assert notebooks, "Expected a completed notebook in the project root"


def test_report_and_defense_are_non_empty():
    report = (ROOT / "evaluation_report.md").read_text().strip()
    defense = (ROOT / "defense_answers.md").read_text().strip()
    assert len(report) > 500, "evaluation_report.md looks too short for the required sections"
    assert len(defense) > 500, "defense_answers.md looks too short for five written answers"


# ---------------------------------------------------------------------------
# Spec-locked dataset / split invariants
# ---------------------------------------------------------------------------

def test_dataset_contract_from_generation_code():
    loans, X, X_train, X_test, y_train, y_test = _build_split_frame()
    assert loans.shape == (1200, 6)
    assert loans["credit_score"].isna().sum() == 90
    assert list(X.columns) == [
        "credit_score",
        "applicant_income",
        "loan_amount",
        "employment_type_Salaried",
        "employment_type_Self-Employed",
    ]
    assert len(X_train) == 960
    assert len(X_test) == 240
    assert y_train.mean() == pytest.approx(0.6)
    assert y_test.mean() == pytest.approx(0.6)


def test_credit_score_imputation_is_train_only_not_full_dataset(metrics):
    """Catch the classic leak: fill computed on the full frame before the split."""
    _, X, X_train, _, _, _ = _build_split_frame()
    reported = float(metrics["credit_score_imputation_value"])

    train_median = float(X_train["credit_score"].median())
    train_mean = float(X_train["credit_score"].mean())
    full_median = float(X["credit_score"].median())
    full_mean = float(X["credit_score"].mean())

    assert reported != pytest.approx(full_median, abs=1e-9), (
        "Reported fill matches the FULL-dataset median — compute fill from X_train only"
    )
    matches_train = (
        reported == pytest.approx(train_median, abs=1e-6)
        or reported == pytest.approx(train_mean, abs=1e-6)
    )
    assert matches_train, (
        f"Reported fill {reported} matches neither train median ({train_median}) "
        f"nor train mean ({train_mean}). Got full mean={full_mean}."
    )


def test_baseline_metrics_match_most_frequent_dummy(metrics):
    """DummyClassifier(strategy='most_frequent') on this split has only one answer."""
    for key, expected in BASELINE_EXPECTED.items():
        assert metrics["baseline"][key] == pytest.approx(expected, abs=1e-9), (
            f"baseline.{key}: expected {expected}, got {metrics['baseline'][key]}"
        )


# ---------------------------------------------------------------------------
# Methodology invariants (choices can vary; these should not)
# ---------------------------------------------------------------------------

def test_real_models_beat_baseline_roc_auc(metrics):
    baseline_auc = metrics["baseline"]["roc_auc"]
    for model in REAL_MODELS:
        assert metrics[model]["roc_auc"] > baseline_auc + 0.05, (
            f"{model} ROC-AUC {metrics[model]['roc_auc']} does not clearly beat baseline"
        )


def test_real_models_are_not_identical_to_baseline(metrics):
    for model in REAL_MODELS:
        assert metrics[model] != metrics["baseline"], (
            f"{model} metrics are identical to baseline — model may not have been fit/scored"
        )


def test_final_model_is_not_just_the_dummy(metrics):
    assert metrics["final_model"] in REAL_MODELS, (
        "final_model should be one of the trained classifiers, not the dummy baseline"
    )
    final = metrics["final_model"]
    assert metrics[final]["roc_auc"] > metrics["baseline"]["roc_auc"]


def test_final_model_metrics_are_internally_consistent(metrics):
    """Precision/recall/F1 cannot all be extreme in incompatible ways."""
    final = metrics["final_model"]
    m = metrics[final]
    if m["precision"] > 0 and m["recall"] > 0:
        expected_f1 = 2 * m["precision"] * m["recall"] / (m["precision"] + m["recall"])
        assert m["f1"] == pytest.approx(expected_f1, abs=1e-6)


# ---------------------------------------------------------------------------
# Written deliverables: required topics present
# ---------------------------------------------------------------------------

def test_evaluation_report_covers_required_topics():
    text = (ROOT / "evaluation_report.md").read_text().lower()
    required_snippets = [
        "baseline",
        "logistic",
        "decision tree",
        "random forest",
        "final",
        "error",
        "calibration",
        "limitation",
    ]
    missing = [s for s in required_snippets if s not in text]
    assert not missing, f"evaluation_report.md missing expected topics: {missing}"


def test_evaluation_report_includes_a_comparison_table():
    text = (ROOT / "evaluation_report.md").read_text()
    assert "|" in text, "evaluation_report.md should include a markdown comparison table"
    assert "accuracy" in text.lower() and "recall" in text.lower()


def test_defense_answers_all_five_prompts():
    text = (ROOT / "defense_answers.md").read_text().lower()
    topic_checks = [
        ("random forest / final-model choice", ["random forest", "logistic"]),
        ("imputation leakage", ["imput", "split", "train"]),
        ("accuracy vs recall", ["accuracy", "recall"]),
        ("calibration / interest rate", ["calibrat", "probabilit"]),
        ("missing real-world factor", ["debt", "payment", "history", "income", "feature"]),
    ]
    for label, keywords in topic_checks:
        assert any(k in text for k in keywords), (
            f"defense_answers.md does not clearly address: {label}"
        )


def test_defense_cites_numeric_results():
    text = (ROOT / "defense_answers.md").read_text()
    numbers = re.findall(r"\b0\.\d{2,}\b", text)
    assert len(numbers) >= 5, (
        "defense_answers.md should cite several of your actual metric values"
    )
