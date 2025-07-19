def linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = []
n = int(input("Enter the number of elements: "))
print("Enter the array elements:")
for _ in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))
index = linearSearch(arr, key)

if index != -1:
    print(f"{key} found at index: {index}")
else:
    print(f"{key} not found in the array.")
