import sys
from basics_of_python.dz_lesson_17.core import get_list, get_dir

command = sys.argv[1]

if command == 'list_all':
    get_list()
elif command == 'list_d':
    get_dir(True)
elif command == 'mk_file':
    pass
elif command == 'mk_dir':
    pass
elif command == 'del':
    pass
elif command == 'copy':
    pass
elif command == 'help' or '/?' or '?':
    print('Помощь')
