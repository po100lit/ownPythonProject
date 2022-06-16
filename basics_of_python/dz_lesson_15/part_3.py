# Напишите функцию которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней чисел (если число положительное)
# и самих чисел (если число отрицательное) и возвращает результат
# (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться.
import math

old_list = [5, -3, 10, -7]

# без тенарного оператора возвращяются только корни положительных чисел
def new_list(input_list):
    result = [round(math.sqrt(number), 2) for number in input_list if number > 0]
    return result

# # с тенарным оператором отрицательные числа попадают в список без изменений
# def new_list(input_list):
#     result = [round(math.sqrt(number), 2) if number >0 else number for number in input_list]
#     return result

result = new_list(old_list)
print(result)
print(old_list)
