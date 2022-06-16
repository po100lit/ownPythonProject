import requests
from bs4 import BeautifulSoup
# import collections
import csv

# последовательность столбцов задаётся здесь
# ParseResult = collections.namedtuple('ParseResult', ('art', 'price', 'goods_name', 'url', 'image'))

host = 'https://shop.kz'
url = 'https://shop.kz/videokarty/videokarty-dlya-igr/'
csv_head = ('Артикул', 'Цена', 'Товар', 'Ссылка', 'Картинка')  # первая строка CSV
path = 'links.csv'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2) Gecko/20100115 Firefox/3.6 GTBDFff GTB7.0',
    'accept': '*/*'
}
products = []

pagination = int(input('Введите количество страниц для парсинга: '))
for i in range(1, pagination + 1):
    print(f'Парсим {i} страницу...')
    url = f'https://shop.kz/videokarty/videokarty-dlya-igr/?PAGEN_1={i}'
    req = requests.get(url=url, headers=headers)
    html = req.text

    soup = BeautifulSoup(html, 'lxml')
    product_block = soup.select('div.bx_catalog_item_title')
    articul = soup.select('div.bx_catalog_item_XML_articul')

    for i in product_block:
        href = i.find_all('a', href=True)
        for link in href:
            link = host + link.get('href')
            products.append(link)


# clear_products = list(set(products))
# print(f'количество элементов после очистки {len(clear_products)}: {len(products)}/2')

with open(path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';', lineterminator='\r')
    # for item in clear_products:
    for item in products:
        writer.writerow([item])

# print(f'Парсинг ссылок с {pagination} страниц завершен. Ссылок получено {len(clear_products)}. Смотри файл {path}')
print(f'Парсинг ссылок с {pagination} страниц завершен. Ссылок получено {len(products)}. Смотри файл {path}')
