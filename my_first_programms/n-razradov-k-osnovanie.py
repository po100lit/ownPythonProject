# Найти количество N-значных чисел в системе счисления с основанием K,
# таких, что их запись не содержит двух подряд идущих нулей.
# Например: N = 3, K = 2 - 101, 110, 111 - 3 числа (100 не подходит по условию)

import string
import textwrap

n = int(input('Введите Количество знаков '))
k = int(input('Введите разрядность системы '))


def main():
    digits = string.digits + string.ascii_uppercase
    low_limit = int(str(10 ** (n - 1)), k)
    high_limit = int(str(10 ** n), k)
    numbers_list = []
    for i in range(low_limit, high_limit):
        res = ''
        while i > 0:
            res = digits[i % k] + res
            i //= k
        if '00' not in res:
            numbers_list.append(res)
    print(f'Количество {n}-значных чисел без двух нулей подряд: {len(numbers_list)}')

    is_numbers_print = input('Вывести числа в консоль? y/n: ')
    if is_numbers_print.lower() == 'y':
        print(textwrap.fill(' '.join(numbers_list), 120))

    # Решение Олега (Htyg) через рекурсию
    def True_numbers(n, k):  # Количество "подходящих" чисел
        if n == 1:
            return k - 1  # Количество не нулевых однозначных чисел
        if n == 2:
            return (k - 1) * k  # Количество двухзначных чисел
        return ((k - 1) *  # Количество чисел которые могут стоять первыми(в самом большом разряде)
                (True_numbers(n - 1, k) +  # Количество чисел если последняя цифа 0
                 True_numbers(n - 2, k)))  # Количество чисел если последняя цифра не 0

    print(True_numbers(n, k))


if __name__ == "__main__":
    main()
