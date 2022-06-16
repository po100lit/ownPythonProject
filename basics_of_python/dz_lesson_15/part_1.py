# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

list_1 = ['яблоко', 'апельсин', 'морковь', 'дыня', 'картошка']
list_2 = ['вишня', 'апельсин', 'свекла', 'арбуз', 'картошка']

# классический способ через цикл
res_list = []

for item in list_1:
    if item in list_2:
        res_list.append(item)

print(res_list)

# через генератор
res_list = []
res_list = [item for item in list_1 if item in list_2]

print(res_list)
