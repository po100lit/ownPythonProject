# поиск пары чисел в массиве, в сумме дающие заданное число

my_list = [-3, 0, 1, 3, 4, 5, 8]
k = 7

# 1 способ
# for i in range(0, len(my_list)):
#     for j in range((i + 1), len(my_list)):
#         if my_list[i] + my_list[j] == k:
#             print(my_list[i], my_list[j])

# 2 способ
# new_list = []
# for i in range(0, len(my_list)):
#     num_to_find = k - my_list[i]
#     if num_to_find in new_list:
#         print(num_to_find, my_list[i])
#     else:
#         new_list.append(my_list[i])

# 3 способ
# for i in range(0, len(my_list)):
#     num_to_find = k - my_list[i]
#     l = i + 1
#     r = len(my_list) - 1
#     while l <= r:
#         mid = int(l + (r - l) / 2)
#         if my_list[mid] == num_to_find:
#             print(my_list[i], my_list[mid])
#         if num_to_find < my_list[mid]:
#             r = mid - 1
#         else:
#             l = mid + 1

# 4 способ
l = 0
r = len(my_list) - 1
while l < r:
    summ = my_list[l] + my_list[r]
    if summ == k:
        print(my_list[l], my_list[r])
    if summ < k:
        l += 1
    else:
        r -= 1
