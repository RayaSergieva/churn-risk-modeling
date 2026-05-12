# Data Sources

This project uses two independent customer churn datasets, downloaded from Kaggle.

## 1. Telco Customer Churn (primary dataset)

- **Source:** https://www.kaggle.com/datasets/blastchar/telco-customer-churn
- **Original publisher:** IBM Sample Data Sets
- **File:** `data/raw/telco_churn.csv`
- **Rows:** 7,043
- **Domain:** Telecommunications subscribers (US)
- **Target variable:** `Churn` (Yes/No) — whether the customer left within the last month
- **License:** Public (IBM Sample Data Sets, redistributed under Kaggle's standard data terms)

## 2. Bank Customer Churn (secondary dataset)

- **Source:** https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling
- **File:** `data/raw/bank_churn.csv`
- **Rows:** 10,000
- **Domain:** Retail banking customers (Europe — France, Spain, Germany)
- **Target variable:** `Exited` (1/0) — whether the customer closed their account
- **License:** Public (Kaggle community dataset)

## How to download

The raw CSV files are **not committed to this repository** to respect dataset licensing and avoid bloating the repo. To reproduce the analysis, install the Kaggle CLI and run:

    pip install kaggle
    # Place your kaggle.json credentials in ~/.kaggle/
    kaggle datasets download -d blastchar/telco-customer-churn -p data/raw --unzip
    kaggle datasets download -d shrutimechlearn/churn-modelling -p data/raw --unzip

Then rename the files:

- `WA_Fn-UseC_-Telco-Customer-Churn.csv` → `telco_churn.csv`
- `Churn_Modelling.csv` → `bank_churn.csv`

## Why two sources?

This project meets the course requirement of two independent data sources. More importantly, comparing churn patterns across telecommunications and banking allows examining whether features and modeling approaches generalize across domains — a question with real practical relevance for transfer of methods between industries.