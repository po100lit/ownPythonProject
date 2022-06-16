# компьютер загадывает число, пользователь пытается его угадать
# добавлены уровни сложности и многопользовательская версия

import random
def game():
    x_num = random.randint(0, 100)
    # print(x_num) # комп загадал число

    u_num = None
    count = 0
    hard_levels = {1: 10, 2: 5, 3: 3}
    level = int(input('Выберите уровень сложности от 1 до 3: '))
    max_count = hard_levels[level]

    user_count = int(input('Количество игроков: '))
    users= []
    for i in range(user_count):
        user_name = input(f'Введите пользователя {i+1}: ')
        users.append(user_name)
    print(users)

    is_winner = False
    winner_name = None

    while not is_winner:
        count += 1
        if count > max_count:
            print('LOOSER')
            break
        print(f'Попытка № {count}')
        for user in users:
            print(f'Ход игрока {user}')
            u_num = int(input('Введите число: '))  # пользователь ввел число
            if u_num == x_num:
                is_winner = True
                winner_name = user
                break
            elif u_num < x_num:
                print('надо больше')
            else:
                print('надо меньше')
    else:
        print(f'победа игрока {winner_name}')

if __name__ == '__main__':
    game()