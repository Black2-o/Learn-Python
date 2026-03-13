import pandas as pd 

df = pd.read_csv("data.csv")

print(df)

print(df.to_string())

df = pd.read_json("data.json")

print(df)