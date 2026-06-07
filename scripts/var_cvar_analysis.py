from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent
nav_df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_nav_history.csv"
)
nav_df["date"] = pd.to_datetime(nav_df["date"])
nav_df = nav_df.sort_values(
    ["amfi_code", "date"]
)
nav_df["daily_return"] = (
    nav_df.groupby("amfi_code")["nav"]
    .pct_change()
)
results = []
for fund in nav_df["amfi_code"].unique():

    returns = nav_df[
        nav_df["amfi_code"] == fund
    ]["daily_return"].dropna()

    if len(returns) < 30:
        continue

    var95 = np.percentile(
        returns,
        5
    )

    cvar95 = returns[
        returns <= var95
    ].mean()

    results.append([
        fund,
        var95,
        cvar95
    ])
risk_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "VaR_95",
        "CVaR_95"
    ]
)
risk_df.to_csv(
    BASE_DIR / "data" / "analytics" / "var_cvar_report.csv",
    index=False
)
print(risk_df.head())