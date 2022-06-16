# перевернуть массив и записать его в обратном порядке

array = [5, 3, 2, 4, 1]
print(f'input array:  {array}')
i = 0
n = len(array)

while n - i > 0:
    temp = array[i]
    array[i] = array[n - 1]
    array[n - 1] = temp
    i = i + 1
    n = n - 1

print(f'output array: {array}')
