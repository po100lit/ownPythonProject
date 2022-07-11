import string

input_number = int(input('Enter number: '))


def decimal_converter():
    number_to_letter = string.digits + string.ascii_uppercase
    for i in range(2, 37):
        x = input_number
        result_number = ''
        while x > 0:
            result_number += number_to_letter[x % i]
            x //= i
        print(f'{input_number}: 10 --> {i} = {result_number[::-1]}')


def main():
    decimal_converter()


if __name__ == '__main__':
    main()
