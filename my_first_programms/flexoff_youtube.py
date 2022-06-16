my_list = []
# check_list = []
abs_list = []

while True:
    my_num = int(input('введите ставку: '))
    if my_num != 0:
        my_list.append(my_num)
    else:
        break

check_num = int(input('введите эталон: '))

for i in range(0, len(my_list)):
    # check_list.append(my_list[i] - check_num)
    abs_list.append(abs(my_list[i] - check_num))

# print('список ставок участников: ', my_list)
# print('список разниц ставок с эталоном: ', check_list)
# print('список модулей разниц: ', abs_list)
# print('минимальное значение модуля, оно же ближайшее к эталону: ', min(abs_list))
print('выиграла ставка: ', my_list[abs_list.index(min(abs_list))])
