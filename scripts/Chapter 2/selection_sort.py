def findSmollest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmollest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5,3,8,2,6,9,7,5]))
print(selectionSort([53,3345,854,34,622,952,74,15]))
