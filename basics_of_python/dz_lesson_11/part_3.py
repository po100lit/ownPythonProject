# Создайте модуль ???.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в ???.py всех функций.
# Вызовите каждую функцию в ???.py и проверьте что все работает как надо.

from part_1 import create_folders
from part_1 import del_folders
import part_2

create_folders()
del_folders()

print(part_2.get_random([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(part_2.get_random([]))