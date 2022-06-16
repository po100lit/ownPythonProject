# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def max_number(a, b, c):
    result = max([a, b, c])
    return result


result = max_number(1, 3, 5)
print(result)

result = max_number(7, 11, 3)
print(result)
