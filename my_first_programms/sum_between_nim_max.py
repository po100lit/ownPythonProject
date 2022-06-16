# Найти сумму элементов массива, лежащих между максимальным и
# минимальным по значению элементами

array = [3, 6, 2, 3, 4, 1, 5]
print(f'input array: {array}')
i = 0
n = len(array)
max_i = i
min_i = i
max_value = array[i]
min_value = array[i]
summ = 0

while i < n:
    if array[i] < min_value:
        min_value = array[i]
        min_i = i
    elif array[i] > max_value:
        max_value = array[i]
        max_i = i
    i = i + 1

print(f'min value: {min_value}, min_index: {min_i}\nmax value: {max_value}, max_index: {max_i}')

if min_i < max_i-1:
    while min_i < max_i-1:
        summ += array[min_i + 1]
        min_i += 1
elif max_i < min_i-1:
    while max_i < min_i-1:
        summ += array[max_i + 1]
        max_i += 1
print(summ)