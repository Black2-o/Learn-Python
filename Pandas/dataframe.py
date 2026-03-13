import pandas as pd 

# --- WHAT IS A DATAFRAME? ---
# A DataFrame is a 2-dimensional tabular data structure with rows and columns.
# Think of it like an Excel spreadsheet or a SQL table.

# --- 1. CREATING A DATAFRAME ---
# We can create a DataFrame from a dictionary where keys are column names 
# and values are lists of data for those columns.
data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 40],
}

df = pd.DataFrame(data)
print("Default DataFrame (Auto-numbered index):")
print(df)

# --- 2. CUSTOMIZING THE INDEX ---
# By default, Pandas uses 0, 1, 2... as row labels. We can specify our own labels.
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
print("\nDataFrame with Custom Index:")
print(df)

# --- 3. ACCESSING DATA ---
# Access a row by its LABEL using .loc[]
print("\nAccessing 'Employee 2' using .loc:")
print(df.loc["Employee 2"])

# Access a row by its INTEGER POSITION using .iloc[] (0-based)
print("\nAccessing the 3rd row (index 2) using .iloc:")
print(df.iloc[2])

# --- 4. MODIFYING COLUMNS ---
# Adding a new column is as simple as assigning a list to a new key.
df["job"] = ["Fry Cook", "N/A", "Cashier"]
print("\nDataFrame after adding 'job' column:")
print(df)

# --- 5. ADDING NEW ROWS ---
# To add rows, we create another DataFrame and use pd.concat() to join them.
new_row = pd.DataFrame(
    [
        {"Name": "Sandy", "Age": "28", "job": "Engineer"}, 
        {"Name": "Eugene", "Age": "60", "job": "Manager"}
    ], 
    index=["Employee 4", "Employee 5"]
)

# concat() combines the original 'df' with 'new_row'
df = pd.concat([df, new_row])
print("\nFinal DataFrame after adding new rows:")
print(df)
