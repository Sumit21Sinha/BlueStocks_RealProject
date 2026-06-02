import pandas as pd
from pathlib import Path

data_path = Path("../data/raw")

files = list(data_path.glob("*.csv"))

print(f"Total files found: {len(files)}")

for file in files:
    print("\n" + "=" * 60)
    print(f"DATASET : {file.name}")

    df = pd.read_csv(file)

    print(f"Shape : {df.shape}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())