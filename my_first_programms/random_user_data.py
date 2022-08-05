from russian_names import RussianNames
from random import randint
from pprint import pprint
import csv
from faker import Faker


def gen_name():
    return RussianNames().get_person()


def fake_job():
    fake = Faker(locale='ru-RU')
    return fake.job()


def fake_adr():
    fake = Faker(locale='ru-RU')
    return fake.address()


uniq_ids = []


def gen_id():
    global uniq_ids
    fake = Faker()
    for i in range(30):
        uniq_ids.append('{:06}'.format(fake.unique.random_int()))
    return uniq_ids
    # return '{:06}'.format(fake.unique.random_int())


def gen_phone():
    two_dig = '{:02}'.format(randint(0, 99))
    three_dig = '{:03}'.format(randint(0, 999))
    return f'+7 ({randint(100, 999)}) {three_dig}-{two_dig}-{two_dig}'


def gen_date():
    y = randint(1950, 2000)
    m = '{:02}'.format(randint(1, 12))
    m_30 = [4, 6, 9, 11]
    m_31 = [1, 3, 5, 7, 8, 10, 12]
    if m in m_31:
        d = randint(1, 31)
    elif m in m_30:
        d = randint(1, 30)
    else:
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            d = randint(1, 29)
        else:
            d = randint(1, 28)
    d = '{:02}'.format(d)
    return f'{d}.{m}.{y}'


def main():
    # print(gen_id())
    # print(RussianNames().get_person())
    # print(gen_phone())
    # print(gen_date())
    # print(fake_job())
    # print(fake_adr())
    unique_ids = gen_id()
    with open('data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        # writer.writerow(['id', 'Фамилия', 'Имя', 'Отчество', 'Телефон', 'Дата рождения', 'Профессия', 'Адрес'])
        writer.writerow(['id', 'Фамилия', 'Имя', 'Телефон', 'Профессия'])
    for i in range(30):
        fio = gen_name().split()
        with open('data.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([unique_ids[i], fio[2], fio[0], gen_phone(), fake_job()])
            # writer.writerow([unique_ids[i], fio[2], fio[0], fio[1], gen_phone(), gen_date(), fake_job(), fake_adr()])


if __name__ == '__main__':
    main()
