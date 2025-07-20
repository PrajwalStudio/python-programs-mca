import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("salary_data.csv")

# Extract features and target variable
experience = df["YearsExperience"].values.reshape(-1, 1)
salary = df["Salary"].values.reshape(-1, 1)

# Create and train the model
model = LinearRegression()
model.fit(experience, salary)

# Get model parameters
r_sq = model.score(experience, salary)
intercept = model.intercept_.item()
slope = model.coef_.item()

# Display model evaluation
print(f"Coefficient of determination (R²): {r_sq:.2f}")
print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")

# Predict salary for 15 years of experience
new_exp = np.array([[15]])
psal = model.predict(new_exp).item()
print(f"Predicted salary | 15 YO E: {psal:.2f}")

# Plotting
plt.plot(experience, model.predict(experience), color="red")
plt.scatter(experience, salary)
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend(["Prediction Line", "Actual Data"])
plt.title("Linear Regression: Experience vs. Salary")
plt.show()
