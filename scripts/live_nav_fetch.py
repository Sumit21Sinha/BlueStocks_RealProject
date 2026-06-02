import requests
import pandas as pd
funds = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}
for fund_name, code in funds.items():
    print(f"Fetching {fund_name}")
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data["data"])
    df.to_csv(
        f"../data/raw/{fund_name}.csv",
        index=False
    )
    print(f"{fund_name} saved")