"""
fig4_diagnostic_plots.py

Generate diagnostic plots for multivariate linear regression model
(Random Blood Sugar as dependent variable).
Plots: (a) residuals vs fitted values, (b) histogram of residuals,
(c) normal Q-Q plot.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.graphics.gofplots import qqplot

# ------------------------------
# 1. Load and prepare data
# ------------------------------
df = pd.read_csv("C:\\Users\\Dell\\PycharmProjects\\DjangoProject\\templates\\diabetes_study_data.csv")

# Define dependent variable
y = df['rbs']  # Random Blood Glucose (mg/dL)

# Convert categorical variables to dummy variables (integers, not bool)
# Create dummies for 'activity' (reference = 'High')
act_dummies = pd.get_dummies(df['activity'], prefix='act', drop_first=True).astype(int)

# Create dummies for 'ses' (reference = 'High')
ses_dummies = pd.get_dummies(df['ses'], prefix='ses', drop_first=True).astype(int)

# Drop original categorical columns and add dummies
df = df.drop(['activity', 'ses'], axis=1)
df = pd.concat([df, act_dummies, ses_dummies], axis=1)

# Now all predictors are numeric. Select the ones for the model.
# Note: 'gender' and 'family_history' are already 0/1 integers.
X = df[['age', 'bmi', 'gender', 'family_history',
        'act_Low', 'act_Moderate', 'ses_Low', 'ses_Middle']]

# Add constant for intercept
X = sm.add_constant(X)

# Check for missing values
if X.isnull().any().any() or y.isnull().any():
    print("Warning: Missing values detected. Dropping rows with missing data.")
    combined = pd.concat([y, X], axis=1).dropna()
    y = combined['rbs']
    X = combined.drop('rbs', axis=1)

# ------------------------------
# 2. Fit model and get residuals
# ------------------------------
model = sm.OLS(y, X).fit()
fitted = model.fittedvalues
residuals = model.resid

# ------------------------------
# 3. Diagnostic tests
# ------------------------------
shapiro_stat, shapiro_p = stats.shapiro(residuals)
print(f'Shapiro-Wilk test: W={shapiro_stat:.3f}, p={shapiro_p:.3f}')

bp_test = het_breuschpagan(residuals, X)
print(f'Breusch-Pagan test: LM={bp_test[0]:.2f}, p={bp_test[1]:.3f}')

# ------------------------------
# 4. Create diagnostic plots
# ------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# (a) Residuals vs Fitted
axes[0].scatter(fitted, residuals, alpha=0.5, edgecolors='k', linewidth=0.5)
axes[0].axhline(y=0, color='red', linestyle='--', linewidth=1)
lowess = sm.nonparametric.lowess(residuals, fitted, frac=0.7)
axes[0].plot(lowess[:, 0], lowess[:, 1], color='blue', linewidth=2)
axes[0].set_xlabel('Fitted Values (mg/dL)')
axes[0].set_ylabel('Residuals')
axes[0].set_title('(a) Residuals vs Fitted')
axes[0].grid(True, linestyle=':', alpha=0.6)

# (b) Histogram of residuals
axes[1].hist(residuals, bins=20, edgecolor='black', alpha=0.7, density=True)
x_norm = np.linspace(residuals.min(), residuals.max(), 100)
mu, std = residuals.mean(), residuals.std()
pdf = stats.norm.pdf(x_norm, mu, std)
axes[1].plot(x_norm, pdf, 'r-', linewidth=2, label='Normal')
axes[1].set_xlabel('Residuals')
axes[1].set_ylabel('Density')
axes[1].set_title('(b) Histogram of Residuals')
axes[1].legend()
axes[1].grid(True, linestyle=':', alpha=0.6)

# (c) Normal Q-Q plot
qqplot(residuals, line='s', ax=axes[2], markersize=4)
axes[2].set_title('(c) Normal Q-Q Plot')
axes[2].grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('figure_4_diagnostic_plots.png', dpi=300, bbox_inches='tight')
plt.show()
