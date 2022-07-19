import random

number = random.randint(2, 100000000)


def is_prime(num: int) -> bool:  # проверка числа на простоту
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    return True


def get_all_divisors(num: int) -> list:  # поиск всех делителей числа
    all_divisors = []
    for i in range(2, int(num // 2 + 1)):
        if num % i == 0:
            all_divisors.append(i)
    return sorted(all_divisors)


def get_prime_divisors(num: int) -> list:  # поиск простых делителей числа
    prime_divisors = []
    for i in get_all_divisors(num):
        if is_prime(i):
            prime_divisors.append(i)
    return prime_divisors


def get_prime_multipliers(num: int) -> list:  # разложение числа на простые множители
    multipliers = []
    for i in get_prime_divisors(num):
        while num % i == 0:
            multipliers.append(i)
            num //= i
    return multipliers


def main():
    print(f'Исходное число: {number}')
    print(f'Все делители:', ', '.join(list(map(str, get_all_divisors(number)))))
    print(f'Простые делители:', ', '.join(list(map(str, get_prime_divisors(number)))))
    print(f'Простые множители:', ' * '.join(list(map(str, get_prime_multipliers(number)))), f'= {number}')


if __name__ == "__main__":
    main()