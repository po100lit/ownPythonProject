import random as rd

defcode_list = [700, 701, 702, 705, 706, 707, 708, 747, 771, 775, 776, 777, 778]
count_number = int(input('Введите количество номеров: '))


def gen3digit():
    res = rd.randint(0, 999)
    return '{:03}'.format(res)


def gen2digit():
    res = rd.randint(0, 99)
    return '{:02}'.format(res)


def gen_phone_num():
    res = f'+7 ({rd.choice(defcode_list)}) {gen3digit()}-{gen2digit()}-{gen2digit()}'
    return res


def main():
    for i in range(count_number):
        print(gen_phone_num())


if __name__ == '__main__':
    main()
