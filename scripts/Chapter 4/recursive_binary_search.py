def recursiveBinarySearch(arr, item):
    if len(arr) == 1 :
        return 0 if arr[0] == item else None
    else:
        if len(arr) == 0:
            return None
        m = int(len(arr)/2)
        guess = arr[m]
        #print(f'Array {arr} with size {len(arr)}. Take index {m} with value {guess}.')
        if guess == item:
            return m
        if item > guess:
            index = recursiveBinarySearch(arr[m:], item)
            return None if index == None else m + index 
        if item < guess:
            return recursiveBinarySearch(arr[:m], item)

def printArray(arr):
    item = 9
    index = recursiveBinarySearch(arr, item)
    value = arr[index] if not index == None else None
    print(f'Index of {item} in {arr} is {index}. Value from array by index is {value}')


printArray([1,2,3,4,5,6,7,8,9,10,11])
printArray([1,3,5,7,9,11])
printArray([1,5,7,9,11])
printArray([11])
printArray([7,11,14,17,189,222,367])
printArray([])
printArray([0,1,3,9,27,81,243])
