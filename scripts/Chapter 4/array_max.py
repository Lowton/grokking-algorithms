from random import randrange as rand

def max(arr):
    if len(arr) == 0:
        return 0
    else:
        if arr[0] > max(arr[1:]):        
            return arr[0]
        else:
            return max(arr[1:])


arr = [rand(10) for i in range(rand(10))]

print(f'For array {arr} max is {max(arr)}')
