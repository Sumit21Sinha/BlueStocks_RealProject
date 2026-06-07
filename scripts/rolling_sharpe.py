from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
BASE_DIR = Path(__file__).resolve().parent.parent
nav_df = pd.read_csv(BASE_DIR / "data" / "processed" / "clean_nav_history.csv")
nav_df["date"] = pd.to_datetime(nav_df["date"])
funds = nav_df["amfi_code"].unique()[:5]
plt.figure(figsize=(12,6))
for fund in funds:
    temp = nav_df[
        nav_df["amfi_code"] == fund
    ].copy()

    temp["return"] = temp["nav"].pct_change()

    rolling_sharpe = (
        temp["return"]
        .rolling(90)
        .mean()
        /
        temp["return"]
        .rolling(90)
        .std()
    ) * np.sqrt(252)

    plt.plot(
        temp["date"],
        rolling_sharpe,
        label=str(fund)
    )
plt.legend()
plt.title("Rolling 90-Day Sharpe Ratio")
plt.tight_layout()
plt.savefig(BASE_DIR / "reports" / "rolling_sharpe_chart.png")
plt.show()