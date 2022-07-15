def get_words():
    with open('DATA/words.txt', encoding='utf-8') as file:
        data = file.read()
    return data


def letters_stat():
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    stat_dict = {}
    # stat_string = get_words()
    # for letter in letters:
    #     stat_dict[letter] = stat_string.count(f'{letter}')
    # sort_by_quantity_high_low = sorted(stat_dict.items(), key=lambda x: x[1], reverse=True)
    # sort_by_quantity_low_high = sorted(stat_dict.items(), key=lambda x: x[1])
    # for i in range(10):
    #     print(sort_by_quantity_high_low[i])
    # print()
    # for i in range(10):
    #     print(sort_by_quantity_low_high[i])
    # max_word_length = 0
    # for i in get_words().split(','):
    #     max_word_length = max(max_word_length, len(i))
    # print(max_word_length)
    stat_list = get_words().split(',')
    for letter in letters:
        k = 0
        for word in stat_list:
            if word.startswith(letter):
                k += 1
        stat_dict[letter] = k
    print(sorted(stat_dict.items(), key=lambda x: x[1]))


def main():
    letters_stat()


if __name__ == "__main__":
    main()
