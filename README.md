Diabetes Gender Disparity Analysis

This repository contains the full reproducible analysis code and synthetic dataset for the article:

"Gender Disparities in Random Blood Glucose Levels Among Pakistani Adults with Type 2 Diabetes: A Cross‑Sectional Analysis"
(Authors: Ruby Khan, Salma Rashid, Sumbal Khan, Bakht Pari; under review)

All code is written in Python and uses standard data science libraries. The synthetic dataset (diabetes_study_data.csv) was generated to match the key statistics reported in the manuscript, allowing full reproduction of the figures and statistical results.
Repository Contents
File	Description
diabetes_study_data.csv	Synthetic dataset (N=300) with demographic and clinical variables (age, gender, BMI, activity, SES, family history, diabetes duration, RBS, comorbidities, medication, fasting status).
analysis.py	Main script performing all statistical analyses reported in the paper:
• Descriptive statistics
• Simple and multivariate linear regression
• Machine learning models (Ridge, SVR, Random Forest, Neural Network, Polynomial Regression) with nested cross‑validation
• Feature importance (Random Forest)
• Diagnostic tests (Shapiro–Wilk, Breusch–Pagan)
• Saves: gender_distribution.png, feature_importance.png, diagnostic_plots.png, analysis_results.txt
fig3_gender_glucose_distribution.py	Generates Figure 3 of the manuscript:
• Left panel: grouped bar chart of glycemic categories (normal, hyperglycemic, severe) by gender
• Right panel: pie chart of gender distribution (50% male, 50% female)
• Saves: figure_3_gender_glucose.png
fig4_diagnostic_plots.py	Generates Figure 4 of the manuscript:
• (a) Residuals vs. fitted values with LOESS smooth
• (b) Histogram of residuals with normal density overlay
• (c) Normal Q‑Q plot
• Prints Shapiro–Wilk and Breusch–Pagan test statistics
• Saves: figure_4_diagnostic_plots.png
requirements.txt	List of required Python packages with versions.
README.md	This file.
Reproducibility

    All random processes are seeded with random_state=42 (where applicable) to ensure exact reproducibility.

    The synthetic dataset was constructed to mirror the real study's summary statistics (gender balance, age range, mean glucose, etc.). Running the scripts will produce outputs that match the numbers and figures in the manuscript.

How to Run

    Clone or download this repository to your local machine.

    Navigate to the repository folder.

    Install the required dependencies (preferably inside a virtual environment):
    bash

    pip install -r requirements.txt

    Run any of the Python scripts:
    bash

    python analysis.py
    python fig3_gender_glucose_distribution.py
    python fig4_diagnostic_plots.py

    Each script reads diabetes_study_data.csv and generates its output files in the current directory.

Outputs

    analysis.py produces:

        Console output: regression coefficients, model performance (MAE, R²), test statistics.

        gender_distribution.png – alternative bar chart of glycemic categories by gender.

        feature_importance.png – Random Forest feature importances.

        diagnostic_plots.png – three‑panel diagnostic figure (identical to Fig. 4).

        analysis_results.txt – text summary of main results.

    fig3_gender_glucose_distribution.py produces:

        figure_3_gender_glucose.png – publication‑ready Figure 3.

    fig4_diagnostic_plots.py produces:

        figure_4_diagnostic_plots.png – publication‑ready Figure 4.

Dependencies

    Python ≥ 3.8

    pandas ≥ 1.5.0

    numpy ≥ 1.23.0

    scikit‑learn ≥ 1.1.0

    statsmodels ≥ 0.13.0

    matplotlib ≥ 3.6.0

    scipy ≥ 1.9.0

All specific versions are listed in requirements.txt.
You are free to use and adapt the code with appropriate attribution.
Citation

If you use this code or dataset in your research, please cite the original article:
text

Khan R, Rashid S, Khan S, Pari B. Gender Disparities in Random Blood Glucose Levels Among Pakistani Adults with Type 2 Diabetes: A Cross‑Sectional Analysis. [Under review].

Contact

For questions or issues, please open an issue on GitHub or contact the corresponding author at [rubykhanutk@gmail.com].
