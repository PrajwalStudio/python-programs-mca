import numpy as np

r = int(input("Enter number of rows (r): "))
c = int(input("Enter number of columns (c): "))

array=np.zeros((r,c),dtype=int)
for i in range(r):
    for j in range(c):
        array[i][j]=int(input(f"Enter the element for Row{i} and Column{j}:"))

print("\n Array:")
print(array)

print("\nArray Attributes:")
print("Shape          :", array.shape)
print("Size           :", array.size)
print("Data type      :", array.dtype)
print("Dimensions     :", array.ndim)
print("Item size (in bytes):", array.itemsize)
