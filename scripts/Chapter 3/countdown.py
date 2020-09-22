def countdown(n):
    print(f'{n}...')
    if n < 1:
        return
    else:
        countdown(n-1)

countdown(57)
