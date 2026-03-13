import pandas as pd

# Load CSV file
df = pd.read_csv("data.csv")

# Convert to JSON and save
df.to_json("data.json", orient="records", indent=4)

print("CSV successfully converted to JSON and saved as data.json")
