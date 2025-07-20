#a)Array Manipulation
import numpy as np

arr = np.array([2, 4, 0, 0, 8, 1])
print("Original array:", arr)

print("\nManipulation")
print("Reshaped to 2x3:\n", arr.reshape(2, 3))
print("Appending [2, 6]:", np.append(arr, [2, 6]))
print("Inserting 5 at index 2:", np.insert(arr, 2, 5))

print("\nSearching:")
print("Index of 8:", np.where(arr == 8)[0])
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))

print("\nSorting:")
print("Sorted array:", np.sort(arr))
print("Indices that would sort the array:", np.argsort(arr))

print("\nSplitting:")
print("2 parts:", np.array_split(arr, 2))
arr2d = np.array([[2, 4, 8, 1], [2, 4, 8, 1]])
print("2D Array:\n", arr2d)
print("Horizontal split:", np.hsplit(arr2d, 2))
print("Vertical split:", np.vsplit(arr2d, 2))

#b)Array Broadcasting & Plotting
import numpy as np
import matplotlib.pyplot as plt

arr = np.array([1, 2, 3])
print("Original array:", arr)
print("After broadcasting +5:", arr + 5)
print("After broadcasting *5:", arr * 5)

x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')
plt.title("Sine and Cosine Waves")
plt.xlabel("x")
plt.ylabel("Value")
 
plt.legend()
plt.show()