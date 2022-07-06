def main():
    a = 10
    b = 50
    big = (a + b) / 2 + abs(a - b) / 2
    low = (a + b) / 2 - abs(a - b) / 2
    print(big, low)


if __name__ == "__main__":
    main()
