# Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
import random


def get_random(input_list):
    if input_list:
        result = random.choice(input_list)
        return result
# код будет отрабатывать возврат None и без этого условия
    # else:
    #     return None

# запрещаем дублирование работы функции, если модуль импортирован
if __name__ == '__main__':
    print(get_random([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(get_random([]))
