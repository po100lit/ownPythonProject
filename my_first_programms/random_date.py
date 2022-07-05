import random as rd


def generate_year():
    y = rd.randint(1970, 2020)
    return y


def generate_month():
    m = rd.randint(1, 12)
    return '{:02}'.format(m)


def generate_day(y, m):
    m_30 = [4, 6, 9, 11]
    m_31 = [1, 3, 5, 7, 8, 10, 12]
    if m in m_31:
        d = rd.randint(1, 31)
    elif m in m_30:
        d = rd.randint(1, 30)
    else:
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            d = rd.randint(1, 29)
        else:
            d = rd.randint(1, 28)
    return '{:02}'.format(d)


def main():
    count = int(input('количество генерируемых дат: '))
    for i in range(count):
        print(f'{generate_day(generate_year(), generate_month())}.{generate_month()}.{generate_year()}')


if __name__ == '__main__':
    main()
