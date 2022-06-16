from bs4 import BeautifulSoup
import requests
import csv
import lxml

# имя файла, в который сохранятся данные
CSV = 'parse.csv'
# начальный домен для подстановки в адреса ссылок и картинок, / в конце, как правило, не нужен
HOST = 'https://www.kizlyar-shop.ru/'
# начальный адрес для парсинга
URL = 'https://www.kizlyar-shop.ru/catalog/authors/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 '
                  'YaBrowser/22.3.0.2434 Yowser/2.5 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
              'q=0.8,application/signed-exchange;v=b3;q=0.9'
}


# получаем исходный код страницы
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


# извлекаем необходимые данные со страницы
def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='posts__item')  # карточка для парсера
    data = []
    for item in items:
        data.append(
            {
                'title': item.find('div', class_='item-title').get_text(strip=True),
                'price': item.find('div', class_='price').get_text(strip=True),
                'image': HOST + item.find('div', class_='stickers').find('img').get('src'),
                'link': HOST + item.find('a', class_='thumb').get('href')
            }
        )
    return data


def save_doc(items, path):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Цена', 'Картинка', 'Ссылка'])
        for item in items:
            writer.writerow([item['title'], item['price'], item['image'], item['link']])


def parser():
    pagenation = int(input('Введите количество страниц для парсинга: '))
    html = get_html(URL)
    if html.status_code == 200:
        data = []
        for page in range(1, pagenation + 1):
            print(f'Парсим страницу {page}')
            params = str({'PAGEN_1=': page})
            html = get_html(URL, params=params)
            data.extend(get_content(html.text))
            save_doc(data, CSV)
            print(html.url)
        if len(data) == 0:
            print(f'Ой, что-то пошло не так. Данных получено {len(data)}.')
        else:
            print(f'Парсинг закончен. Данных получено {len(data)}.')
    else:
        print('HOST Error')


parser()

# Источник https://youtu.be/ykjBVT57r68

# 'image': HOST+item.find('div', class_='posts__inner').find('a').find('img').get('src')
# ищем тег 'div' с нужным классом, в нём тег 'a', в нём тег 'img' и извлекаем 'src'
