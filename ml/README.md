# ML (package C)

- `notebooks/`: exploration and training experiments (Jupyter).
- Training data goes in `ml/data/` (ignored by git, it's too big). Download CIC-IDS2017 there.
- Trained models (`*.joblib`) are also ignored by git.

What it must do (PRD 1.3):

1. Map CICFlowMeter output columns to the CIC-IDS2017 training columns.
2. Random Forest for known attack categories, Isolation Forest for anomalies.
3. Score each flow: confidence, severity, detection type, attack category.
4. "Retrain now": retrain on saved TP / BP / FP labels and report before/after scores.
