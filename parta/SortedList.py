def insert_sorted(list, ele):
    list.sort()
    print("Sorted list:", list)
    pos = len(list)
    for k in list:
        if ele < k:
            pos = list.index(k)
            break
    list.insert(pos, ele)  # Insert at the right position
    return list

list = []
n = int(input("Enter the number of elements: "))
print("Enter the array elements in any order:")
for i in range(n):
    list.append(int(input()))

ele = int(input("Enter the element to insert: "))

updated = insert_sorted(list, ele)
print("Updated list:", updated)
