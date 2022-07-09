import os

# Очистить окно терминала!!! (не консоли 'Run')

#1
clear = lambda: os.system('cls')  # В Linux 'cls' заменить на 'clear'
clear()

#2
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
