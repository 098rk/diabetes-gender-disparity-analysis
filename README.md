# Diabetes Gender Disparity Analysis

This repository contains the full reproducible analysis code and synthetic dataset for the article:

**"Gender Disparities in Random Blood Glucose Levels Among Pakistani Adults with Type 2 Diabetes: A Cross-Sectional Analysis"**

## Contents

- `diabetes_study_raw.csv` – Synthetic dataset (N=300) mimicking the study cohort.
- `analysis.py` – Python script that performs all statistical and machine learning analyses reported in the paper.
- `requirements.txt` – List of required Python packages.
- `README.md` – This file.

## Reproducibility

All analyses are seeded with `random_state=42` to ensure exact reproducibility. The synthetic dataset was generated to match the key statistics from the article (gender balance, age range, glucose means, etc.). Running `analysis.py` will produce:

- Console output with regression coefficients, model performance, and test statistics.
- Diagnostic plots saved as `diagnostic_plots.png`.
- Feature importance plot saved as `feature_importance.png`.
- Gender distribution plot saved as `gender_distribution.png`.
- A text file `analysis_results.txt` summarizing the main results.

## How to Run

1. Clone this repository or download the files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
