import pandas as pd

# 1) Importing the Dataset
df = pd.read_csv("Toyota.csv", na_values=["??", "????"])
print("Imported Dataset", df.shape)

# 2) Cleaning the Data (handling missing values)
print("\nMissing values before cleaning:", df.isna().sum().sum())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["KM"] = df["KM"].fillna(df["KM"].mean())
df["FuelType"] = df["FuelType"].fillna(df["FuelType"].value_counts().index[0])
df["HP"] = df["HP"].fillna(df["HP"].median())
df["MetColor"] = df["MetColor"].fillna(df["MetColor"].mode()[0])
print("Missing values after cleaning:", df.isna().sum().sum())

# 3) DataFrame Manipulation: merge two DataFrames
df1 = pd.DataFrame({
    "city": ["Mangaluru", "Bengaluru", "Mysore"],
    "temp": [35, 40, 21]
})
print(f"Df1:{df1}")
df2 = pd.DataFrame({
    "city": ["Mangaluru", "Bengaluru", "Mysore"],
    "humidity": [80, 60, 40]
})
print(f"Df2:{df2}")
df1["windspeed"] = [40, 10, 15]
merged = pd.merge(df1, df2, on="city")

print("\nFinal Merged DataFrame:\n", merged)

