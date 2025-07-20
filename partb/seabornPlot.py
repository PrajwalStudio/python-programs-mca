import seaborn as sns
import matplotlib.pyplot as plt

# Load built-in dataset
df = sns.load_dataset("iris")

# Scatterplot
sns.scatterplot(df, x="sepal_length", y="sepal_width", hue="species")
plt.title("Sepal Length vs Sepal Width")
plt.show()

# Boxplot
sns.boxplot(df, x="species", y="petal_length", hue="species")
plt.title("Petal Length by Species")
plt.show()

# Histogram
sns.histplot(df["sepal_length"], kde=True)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.show()
