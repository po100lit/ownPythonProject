from bs4 import BeautifulSoup
import requests
import csv

# имя файла, в который сохранятся данные
CSV = 'parse.csv'
# начальный домен для подстановки в адреса ссылок и картинок, / в конце, как правило, не нужен
HOST = 'https://kz.wildberries.ru'
# начальный адрес для парсинга
URL = 'https://kz.wildberries.ru/catalog/muzhchinam/dlya-vysokih'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/98.0.4758.119 YaBrowser/22.3.0.2434 Yowser/2.5 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
              'q=0.8,application/signed-exchange;v=b3;q=0.9'
}


# получаем исходный код страницы
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


# извлекаем необходимые данные со страницы
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-card')  # карточка для парсера
    data = []
    for item in items:
        data.append(
            {
                'title': item.find('div', class_='product-card__brand-name').find('span', class_='goods-name').get_text(
                    strip=True),
                'brand': item.find('div', class_='product-card__brand-name').find('strong').get_text(strip=True),
                'image': 'https:' + item.find('div', class_='product-card__img-wrap').find('img').get('src'),
                'link': HOST + item.find('div', class_='product-card__wrapper').find('a').get('href'),
                'price': item.find('div', class_='product-card__price').find('span', class_='price').get_text(
                    strip=True)
            }
        )
        # print(data)
    return data


def save_doc(items, path):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Наименование', 'Цена', 'Производитель', 'Картинка', 'Ссылка'])
        for item in items:
            writer.writerow([item['title'], item['price'], item['brand'], item['image'], item['link']])


def parser():
    pagination = int(input('Введите количество страниц для парсинга: '))
    html = get_html(URL)
    if html.status_code == 200:
        data = []
        for page in range(1, pagination + 1):
            print(f'Парсим страницу {page}')
            html = get_html(URL, params={'page': page})
            data.extend(get_content(html.text))
            save_doc(data, CSV)
            # print(html.url)
        print('Парсинг закончен')
    else:
        print('HOST Error')


parser()

# Источник https://youtu.be/ykjBVT57r68
