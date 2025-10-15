import pandas as pd
import os

PARQUET_FILE = "data/data.parquet"

# Create two example rows of data
data1 = {"id": 1, "name": "Vanitas", "score": 95}
data2 = {"id": 2, "name": "Wasiq", "score": 100}

# Combine into a DataFrame
df_new = pd.DataFrame([data1, data2])

# If Parquet file exists, read it and append
if os.path.exists(PARQUET_FILE):
    df_existing = pd.read_parquet(PARQUET_FILE)
    df_combined = pd.concat([df_existing, df_new]).drop_duplicates(subset=["id"])
else:
    df_combined = df_new

# Save back to Parquet
os.makedirs(os.path.dirname(PARQUET_FILE), exist_ok=True)
df_combined.to_parquet(PARQUET_FILE, index=False)

print("Data written to Parquet with unique rows:")
print(df_combined)
