print('переводим неправильную дробь в правильную:')
a = 0
b = 0
while a <= 0:
    a = int(input('Введите числитель больше нуля: '))
while b <= 0:
    b = int(input('Введите знаменатель больше нуля: '))
c = a // b
if a % b != 0 and a > b:
    print(f'{a}/{b} = {c} {a - b * c}/{b}')
elif a < b:
    print(f'дробь {a}/{b} - правильная')
elif a % b == 0:
    print(f'дробь {a}/{b} - это целое число {int(a / b)}')
