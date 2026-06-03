from pathlib import Path
import pandas as pd
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "raw" / "02_nav_history.csv"
nav_df = pd.read_csv(file_path)
print(nav_df.info())
print(nav_df.isnull().sum())
nav_df["date"] = pd.to_datetime(nav_df["date"])
print(nav_df.dtypes)
nav_df = nav_df.sort_values(by=["amfi_code", "date"])
duplicates = nav_df.duplicated().sum()
print("Duplicates:", duplicates)
invalid_nav = nav_df[nav_df["nav"] <= 0]
print("Invalid NAV rows:")
print(len(invalid_nav))
nav_df["nav"]=(nav_df.groupby("amfi_code")["nav"].ffill())
output_path = BASE_DIR / "data" / "processed" / "clean_nav_history.csv"
nav_df.to_csv(output_path, index=False)
print(f"Saved to: {output_path}")


print("\n===== CLEANING SUMMARY =====")
print(f"Total Rows: {len(nav_df)}")
print(f"Unique Funds: {nav_df['amfi_code'].nunique()}")
print(f"Start Date: {nav_df['date'].min()}")
print(f"End Date: {nav_df['date'].max()}")
print("\nFile Saved Successfully")