# найти все натуральные значения N, чтоб N^2+45 давало X^2

for i in range(1, 101):
    n = i
    for j in range(1, 101):
        x = j
        if n ** 2 + 45 == x ** 2:
            print(f'N = {n}, X = {x}')
