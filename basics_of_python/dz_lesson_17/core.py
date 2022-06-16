import os
import shutil
import datetime


# создаем файл
def create_file(filename, text=None):
    with open(filename, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# создаем папку
def create_dir(dirname):
    try:
        os.mkdir(dirname)
    except FileExistsError:
        print('Данная папка уже существует')


# вывод содержимого папки
def get_list():
    print(os.listdir())


# вывод только папок
def get_dir(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# удаление файла/папки
def del_item(itemname):
    if os.path.isdir(itemname):  # проверяем что объект папка
        os.rmdir(itemname)
    else:
        os.remove(itemname)


# копирование файла/папки
def copy_item(itemname, new_name):
    if os.path.isdir(itemname):  # проверяем что объект папка
        try:
            shutil.copytree(itemname, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(itemname, new_name)


# сохранияем логи
def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


if __name__ == '__main__':
    create_file('text.dat', 'Some text')
    create_dir('NewDir')
    get_list()
    get_dir(True)
    del_item('NewDir')
    del_item('text.dat')
    save_info('message')
