# компьютер угадывает число, загаданное человеком

import random

up_lim = 100
dn_lim = 0
count = 0
check = None

while check != "=":
    count += 1
    num = int(random.randint(dn_lim, up_lim))
    print(f'ваше число в диапазоне {dn_lim} - {up_lim}')
    print(f'{num} < меньше, > больше или = равно загаданному вами? ')
    check = input()
    if check == '>':
        up_lim = num - 1
    else:
        dn_lim = num + 1

print(f'ИИ угадал число {num} с {count} попыток')
