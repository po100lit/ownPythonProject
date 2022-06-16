print('Ищем натуральные числа "пифагоровой тройки" от 1 до...')
up_lim = int(input('Введите верхний предел поиска: '))
my_list = []  # текущий список для прохода по циклу
all_list = []  # итоговый список со значениями
count = 0  # счетчик повторяющихся значений
for i in range(1, up_lim + 1):
    a = i
    for i in range(1, up_lim + 1):
        b = i
        for i in range(1, up_lim + 1):
            c = i
            if a ** 2 + b ** 2 == c ** 2:
                my_list.append(a)
                my_list.append(b)
                my_list.append(c)
                my_list.sort()
                if my_list in all_list:
                    count += 1
                else:
                    all_list.append(list(my_list))
                my_list.clear()
print(*all_list, sep='\n')
print(f'найдено {len(all_list)}')
print(f'повторяющихся значений {count}')
