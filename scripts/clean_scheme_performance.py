from pathlib import Path
import pandas as pd
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = (
    BASE_DIR /
    "data" /
    "raw" /
    "07_scheme_performance.csv"
)
perf_df = pd.read_csv(file_path)
print("Original Shape:", perf_df.shape)
print("\nMissing Values:")
print(perf_df.isnull().sum())
duplicates = perf_df.duplicated().sum()
print("\nDuplicates:", duplicates)
perf_df = perf_df.drop_duplicates()
negative_sharpe = perf_df[
    perf_df["sharpe_ratio"] < 0
]
print(
    "\nNegative Sharpe Funds:",
    len(negative_sharpe)
)
invalid_expense = perf_df[
    (perf_df["expense_ratio_pct"] < 0.1) |
    (perf_df["expense_ratio_pct"] > 2.5)
]
print(
    "Invalid Expense Ratio Funds:",
    len(invalid_expense)
)
processed_dir = (
    BASE_DIR /
    "data" /
    "processed"
)
output_path = (
    processed_dir /
    "clean_scheme_performance.csv"
)
perf_df.to_csv(
    output_path,
    index=False
)
print("\nFile Saved Successfully")