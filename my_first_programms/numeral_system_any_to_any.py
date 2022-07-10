import string

possible_symbols = string.digits + string.ascii_uppercase


def numeral_system(number, from_ns, to_ns):
    '''
    Перевод числа из системы счисления [2-36] в систему счисления [2-36]
    :param number: number to convert - must be a string
    :param from_ns: input numeral system - must ba an integer
    :param to_ns: output numeral system - must ba an integer
    :return: number as string
    '''
    if to_ns == 10:
        return int(number, from_ns)
    elif from_ns == 10 and to_ns == 2:
        return bin(int(number))[2:]
    elif from_ns == 10 and to_ns == 8:
        return oct(int(number))[2:]
    elif from_ns == 10 and to_ns == 16:
        return hex(int(number))[2:]
    else:
        result = ''
        number = int(number, from_ns)
        while number > 0:
            result += possible_symbols[number % to_ns]
            number //= to_ns
        return result[::-1]


def main():
    print(numeral_system('101', 3, 8))


if __name__ == "__main__":
    main()
