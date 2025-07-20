import pandas as pd

# Load the dataset with custom NA values
df = pd.read_csv("Toyota.csv", na_values=["??", "????"])
print("Imported Dataset", df.shape)

# Count missing values before cleaning
print("\nMissing values:", df.isna().sum().sum())

# Filling missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["KM"] = df["KM"].fillna(df["KM"].mean())
df["FuelType"] = df["FuelType"].fillna(df["FuelType"].value_counts().index[0])
df["HP"] = df["HP"].fillna(df["HP"].median())
df["MetColor"] = df["MetColor"].fillna(df["MetColor"].mode()[0])

# Count missing values after cleaning
print("Missing values after cleaning:", df.isna().sum().sum())

# Create two DataFrames
df1 = pd.DataFrame({
    "city": ["Mangaluru", "Bengaluru", "Mysore"],
    "temp": [35, 40, 21]
})

df2 = pd.DataFrame({
    "city": ["Mangaluru", "Bengaluru", "Mysore"],
    "humidity": [80, 60, 40]
})

print("\nDF1:\n", df1)
print("\nDF2:\n", df2)

# Add new column
df1["windspeed"] = [40, 10, 15]
print("\nAfter adding windspeed column:\n", df1)

# Merge the two DataFrames on "city"
df1 = pd.merge(df1, df2, on="city")
print("\nAfter merging DF1 and DF2:\n", df1)
