from random import randrange as rand

def max(arr):
    print(f'Array is {arr}')
    if len(arr) == 0:
        return 0
    else:
        m = max(arr[1:])
        if arr[0] > m:        
            return arr[0]
        else:
            return m


arr = [rand(10) for i in range(rand(10))]

print(f'For array {arr} max is {max(arr)}')
