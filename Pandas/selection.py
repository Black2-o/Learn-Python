import pandas as pd

"""
PANDAS DATA SELECTION GUIDE
---------------------------
This script demonstrates various ways to select and filter data from a DataFrame
using column names, labels (.loc), and integer positions (.iloc).
"""

# Load the dataset
df = pd.read_csv("data.csv")

# --- 1. SELECTION BY COLUMN ---
# You can select a single column using its name in square brackets.
# This returns a Pandas Series.
print("Selecting 'Name' column:")
print(df["Name"])

# Using .to_string() prints the entire Series without truncation
# (Useful for seeing all rows at once in the terminal)
print("\n'Name' column as string:")
print(df["Name"].to_string())

# --- 2. SELECTING MULTIPLE COLUMNS ---
# To select multiple columns, pass a LIST of column names.
# This returns a new DataFrame.
print("\nSelecting 'Name', 'Height', and 'Weight':")
print(df[["Name", "Height", "Weight"]])

# --- 3. SELECTION BY ROWS (LABELS: .loc) ---
# .loc is label-based, meaning you use row labels or column names.
print("\nAccessing the first row (index 0) using .loc:")
print(df.loc[0])

# --- 4. USING A COLUMN AS THE INDEX ---
# We can set a specific column (like 'Name') as the row labels.
df = pd.read_csv("data.csv", index_col="Name")

print("\nAccessing data for 'Pikachu':")
print(df.loc["Pikachu"])

# You can also select specific columns for a specific row
print("\nHeight and Weight for 'Charizard':")
print(df.loc["Charizard", ["Height", "Weight"]])

# Slicing: Select a range of rows (inclusive) and specific columns
print("\nSlicing from 'Charizard' to 'Pikachu':")
print(df.loc["Charizard":"Pikachu", ["Height", "Weight"]])

# --- 5. SELECTION BY POSITION (INTEGERS: .iloc) ---
# .iloc is integer-based, similar to Python list slicing.
print("\nSelecting first 11 rows (0 to 10):")
print(df.iloc[0:11])

# Every Second Row (using a 'step' of 2)
print("\nEvery second row from first 11 rows:")
print(df.iloc[0:11:2])

# Selecting specific rows and columns by position [rows, columns]
print("\nSlicing rows and columns by position:")
print(df.iloc[0:11:2, 0:3])

# --- 6. INTERACTIVE SEARCH ---
# A practical example of using .loc to find specific data based on user input.
pokemon = input("\nEnter A Pokemon Name to look up: ")

try:
    print(f"\nData for {pokemon}:")
    print(df.loc[pokemon])
except KeyError:
    # .loc raises a KeyError if the label doesn't exist in the index
    print(f"Error: '{pokemon}' not found in the dataset.")