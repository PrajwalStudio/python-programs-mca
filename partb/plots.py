import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

categories = ["A", "B", "C", "D"]
values = [5, 7, 3, 4]
plt.bar(categories, values)
plt.title("Bar Chart")
plt.show()

slices = [30, 25, 20, 25]
labels = ["Apple", "Banana", "Mango", "Grapes"]
plt.pie(slices, labels=labels)
plt.title("Pie Chart")
plt.show()

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.hist(data, bins=5)
plt.title("Histogram")
plt.show()
