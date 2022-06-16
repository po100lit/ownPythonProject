import sys
from core import create_file, create_dir, get_list, get_dir, del_item, save_info, copy_item
from game import game
from game_rev import game_rev

save_info('Start')

try:
    command = sys.argv[1]
except IndexError:
    print('Введите команду. \nДля вывода списка команд наберите help')
else:
    if command == 'list_all':
        get_list()
    elif command == 'list_d':
        get_dir(True)
    elif command == 'mk_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Введите имя файла')
        else:
            create_file(name)
    elif command == 'mk_dir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Введите имя папки')
        else:
            create_dir(name)
    elif command == 'del':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Введите имя файла/папки')
        else:
            del_item(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Введите начальное и конечное имя файла/папки')
        else:
            copy_item(name, new_name)
    elif command == 'help':
        print('list_all - показать содержимое текущей папки')
        print('list_d - показать папки в текущей папке')
        print('mk_file - создать файл')
        print('mk_dir - создать папку')
        print('del - удалить файл или папку')
        print('copy - копировать файл или папку')
        print('game1 - пользователь угадывает число, задуманное компьютером')
        print('game2 - компьютер угадывает число, задуманное пользователем')
    elif command == 'game1':
        game()
    elif command == 'game2':
        game_rev()

save_info('End')
