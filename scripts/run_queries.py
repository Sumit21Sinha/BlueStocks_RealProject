from pathlib import Path
import sqlite3
import pandas as pd
BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "data" / "db" / "bluestock_mf.db"
conn = sqlite3.connect(db_path)
query = """
SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;
"""
df = pd.read_sql_query(query, conn)
print(df)
conn.close()