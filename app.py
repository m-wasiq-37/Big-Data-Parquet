import pandas as pd
import os

PARQUET_FILE = "data/data.parquet"

data1 = {"id": 1, "name": "Vanitas", "score": 95}
data2 = {"id": 2, "name": "Wasiq", "score": 100}

df_new = pd.DataFrame([data1, data2])

if os.path.exists(PARQUET_FILE):
    df_existing = pd.read_parquet(PARQUET_FILE)
    df_combined = pd.concat([df_existing, df_new]).drop_duplicates(subset=["id"])
else:
    df_combined = df_new

os.makedirs(os.path.dirname(PARQUET_FILE), exist_ok=True)
df_combined.to_parquet(PARQUET_FILE, index=False)

print("Data written to Parquet with unique rows:")
print(df_combined)

try:
    from hdfs import InsecureClient
    client = InsecureClient('http://hadoop:9870', user='root')
    hdfs_path = "/data/data.parquet"
    client.upload(hdfs_path, PARQUET_FILE, overwrite=True)
    print(f"Successfully uploaded to HDFS: {hdfs_path}")
except Exception as e:
    print(f"Could not upload to HDFS: {e}")
