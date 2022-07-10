def main():
    a = 10
    b = 50
    big = (a + b) / 2 + abs(a - b) / 2
    low = (a + b) / 2 - abs(a - b) / 2
    print(big, low)
    print('max = ', (a, b)[a < b])
    print('min = ', (a, b)[a > b])
    print('max = ', (a < b) * b + (a > b) * a)
    print('min = ', (a < b) * a + (a > b) * b)


if __name__ == "__main__":
    main()
