# Найти количество N-значных чисел в системе счисления с основанием K,
# таких, что их запись не содержит двух подряд идущих нулей.
# Например: N = 3, K = 2 - 101, 110, 111 - 3 числа (100 не подходит по условию)

import string


def main():
    digits = string.digits + string.ascii_uppercase
    n = int(input('Введите количество разрядов: '))
    k = int(input('Введите основание системы счисления: '))
    low_limit = int(str(10 ** (n - 1)), k) # Минимальное N-значное число в с/с с основанием K в десятичном виде
    high_limit = int(str(10 ** n), k) # Минимальное (N+1)-значное число в с/с с основанием K в десятичном виде
    numbers_list = []
    for i in range(low_limit, high_limit):
        res = ''
        while i > 0:
            res = digits[i % len(digits[:k])] + res
            i //= len(digits[:k])
        if '00' not in res:
            numbers_list.append(res)
    print(f'Количество {n}-значных чисел без двух нулей подряд: {len(numbers_list)}')


if __name__ == "__main__":
    main()
