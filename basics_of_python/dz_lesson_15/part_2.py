# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# Элемент кратен 3,
# Элемент положительный,
# Элемент не кратен 4.

numbers = [2, 5, 36, 0, -7, 18, -12, 11, -28, 30, -24]

# условия по одельности
result = [number for number in numbers if number %3 == 0]
print(result)
result = [number for number in numbers if number > 0]
print(result)
result = [number for number in numbers if number %4 != 0]
print(result)

# все условия вместе
result = [number for number in numbers if number %3 == 0 and number > 0 and number %4 != 0]
print(result)
