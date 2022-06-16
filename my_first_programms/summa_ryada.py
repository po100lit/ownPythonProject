# сумма последовательных N чисел
summ1 = 0
summ2 = 0
lim = int(input('введите число: '))

# через цикл
for i in range(1, lim + 1):
    summ1 += i

# через формулу суммы ряда
summ2 = lim * (lim + 1) / 2

print(summ1)
print(int(summ2))
