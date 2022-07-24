def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def main():
    print(is_prime(59))


if __name__ == "__main__":
    main()
