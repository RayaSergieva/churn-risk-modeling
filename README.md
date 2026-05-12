# Churn Risk Modeling

End-to-end customer churn analysis and prediction using two independent datasets: IBM Telco Customer Churn and Bank Customer Churn.

## Project Overview

Customer churn prediction is a common business problem where the goal is to identify customers who are likely to leave. This project analyzes churn patterns, validates and cleans raw datasets, performs exploratory data analysis, explains the mathematical foundations of binary classification, and trains machine-learning models to estimate churn risk.

## Data Sources

This project uses two Kaggle datasets:

1. **Telco Customer Churn**
   - Domain: telecommunications
   - Rows: 7,043
   - Target: `Churn`

2. **Bank Customer Churn**
   - Domain: retail banking
   - Rows: 10,000
   - Target: `Exited`

Raw data files are not committed to the repository. Download instructions are provided in `data/README.md`.

## Repository Structure

```text
churn-risk-modeling/
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
├── docs/
│   └── self_assessment.md
├── notebooks/
│   ├── 01_data_loading_and_validation.ipynb
│   └── 02_modeling.ipynb
├── src/
│   └── cleaning.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Notebooks

### `01_data_loading_and_validation.ipynb`

Contains data loading, validation, cleaning, processed-data saving, and exploratory data analysis for both datasets.

### `02_modeling.ipynb`

Contains the mathematical formulation of churn prediction, logistic regression, gradient boosting, class-imbalance evaluation, and Telco model comparison.

## Main Findings

- Telco churn is strongly associated with short tenure, month-to-month contracts, and service/price structure.
- Bank churn is strongly associated with geography, age, number of products, active membership, and balance.
- Accuracy alone is misleading because both datasets are imbalanced.
- ROC-AUC, PR-AUC, log-loss, and confusion matrices provide a better evaluation picture.
- Logistic regression produced stronger churn recall, while XGBoost produced higher overall accuracy.

## How to Run

Create and activate a virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Download the raw datasets as described in `data/README.md`.

Then run the notebooks in order:

1. `notebooks/01_data_loading_and_validation.ipynb`
2. `notebooks/02_modeling.ipynb`

## License

This project is licensed under the MIT License.