from pathlib import Path
import pandas as pd
import numpy as np
BASE_DIR = Path(__file__).resolve().parent.parent
nav_df = pd.read_csv(BASE_DIR /"data" /"processed" /"clean_nav_history.csv")
fund_df = pd.read_csv(BASE_DIR /"data" /"raw" /"01_fund_master.csv")
nav_df["date"] = pd.to_datetime(nav_df["date"])
print(nav_df.head())

nav_df["daily_return"]=(nav_df.groupby("amfi_code")["nav"].pct_change())
print(nav_df[["amfi_code", "date", "nav", "daily_return"]].head(10))

cagr_results = []
for fund in nav_df["amfi_code"].unique():
    temp = nav_df[nav_df["amfi_code"]==fund]
    start_nav = temp.iloc[0]["nav"]
    end_nav = temp.iloc[-1]["nav"]
    years=(temp["date"].max()-temp["date"].min()).days/365
    cagr=((end_nav / start_nav)**(1 / years)-1)
    cagr_results.append([fund, cagr])
cagr_df=pd.DataFrame(cagr_results, columns=["amfi_code", "cagr"])
print(cagr_df.head())

volatility_df=(
    nav_df.groupby("amfi_code")
    ["daily_return"]
    .std()
    .reset_index()
)
volatility_df.rename(
    columns={
        "daily_return":
        "volatility"
    },
    inplace=True
)
print(volatility_df.head())

risk_free_rate = 0.06
sharpe_results = []
for fund in nav_df["amfi_code"].unique():
    temp = nav_df[
        nav_df["amfi_code"] == fund
    ]
    annual_return = (
        temp["daily_return"]
        .mean()
        * 252
    )
    volatility = (
        temp["daily_return"]
        .std()
        * np.sqrt(252)
    )
    sharpe = (
        annual_return
        -
        risk_free_rate
    ) / volatility
    sharpe_results.append(
        [fund, sharpe]
    )
sharpe_df = pd.DataFrame(
    sharpe_results,
    columns=[
        "amfi_code",
        "sharpe_ratio"
    ]
)
print(sharpe_df.head())

analytics_df=(cagr_df.merge(volatility_df, on="amfi_code").merge(sharpe_df,on="amfi_code"))
analytics_df=analytics_df.merge(fund_df[["amfi_code", "scheme_name"]], on="amfi_code")
print(analytics_df.head())

analytics_dir=(BASE_DIR /"data" /"analytics")
analytics_dir.mkdir(exist_ok=True)
analytics_df.to_csv(analytics_dir /"fund_analytics.csv",index=False)

import matplotlib.pyplot as plt
import seaborn as sns
top_cagr=(analytics_df.sort_values("cagr", ascending=False).head(10))
plt.figure(figsize=(10,6))
sns.barplot(data=top_cagr, x="cagr", y="scheme_name")
plt.title("Top Funds by CAGR")
plt.show()
top_sharpe=(analytics_df.sort_values("sharpe_ratio", ascending=False).head(10))
plt.figure(figsize=(10,6))
sns.barplot(data=top_sharpe, x="sharpe_ratio", y="scheme_name")
plt.title("Top Funds by Sharpe Ratio")
plt.show()

analytics_df.head()

drawdown_results = []

for fund in nav_df["amfi_code"].unique():
    temp=nav_df[nav_df["amfi_code"]==fund].copy()
    temp["rolling_max"] = temp["nav"].cummax()
    temp["drawdown"]=(temp["nav"]-temp["rolling_max"])/temp["rolling_max"]
    max_drawdown = temp["drawdown"].min()
    drawdown_results.append([fund, max_drawdown])
drawdown_df=pd.DataFrame(drawdown_results, columns=["amfi_code", "max_drawdown"])
print(drawdown_df.head())

analytics_df = analytics_df.merge(
    drawdown_df,
    on="amfi_code"
)
print(analytics_df.head())

analytics_df["score"] = (
      analytics_df["cagr"] * 0.4
    + analytics_df["sharpe_ratio"] * 0.3
    - abs(
        analytics_df["max_drawdown"]
      ) * 0.3
)

analytics_df = analytics_df.sort_values("score", ascending=False)
analytics_df["rank"]=range(1, len(analytics_df)+1)
print(analytics_df[["rank", "scheme_name", "score"]].head(10))
top_ranked = analytics_df.head(10)
plt.figure(figsize=(14,8))
sns.barplot(data=top_ranked, x="score", y="scheme_name")
plt.title("Top Ranked Mutual Funds")
plt.tight_layout()
plt.show()

analytics_df.to_csv(analytics_dir/"fund_analytics_final.csv", index=False)
print("Final analytics saved successfully.")