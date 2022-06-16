# Нахождение индексов максимального и минимального элемента массива

array = [3, 5, 2, 4, 1]
print(f'input array: {array}')
i = 0
n = len(array)
max_i = i
min_i = i
max_value = array[i]
min_value = array[i]

while i < n:
    if array[i] < min_value:
        min_value = array[i]
        min_i = i
    elif array[i] > max_value:
        max_value = array[i]
        max_i = i
    i = i + 1

print(f'min value: {min_value}, min_index: {min_i}\nmax value: {max_value}, max_index: {max_i}')
