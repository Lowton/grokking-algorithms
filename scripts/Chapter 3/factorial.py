def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(f'2! = {factorial(2)}')
print(f'5! = {factorial(5)}')
print(f'0! = {factorial(0)}')
print(f'10! = {factorial(10)}')
