def convert_type_input(input_string: str) -> [int, float, str]:
    try:
        return int(input_string)
    except ValueError:
        try:
            return float(input_string)
        except ValueError:
            return input_string


def main():
    lst = list(map(lambda x: convert_type_input(x), input('Enter symbols with whitespace as separator: ').split()))
    for item in lst:
        print(type(item), item)
    print(lst)


if __name__ == '__main__':
    main()