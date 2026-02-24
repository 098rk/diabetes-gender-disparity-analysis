# Diabetes Gender Disparity Analysis

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18756352.svg)](https://doi.org/10.5281/zenodo.18756352)

This repository contains the full reproducible analysis code and synthetic dataset for the article:  

**"Gender Disparities in Random Blood Glucose Levels Among Pakistani Adults with Type 2 Diabetes: A Cross‑Sectional Analysis"**  
*(Authors: Ruby Khan, Salma Rashid, Sumbal Khan, Bakht Pari; under review)*

All code is written in Python and uses standard data science libraries. The synthetic dataset was generated to match the key statistics reported in the manuscript, allowing full reproduction of the figures and statistical results.

---

## Repository Contents

| File | Description |
|------|-------------|
| `diabetic_csv_20260223_6645e9.txt` | Synthetic dataset (N=300) with demographic and clinical variables (age, gender, BMI, activity, SES, family history, diabetes duration, RBS, comorbidities, medication, fasting status). |
| `analysis.py` | Main script performing all statistical analyses reported in the paper: <br> • Descriptive statistics <br> • Simple and multivariate linear regression <br> • Machine learning models (Ridge, SVR, Random Forest, Neural Network, Polynomial Regression) with nested cross‑validation <br> • Feature importance (Random Forest) <br> • Diagnostic tests (Shapiro–Wilk, Breusch–Pagan) <br> • Saves: `gender_distribution.png`, `feature_importance.png`, `diagnostic_plots.png`, `analysis_results.txt` |
| `fig3_gender_glucose_distribution.py` | Generates **Figure 3** of the manuscript: <br> • Left panel: grouped bar chart of glycemic categories (normal, hyperglycemic, severe) by gender <br> • Right panel: pie chart of gender distribution (50% male, 50% female) <br> • Saves: `figure_3_gender_glucose.png` |
| `fig4_diagnostic_plots.py` | Generates **Figure 4** of the manuscript: <br> • (a) Residuals vs. fitted values with quadratic fit <br> • (b) Histogram of residuals with normal density overlay <br> • (c) Normal Q‑Q plot <br> • Prints Shapiro–Wilk and Breusch–Pagan test statistics <br> • Saves: `figure_4_diagnostic_plots.png` |
| `requirements.txt` | List of required Python packages with versions. |
| `README.md` | This file. |

---

## Reproducibility

- All random processes are seeded with `random_state=42` (where applicable) to ensure exact reproducibility.
- The synthetic dataset was constructed to mirror the real study's summary statistics (gender balance, age range, mean glucose, etc.). Running the scripts will produce outputs that match the numbers and figures in the manuscript.

---

## How to Run

1. **Clone or download** this repository to your local machine.
2. **Navigate** to the repository folder.
3. **Install the required dependencies** (preferably inside a virtual environment):
   ```bash
   pip install -r requirements.txt
