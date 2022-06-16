import random

words_bank = ['автострада', 'бензин', 'инопланетянин',
              'самолет', 'библиотека',
              'шайба', 'олимпиада']

secret_word = random.choice(words_bank)
# print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

errors_cnt = 0

while True:
    letter = input('введите ОДНУ русскую букву: ').lower()
    if len(letter) != 1:
        continue

    if letter in secret_word:
        for idx, symbol in enumerate(secret_word):
            if symbol == letter:
                gamer_word[idx] = letter
        if '*' not in gamer_word:
            print('вы выиграли')
            break
    else:
        errors_cnt += 1
        print('ошибок допущено:', errors_cnt)
        if errors_cnt == len(secret_word) + 2:
            print('вы проиграли')
            break

    print(''.join(gamer_word))
