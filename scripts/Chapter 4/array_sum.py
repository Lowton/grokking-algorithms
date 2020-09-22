from random import randrange as rand
def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr.pop(0) + sum(arr)


arr = [rand(10) for i in range(rand(10))]

print(f'For array {arr} sum is {sum(arr)}')
