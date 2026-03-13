import pandas as pd 

# --- LOAD DATA ---
# Load the dataset from data.csv into a DataFrame (df)
df = pd.read_csv("data.csv")
print(df)


# --- FILTERING CONCEPTS ---
# Filtering means keeping only the rows that match specific conditions.

# 1. Basic Filtering by Comparison (Height >= 2)
# This creates a new DataFrame containing only 'tall' Pokemon.
tall_pokemon = df[df["Height"] >= 2]
print(tall_pokemon)

# 2. Filtering by Weight (Weight >= 100)
# Keeps only Pokemon that weigh 100 units or more.
heavy_pokemon = df[df["Weight"] >= 100]
print(heavy_pokemon)

# 3. Filtering by Boolean/Binary values (Legendary == True/1)
# You can check for equality to 1 or True depending on how the data is stored.
legendary = df[df["Legendary"] == True] 
print(legendary)


# 4. Filtering by exact String Match (Type1 == "Water")
# Keeps only the Pokemon whose primary type is 'Water'.
water_pokemon = df[df["Type1"] == "Water"]
print(water_pokemon)

# 5. Multiple Conditions with OR (|)
# Matches Pokemon that are 'Water' type in either Type1 OR Type2.
any_water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
print(any_water_pokemon)


# 6. Multiple Conditions with AND (&)
# Matches Pokemon that are BOTH 'Fire' AND 'Flying' types.
fire_fly_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
print(fire_fly_pokemon)
