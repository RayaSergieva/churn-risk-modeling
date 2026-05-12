# Self-Assessment

## Problem Understanding and Formulation

The project addresses customer churn prediction, a common real-world business problem where companies want to identify customers who are likely to leave. The problem is formulated as a binary classification and probability-estimation task.

The project uses two independent datasets from different domains: telecommunications and banking. This satisfies the requirement for multiple data sources and gives broader analytical context.

## Writing Layout

The project is organized into two notebooks:

1. `01_data_loading_and_validation.ipynb` — data loading, validation, cleaning, and exploratory data analysis.
2. `02_modeling.ipynb` — mathematical foundations and supervised modeling.

Markdown explanations are included before and after code sections so that the notebooks read as an analysis report rather than only code.

## Mathematical Understanding

The modeling notebook explains the churn problem as probability estimation, introduces logistic regression, defines the sigmoid function, explains log-loss / binary cross-entropy, and discusses why ROC-AUC and PR-AUC are more appropriate than accuracy under class imbalance.

Gradient boosting is also described as a non-linear additive model that can capture interactions and non-linear feature effects.

## Code Quality

The project uses a clean repository structure with separate folders for raw data, processed data, notebooks, source code, and documentation. Data cleaning logic is separated into `src/cleaning.py`, which improves readability and reusability.

The raw and processed datasets are excluded from version control through `.gitignore`, while data sources and download instructions are documented in `data/README.md`.

## Methods and Data Handling

The project includes data validation, missing-value investigation, type correction, target harmonization, and exploratory data analysis across both datasets. The Telco dataset required special handling of the `TotalCharges` column, where whitespace values were found for customers with zero tenure.

The modeling section uses a stratified train/test split, one-hot encoding for categorical variables, standard scaling for numeric variables, logistic regression, and XGBoost. Evaluation includes ROC-AUC, PR-AUC, log-loss, accuracy, classification reports, confusion matrices, and ROC / precision-recall curves.

## Limitations

The project could be improved by adding calibration analysis, feature importance interpretation, modeling on the bank dataset, and business-cost-sensitive threshold optimization. These are left as future work.