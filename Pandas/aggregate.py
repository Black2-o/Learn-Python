import pandas as pd

# This file demonstrates how to use aggregation functions in Pandas.
# It covers summarizing data (mean, sum, min, max, count) for both 
# entire DataFrames and specific columns, including the use of groupby().

# aggregate function = Reduce a set of value into a single summary values
#                      Used to summarize and analize data
#                      Ofter used with the groupby() function


df = pd.read_csv("data.csv")

# print(df)


# Whole Datafram
# print(df.mean()) Can not use Because we can only use numaric number not any alphabet So

print(df.mean(numeric_only=True))

print(df.sum(numeric_only=True))

print(df.min(numeric_only=True))

print(df.max(numeric_only=True))

print(df.count())


# Single Column 
print(df["Height"].mean())
print(df["Height"].sum())
print(df["Height"].min())
print(df["Height"].max())
print(df["Height"].count())
print(df["Type2"].count())


# Groupby
group = df.groupby("Type1")
print(group["Height"].mean())
print(group["Height"].count()) 
print(group["Height"].sum()) 
print(group["Height"].max()) 
print(group["Height"].min()) 
