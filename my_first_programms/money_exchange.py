# найдите количество способов разменять N {денег} монетами по 1, 2, 5, 10, 25, 50 {монет}

def get_ways(n, coins):
    ways = [0 for i in range(n + 1)]
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(len(ways)):
            if coins[i] <= j:
                ways[j] += ways[j - coins[i]]
    return ways[n]


def main():
    money = int(input('Введите исходную сумму: '))
    coins = [1, 2, 5, 10, 25, 50]
    print(get_ways(money, coins))


if __name__ == "__main__":
    main()
