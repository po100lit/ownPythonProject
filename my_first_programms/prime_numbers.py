# простые числа в диапазоне
from sympy import simplify

lim = int(input('Введите предел поиска: '))
my_list = []
for i in range(0, lim+1):
    if simplify(i).is_prime:
        my_list.append(i)
print(my_list)
print(f'Найдено простых чисел: {len(my_list)}')
