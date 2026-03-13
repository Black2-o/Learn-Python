import pandas as pd

# Data Cleaning = the process of fixing/removing:
#                 incomplete, incorrect, or irrelevent data.
#                 ~75% of work done with Pandas is data cleaning

df = pd.read_csv("data.csv")

# print(df)

# 1. Drop irrelevent columns 
# df = df.drop(columns=["Legendary", "No"])
# print(df)

# 2. Handle Missing Data 
df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2": "Unknown"})
# print(df.to_string())


# 3. Fix Any inconsistent values 
df["Type1"] = df["Type1"].replace({"Grass": "Ground", "Fire": "Flame"})

# print(df.to_string())


# 4. Standardize Text
df["Name"] = df["Name"].str.upper()
# print(df)


# 5. Fix Data Types 
df["Legendary"] = df["Legendary"].astype(bool)

# print(df)

# 6. Remove duplicate values
df = df.drop_duplicates()
print(df.to_string())