from pathlib import Path
import pandas as pd
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = (
    BASE_DIR /
    "data" /
    "raw" /
    "08_investor_transactions.csv"
)
tx_df = pd.read_csv(file_path)
print("Original Shape:", tx_df.shape)
tx_df["transaction_date"] = pd.to_datetime(
    tx_df["transaction_date"]
)
duplicates = tx_df.duplicated().sum()
print("Duplicates:", duplicates)
tx_df = tx_df.drop_duplicates()
invalid_amounts = tx_df[tx_df["amount_inr"] <= 0]
print("Invalid Amount Rows:", len(invalid_amounts))
tx_df = tx_df[
    tx_df["amount_inr"] > 0
]
tx_df["transaction_type"] = (
    tx_df["transaction_type"]
    .str.strip()
    .str.title()
)
valid_kyc = [
    "Verified",
    "Pending"
]
invalid_kyc = tx_df[
    ~tx_df["kyc_status"].isin(valid_kyc)
]
print("Invalid KYC Rows:", len(invalid_kyc))
processed_dir = (
    BASE_DIR /
    "data" /
    "processed"
)
processed_dir.mkdir(exist_ok=True)
output_path = (
    processed_dir /
    "clean_transactions.csv"
)
tx_df.to_csv(
    output_path,
    index=False
)
print("\n===== CLEANING SUMMARY =====")
print("Rows:", len(tx_df))
print(
    "Date Range:",
    tx_df["transaction_date"].min(),
    "to",
    tx_df["transaction_date"].max()
)
print(
    "Unique Investors:",
    tx_df["investor_id"].nunique()
)
print(
    "File Saved Successfully"
)