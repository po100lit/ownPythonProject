# Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.

numbers = [2, 2, 5, 12, 8, 2, 12, 7]

result = []

for number in numbers:
    if numbers.count(number) == 1:
        result.append(number)

print(result)
print(type(result))
