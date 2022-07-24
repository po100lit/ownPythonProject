def find_scm(num1: int, num2: int) -> int:
    """
    Принимаем за НОК наименьшее число и увеличиваем его на единицу до тех пор,
    пока полученное число не будет делиться на оба введённых числа без остатка

    :param num1: first number as int
    :param num2: second number as int
    :return: smallest common multiple as int
    """
    scm = min(num1, num2)
    while True:
        if scm % num1 == 0 and scm % num2 == 0:
            break
        scm += 1
    return scm


#
def find_gcd(num1: int, num2: int) -> int:
    """
    Так как одно из чисел всегда становится равным нулю, то функция всегда будет возвращать делитель,
    благодаря логическому оператору или, который используется вместе с return.

    :param num1: first number as int
    :param num2: second number as int
    :return: greatest common divisor as int
    """
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def main():
    print(find_scm(22, 6))
    print(find_gcd(96, 144))


if __name__ == "__main__":
    main()

