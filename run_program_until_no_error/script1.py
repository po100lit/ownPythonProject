from subprocess import run


def main():
    p = run('python script2.py')
    if p.returncode == 0:
        print('Программа завершена корректно')
    else:
        print('Программа завершена с ошибкой')
        main()


if __name__ == "__main__":
    main()
