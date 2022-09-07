import qrcode
import csv
from tqdm import tqdm


def main():
    links = []
    count = 1
    with open('links.csv', 'r', encoding='utf-8') as file:
        all_links = csv.reader(file)
        for i in all_links:
            links.append(''.join(i))
    for link in tqdm(links, ncols=100):
        data = link  # пример данных
        filename = f"data_png/{count}.png"  # имя конечного файла
        img = qrcode.make(data, box_size=40, border=4)  # генерируем qr-код
        img.save(filename)  # сохраняем img в файл
        count += 1


if __name__ == '__main__':
    main()
