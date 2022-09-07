import csv
import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import re


def get_data():
    error_count = 0
    host = 'https://market.csgo.com'
    headers = {
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML,"
                        " like Gecko) Chrome / 102.0.5005.167 YaBrowser / 22.7.3.822 Yowser / 2.5 Safari / 537.36"
    }

    response = requests.get(url=host, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    last_page = int(soup.find('div', class_='page-counter').find('span', id='total_pages').get_text())
    print(f'[INFO] Total pages found: {last_page}')
    links = []
    for page in tqdm(range(last_page), ncols=100, unit=' page', desc='Page parsing'):
        url = host + f'?s=price&p={page}&sd=desc'

        resp = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')

        try:
            res = soup.find('div', class_='market-items').find_all('a', class_='item')
        except:
            error_count += 1

        for i in res:
            links.append(host + i.get('href'))

    result = {}

    for item in tqdm(links, ncols=100, unit=' item', desc='Item parsing'):
        resp = requests.get(url=item, headers=headers)
        goods_id = '-'.join(item.split('/')[4].split('-', maxsplit=2)[:2])
        soup = BeautifulSoup(resp.text, 'lxml')
        try:
            title = soup.find('h1').get_text().strip()  # Название предмета
        except:
            title = "Title not found"
            error_count += 1
        try:  # Статус предмета
            status = soup.find_all('div', class_='item-appearance')[0].get_text().strip()
        except:
            status = 'Status not defined'
            error_count += 1
        try:  # Тип предмета
            type = soup.find_all('div', class_='item-appearance')[1].get_text().strip()
        except:
            type = 'Type not defined'
            error_count += 1
        try:  # Теги предмета
            tags = [soup.find_all('div', class_='item-tag')[0].get_text(),
                    soup.find_all('div', class_='item-tag')[1].get_text()]
        except:
            tags = 'Tags not defined'
            error_count += 1
        # Лучшая цена
        try:
            best_price = soup.find('div', class_='ip-bestprice').get_text().strip().replace(' ', '')
        except:
            best_price = "Price not found"
            error_count += 1
        # Описание
        try:
            d_description = str(soup.find('div', id='descr').find_all('p')[2:]).replace('> <', '><').replace(',', '')
            clear_html = re.compile('<.*?>')
            c_description = re.sub(clear_html, '', d_description).strip()
            c_description = ' '.join(c_description.split()).replace('\n', ' ').replace('[', '').replace(']', '').strip()
        except:
            c_description = "Description not found"
            error_count += 1
        # Картинка
        try:
            img = soup.find('div', class_='ip-pic').find('img').get('src')
        except:
            img = 'Image not found'
            error_count += 1
        result[goods_id] = {
            'Title': title,
            'Status': status,
            'Type': type,
            'Tags': tags,
            'Best price': best_price,
            'Description': c_description,
            'Image': img
        }

    print(f'Parsing errors: {error_count}')

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    with open('data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['ID','Title', 'Status', 'Type', 'Tags', 'Best price', 'Description', 'Image'])
        for k, v in result.items():
            writer.writerow((k, v['Title'], v['Status'], v['Type'],
                             v['Tags'], v['Best price'], v['Description'], v['Image']))


def main():
    get_data()


if __name__ == '__main__':
    main()
