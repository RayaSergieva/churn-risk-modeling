"""
Data cleaning functions for the churn risk modeling project.

This module contains pure data-cleaning functions for the two raw datasets
used in the project: the IBM Telco Customer Churn dataset and the Bank
Customer Churn (Churn Modelling) dataset. Each function takes a raw
DataFrame and returns a cleaned, analysis-ready DataFrame.

Design principles
-----------------
1. Functions are pure: they do not modify their inputs in place. They take
   a DataFrame and return a new one. This makes the code safer to reason
   about and easier to test.
2. Each function has a single, narrowly-defined responsibility.
3. The output schema of each cleaner is documented in its docstring.
4. After cleaning, both datasets share a common target column name (`churn`)
   and a common positive-class encoding (1 = churned, 0 = retained).
"""

from __future__ import annotations

import pandas as pd


# ---------------------------------------------------------------------------
# Telco cleaning
# ---------------------------------------------------------------------------

def clean_telco(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the IBM Telco Customer Churn dataset.

    Operations performed
    --------------------
    1. Drop the identifier column ``customerID`` (not predictive).
    2. Coerce ``TotalCharges`` to numeric; the 11 rows containing
       whitespace correspond to brand-new (tenure=0) customers and are
       imputed to 0.0, the natural value (they have not yet been billed).
    3. Convert ``SeniorCitizen`` from 0/1 integer encoding to a Yes/No
       string, so it matches the encoding of the other binary categorical
       features (consistent encoding simplifies downstream pipeline code).
    4. Replace placeholder phrases ``"No internet service"`` and
       ``"No phone service"`` with plain ``"No"`` in the service-detail
       columns. These placeholders are redundant — they convey the same
       information already encoded in ``InternetService`` and
       ``PhoneService``.
    5. Convert the target ``Churn`` from Yes/No to a 1/0 integer column
       named ``churn`` (lower-case, to match the convention used by the
       bank cleaner).

    Parameters
    ----------
    df : pd.DataFrame
        The raw Telco DataFrame as loaded from CSV.

    Returns
    -------
    pd.DataFrame
        A cleaned copy of the input, with ``churn`` (int) as the target.
    """
    df = df.copy()

    # 1. Drop identifier
    df = df.drop(columns=["customerID"])

    # 2. Fix TotalCharges
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(0.0)

    # 3. Normalise SeniorCitizen encoding
    df["SeniorCitizen"] = df["SeniorCitizen"].map({0: "No", 1: "Yes"})

    # 4. Collapse redundant placeholder values
    placeholder_replacements = {
        "No internet service": "No",
        "No phone service": "No",
    }
    service_detail_cols = [
        "MultipleLines",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
    ]
    df[service_detail_cols] = df[service_detail_cols].replace(placeholder_replacements)

    # 5. Convert target to numeric and rename
    df["churn"] = (df["Churn"] == "Yes").astype(int)
    df = df.drop(columns=["Churn"])

    return df


# ---------------------------------------------------------------------------
# Bank cleaning
# ---------------------------------------------------------------------------

def clean_bank(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the Bank Customer Churn (Churn Modelling) dataset.

    Operations performed
    --------------------
    1. Drop the three identifier / bookkeeping columns ``RowNumber``,
       ``CustomerId``, and ``Surname`` (none have predictive value).
    2. Rename the target column ``Exited`` to ``churn``, matching the
       convention used by the telco cleaner. The encoding (1 = churned,
       0 = retained) is already consistent so no value mapping is needed.

    Parameters
    ----------
    df : pd.DataFrame
        The raw Bank DataFrame as loaded from CSV.

    Returns
    -------
    pd.DataFrame
        A cleaned copy of the input, with ``churn`` (int) as the target.
    """
    df = df.copy()

    df = df.drop(columns=["RowNumber", "CustomerId", "Surname"])
    df = df.rename(columns={"Exited": "churn"})

    return df