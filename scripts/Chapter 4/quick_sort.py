from random import randrange as rnd

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        grater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(grater)

def printArray(arr):
    print(arr, quickSort(arr))

printArray([rnd(100) for i in range(rnd(10))])
