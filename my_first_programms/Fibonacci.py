# ряд Фибоначи

x = None
lim_num = int(input('Сколько чисел вывести: '))

list_fib_pozitive = [0, 1]
for i in range(1, lim_num-1):
    x = list_fib_pozitive[-1] + list_fib_pozitive[-2]
    list_fib_pozitive.append(x)
print(f'положительный ряд {list_fib_pozitive}')

x = None
list_fib_negative = [0, 1]
for i in range(1, lim_num-1):
    x = list_fib_negative[-2] - list_fib_negative[-1]
    list_fib_negative.append(x)
print(f'отрицательный ряд {list_fib_negative}')
