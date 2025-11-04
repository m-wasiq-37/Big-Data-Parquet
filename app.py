from hdfs import InsecureClient
import pandas as pd
import time

# Wait for Hadoop NameNode
time.sleep(10)

# Connect to Hadoop NameNode
client = InsecureClient('http://namenode:50070', user='hadoop')

# Create sample data
data = {
    "id": [1, 2, 3],
    "name": ["Wasiq", "Ali", "Sara"],
    "marks": [95, 88, 92]
}
df = pd.DataFrame(data)

# Save CSV locally
csv_file = "students.csv"
df.to_csv(csv_file, index=False)

# Write to HDFS
hdfs_path = "/user/hadoop/students.csv"
with open(csv_file, "r") as f:
    client.write(hdfs_path, data=f, overwrite=True)

print(f"✅ File saved to HDFS at {hdfs_path}")

# Read from HDFS
with client.read(hdfs_path, encoding='utf-8') as reader:
    content = reader.read()

print("\n--- File Content from HDFS ---")
print(content)
