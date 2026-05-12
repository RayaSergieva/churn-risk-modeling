# Churn Risk Modeling

End-to-end customer churn analysis and prediction using two independent datasets: IBM Telco Customer Churn and Bank Customer Churn.

## Project Overview

Customer churn prediction is a common business problem where the goal is to identify customers who are likely to leave. This project analyzes churn patterns, validates and cleans raw datasets, performs exploratory data analysis, explains the mathematical foundations of binary classification, and trains machine-learning models to estimate churn risk.

The project uses two independent data sources from different business domains: telecommunications and banking. This allows the analysis to compare whether similar churn-modeling workflows can be applied across different industries.

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

Contains:

- loading both raw datasets
- validating shapes, column types, missing values, and target distributions
- cleaning the Telco and Bank datasets
- saving processed datasets
- exploratory data analysis for both datasets
- visual analysis of churn drivers across domains

### `02_modeling.ipynb`

Contains:

- mathematical formulation of churn prediction as a probability-estimation task
- logistic regression theory
- gradient boosting explanation
- class-imbalance evaluation
- ROC-AUC, PR-AUC, log-loss, accuracy, and confusion matrices
- model comparison on both the Telco and Bank datasets

## Main Findings

- Telco churn is strongly associated with short tenure, month-to-month contracts, and service/price structure.
- Bank churn is strongly associated with geography, age, number of products, active membership, and balance.
- Accuracy alone is misleading because both datasets are imbalanced.
- ROC-AUC, PR-AUC, log-loss, and confusion matrices provide a better evaluation picture than accuracy alone.
- On the Telco dataset, logistic regression produced stronger churn recall, while XGBoost produced higher overall accuracy.
- On the Bank dataset, XGBoost clearly outperformed logistic regression, supporting the EDA finding that Bank churn has stronger non-linear patterns.

## Methods Used

The project includes:

- data validation and vetting
- missing-value investigation
- type correction
- feature cleaning and target harmonization
- exploratory data analysis
- stratified train/test splitting
- one-hot encoding for categorical variables
- standard scaling for numeric variables
- logistic regression
- XGBoost gradient boosting
- ROC and precision-recall curve analysis

## How to Run

Create and activate a virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Download the raw datasets as described in `data/README.md`.

Then run the notebooks in order:

1. `notebooks/01_data_loading_and_validation.ipynb`
2. `notebooks/02_modeling.ipynb`

## Limitations

The two datasets come from different domains and cannot be merged at the individual customer level. The project compares them conceptually and methodologically rather than combining them into one unified customer table.

Future work could include probability calibration, SHAP-based interpretation, business-cost-sensitive threshold optimization, and a more detailed comparison of feature importance across the Telco and Bank domains.

## License

This project is licensed under the MIT License.