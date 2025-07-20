import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species")
plt.title("Sepal: Length vs Width")
plt.show()

sns.boxplot(data=df, x="species", y="petal_length")
plt.title("Petal Length by Species")
plt.show()

sns.histplot(df["sepal_length"], kde=True)
plt.title("Sepal Length Distribution")
plt.show()
