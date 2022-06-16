# вычисление средних значений
from random import randint
from art import tprint

tprint('averages',font='random')

quantity = int(input('Введите количество генерируемых чисел: '))
num_list = []
for i in range(1, quantity + 1):
    num_list.append(randint(1, 100))
print(f'список чисел: {num_list}')

# гармоническое
harmonic = 0
for i in range(len(num_list)):
    harmonic += 1 / num_list[i]
print(f'среднее  гармоническое: {len(num_list) / harmonic}')

# геометрическое
product = 1
for i in range(len(num_list)):
    product = product * num_list[i]
print(f'среднее геометрическое: {pow(product, 1 / len(num_list))}')

# арифметическое
summ = 0
for i in range(len(num_list)):
    summ += num_list[i]
print(f'среднее арифметическое: {summ / len(num_list)}')

# квадратичное (квадратическое)
squared = 0
for i in range(len(num_list)):
    squared += num_list[i] ** 2
print(f'среднее   квадратичное: {pow(squared / len(num_list), 0.5)}')

print('---\nдля любых неотрицательных чисел верно неравенство')
print('квадратичное >= арифметическое >= геометрическое >= гармоническое')
