import json

from bs4 import BeautifulSoup
import requests
import csv

host = 'https://www.technodom.kz'
url = 'https://www.technodom.kz/catalog/tv-audio-foto-video/televizory/led-televizory'
file_name = 'parse.csv'
csv_head = ('Наименование', 'Цена', 'Ссылка')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2) Gecko/20100115 Firefox/3.6 GTBDFff GTB7.0',
    'accept': '*/*'
}


def find_pages():
    pages = []
    print('Поиск пагинации...\n')
    answer = requests.get(url=url, headers=headers)
    html = answer.text
    soup = BeautifulSoup(html, 'lxml')
    found_pages = soup.find('div', class_='Paginator__List').find_all('p', class_='Typography')
    if 5 <= len(found_pages) < 10:
        found_pages = soup.find('div', class_='Paginator__List').find_all('a').__getitem__(-1)
        str_page = str(found_pages)
        str_page = str_page.split('=')
        str_page = str(str_page[2])
        count = int(str_page[0])
    elif len(found_pages) >= 10:
        found_pages = soup.find('div', class_='Paginator__List').find_all('a').__getitem__(-1)
        str_page = str(found_pages)
        str_page = str_page.split('=')
        str_page = str(str_page[2])
        count = int(str_page[0] + str_page[1])
    else:
        count = len(found_pages)
    for i in range(1, count + 1):
        page_url = f'{url}?page={i}'
        print(f'Найдена {i}-ая страница...')
        pages.append(page_url)
    print()
    print(f'Создан список из {len(pages)} страниц')
    return pages


def parse_links():
    data_links = []
    for page in find_pages():
        req = requests.get(url=page, headers=headers)
        html = req.text
        soup = BeautifulSoup(html, 'lxml')
        product_block = soup.select('li.category-page-list__item')
        for item in product_block:
            href = item.find_all('a', href=True)
            for link in href:
                link = host + link.get('href')
                data_links.append(link)
    print()
    print(f'Найдено {len(data_links)} товара...')
    return data_links


def get_parse():
    product_data = []
    for link in parse_links():
        req = requests.get(url=link, headers=headers)
        html = req.text
        soup = BeautifulSoup(html, 'lxml')
        goods = soup.find_all('div', class_='product__info')
        for item in goods:
            product_data.append(
                {
                    'title': item.find('h1', class_='Typography').get_text(strip=True),
                    'price': item.find('div', class_='product-info__prices product-prices').get_text(
                        strip=True).replace('\xa0', '').rstrip('₸').split('₸'),
                    'link': link
                }
            )
    return product_data


def save_csv(goods, file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(csv_head)
        for item in goods:
            writer.writerow([item['title'], item['price'], item['link']])
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(goods, file, indent=4, ensure_ascii=False)


save_csv(get_parse(), file_name)
print()
print(f'Парсинг завершен!')
