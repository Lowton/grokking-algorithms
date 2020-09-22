from random import randrange as rand
def count(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count(arr[1:])


arr = [rand(10) for i in range(rand(10))]

print(f'Array {arr} contains {count(arr)} element{"" if len(arr)==1 else "s"}')
