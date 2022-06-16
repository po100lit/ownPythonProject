from bs4 import BeautifulSoup as bs
import requests
import lxml
import csv
from art import tprint
from time import time

time_start = time()

tprint('PARSING', font='bulbhead')

host = 'https://www.kopchenyi.kz/'
url = 'https://www.kopchenyi.kz/product-category/kupaty/'
path = 'parse.csv'
csv_head = ('Наименование', 'Категория', 'Цена')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2) Gecko/20100115 Firefox/3.6 GTBDFff GTB7.0',
    'accept': '*/*'
}


# поиск количества страниц пагинации
# возвращаем список страниц с которых будем парсить ссылки
def find_pages():
    pages = []
    print('Поиск пагинации и количества страниц...')
    count = 1
    while True:
        pg_url = f'{url}page/{count}/'
        answer = requests.get(pg_url)
        if answer.status_code == 200:
            print(f'Найдена {count}-ая страница...')
            pages.append(pg_url)
        else:
            break
        count += 1
    print()
    print(f'Найдено {len(pages)} страниц пагинации.')
    return pages


# парсинг ссылок на товары с каждой страницы пагинации
# возвращаем список со ссылками на страницу товара
def parse_block():
    prod_links = []
    for page in find_pages():
        # print(page)
        req = requests.get(url=page, headers=headers)
        html = req.text
        soup = bs(html, 'lxml')
        prod_block = soup.select('li.product.type-product')
        for item in prod_block:
            href = item.find_all('a', href=True)
            for link in href:
                link = link.get('href')
                if 'kopchenyi.kz' in link:
                    prod_links.append(link)
    print(f'Найдено {len(prod_links)} товаров...')
    return prod_links


# парсим страницу товара
# возвращаем словарь
def parse_prod():
    data = []
    for item in parse_block():
        req = requests.get(url=item, headers=headers)
        html = req.text
        soup = bs(html, 'lxml')
        page = soup.find_all('div', class_='product')
        for goods in page:
            data.append(
                {
                    'title': goods.find('h1', class_='product_title').get_text(strip=True),
                    'category': goods.find('div', class_='product_meta').find('a').get_text(strip=True),
                    'price': goods.find('bdi').get_text(strip=True)
                }
            )
    # print(data)
    return data


# сохраняем полученные данные в CVS
def save_doc(goods, path):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(csv_head)
        for item in goods:
            writer.writerow([item['title'], item['category'], item['price']])


save_doc(parse_prod(), path)
time_end = time()
print()
print(f'Парсинг завершен за {int(time_end - time_start)} секунд.')
