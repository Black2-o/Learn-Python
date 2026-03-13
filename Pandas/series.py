# Import the pandas library and give it the alias 'pd' for easier reference
import pandas as pd 

# Series = A Pandas 1-Dimensional labeled array that can hold any data type
#          Think of it like a single column in a spreadsheet (1-Dimensional)

# ---------------------------------------------------------
# 1. CREATING A BASIC SERIES FROM A LIST
# ---------------------------------------------------------

# Create a simple Python list containing integers
data = [100, 101, 102, 103, 104]

# Convert the list into a Pandas Series (automatically assigns numerical indices 0, 1, 2...)
series = pd.Series(data)

# Print the entire Series to the console
print(series)

# ---------------------------------------------------------
# 2. SERIES WITH FLOATING POINT NUMBERS
# ---------------------------------------------------------

# Create a list with decimals (floats)
data = [100.1, 101.0, 102.3, 103.4, 104.5]

# Convert it to a Series (notice the 'dtype' will change to float64)
series = pd.Series(data)

# Print the float Series
print(series)

# Informational print statement
print("Can Be any Other Data type also Like Objects Then Bool and others etc.")

# ---------------------------------------------------------
# 3. SERIES WITH CUSTOM LABELS (INDEXING)
# ---------------------------------------------------------

# Re-using the integer list
data = [100, 101, 102, 103, 104]

# Create a Series but manually specify labels for each row using the 'index' parameter
# This makes it easier to reference specific data points using names instead of just numbers
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

# Print the labeled Series
print(series)

# Access data using the custom label 'a' with .loc (Label-based location)
print(series.loc['a'])

# Access data using the custom label 'b' directly (shorthand)
print(series['b'])

# Update/Change the value at index 'c' to 200
series.loc["c"] = 200

# Print the Series to see the updated value
print(series)

# Access data using the integer position (0-based) using .iloc (Integer-location)
# Here, index 4 corresponds to the 5th element ('e')
print(series.iloc[4])

# Filtering: Print only the values in the Series that are greater than or equal to 102
print(series[series >= 102])

# ---------------------------------------------------------
# 4. CREATING A SERIES FROM A DICTIONARY
# ---------------------------------------------------------

# Create a dictionary where keys become indices and values become the data
calories = {
    "Day 1": 1750,
    "Day 2": 2100,
    "Day 3": 1700
}

# Convert the dictionary into a Series
series = pd.Series(calories)

# Print the Series (keys become labels, values become the column)
print(series)

# Use .loc to find the calories for a specific key/label ("Day 2")
print(series.loc["Day 2"])

# Increment the value for "Day 3" by 500 (1700 + 500 = 2200)
series.loc["Day 3"] += 500

# Print the updated value for "Day 3"
print(series.loc["Day 3"])

# Filter the Series: Only show days where calories are 2000 or more
print(series[series >= 2000])

# ---------------------------------------------------------
# 5. HOMEWORK: SERIES FROM A LIST OF STRINGS (OBJECTS)
# ---------------------------------------------------------

# Create a list of names (strings)
name = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard"]

# Convert the list of strings into a Series (Pandas treats strings as 'object' type)
series = pd.Series(name)

# Print the Pokemon Series
print(series)
