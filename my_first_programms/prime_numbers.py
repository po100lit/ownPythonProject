# простые числа в диапазоне
from sympy import simplify


def main():
    lim = int(input('Введите предел поиска от 0 до: '))
    my_list = []
    for i in range(0, lim + 1):
        if simplify(i).is_prime:
            my_list.append(str(i))
    print(", ".join(my_list))
    print(f'Найдено простых чисел: {len(my_list)}')


if __name__ == '__main__':
    main()
