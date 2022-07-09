# Вывод данных в консоль разными цветами

---

## Встроенными средствами

`print("\033[4m \033[37m \033[44m {} \033[0m".format("Text"))`

Синтаксис данной строки (пробелы для наглядности):

> \033 - общий признак того, что дальше идет какой-то управляющий цветом код
> 
> \033[4m — подчёркнутый
> 
> \033[37m — белая надпись
> 
> \033[44m — синий фон
> 
> {} — заменится на "Text"
> 
> \033[0m — сброс к начальным значениям

### Цвета
| Цвет       | Текст | Фон |
|------------|-------|-----|
| Чёрный     | 30    | 40  |
| Красный    | 31    | 41  |
| Зелёный    | 32    | 42  |
| Жёлтый     | 33    | 43  |
| Синий      | 34    | 44  |
| Фиолетовый | 35    | 45  |
| Бирюзовый  | 36    | 46  |
| Белый      | 37    | 47  |

### Эффекты
| Код | Значение                         |
|-----|----------------------------------|
| 0   | Сброс к начальным значениям      |
| 1   | Жирный                           |
| 2   | Блёклый                          |
| 3   | Курсив                           |
| 4   | Подчёркнутый                     |
| 5   | Редкое мигание                   |
| 6   | Частое мигание                   |
| 7   | Смена цвета фона с цветом текста |

---

## Библиотека colorama

Перед использованием библиотеки colorama, её следует установить

`pip install colorama`

```commandline
from colorama import Fore, Back, Style

colorama.init()

print(Fore.RED + "Красный текст")
print(Back.BLUE + "Синий фон")
print(Style.RESET_ALL)
print("Снова обычный текст")
```

`Fore.RED` - меняет цвет текста

`Back.BLUE` - меняет цвет фона

`Style.RESET_ALL` - сброс к начальным настройкам цветов

**Available formatting constants are:**

- **Fore**: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
- **Back**: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
- **Style**: DIM, NORMAL, BRIGHT, RESET_ALL

**These are fairly well supported, but not part of the standard:**

- **Fore**: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX
- **Back**: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX

---

## Библиотека termcolor

Перед использованием библиотеки colorama, её следует установить

`pip install termcolor`

```commandline
from termcolor import colored, cprint

print(colored('Привет мир!', 'red', attrs=['underline']))
print('Привет, я люблю тебя!')
cprint('Вывод с помощью cprint', 'green', 'on_blue')
```

Используем функции colored и cprint.

Первая позволяет создать строку для последующего вывода с необходимыми параметрами цветов и эффектов.

Вторая сразу производит вывод в консоль.

**Available text colors:**

- grey
- red
- green
- yellow
- blue
- magenta
- cyan
- white

**Available text highlights:**

- on_grey
- on_red
- on_green
- on_yellow
- on_blue
- on_magenta
- on_cyan
- on_white

**Available attributes:**

- bold
- dark
- underline
- blink
- reverse
- concealed