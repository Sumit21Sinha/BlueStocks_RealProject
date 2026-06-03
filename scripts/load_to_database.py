from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parent.parent

# Database
db_path = BASE_DIR / "data" / "db" / "bluestock_mf.db"

engine = create_engine(
    f"sqlite:///{db_path}"
)

# ------------------------
# Load DataFrames
# ------------------------

fund_df = pd.read_csv(
    BASE_DIR / "data" / "raw" / "01_fund_master.csv"
)

nav_df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_nav_history.csv"
)

tx_df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_transactions.csv"
)

perf_df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_scheme_performance.csv"
)

# ------------------------
# Load Into SQLite
# ------------------------

fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

tx_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("All Tables Loaded Successfully")

print("\nTable Counts:")

print("dim_fund:", len(fund_df))
print("fact_nav:", len(nav_df))
print("fact_transactions:", len(tx_df))
print("fact_performance:", len(perf_df))