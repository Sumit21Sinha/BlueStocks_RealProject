from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "data" / "db" / "bluestock_mf.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("""SELECT name
    FROM sqlite_master WHERE type='table'""")
tables = cursor.fetchall()
print("Tables in Database:")
for table in tables:
    print(table[0])
conn.close()