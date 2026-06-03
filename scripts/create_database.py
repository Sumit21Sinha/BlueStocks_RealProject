from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
db_dir = BASE_DIR / "data" / "db"
db_dir.mkdir(exist_ok=True)
db_path = db_dir / "bluestock_mf.db"
schema_path = BASE_DIR / "sql" / "schema.sql"
conn = sqlite3.connect(db_path)
with open(schema_path, "r") as f:
    schema = f.read()
conn.executescript(schema)
conn.commit()
conn.close()
print("Database Created Successfully")
print(f"Location: {db_path}")