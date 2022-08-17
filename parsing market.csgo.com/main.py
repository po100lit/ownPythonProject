import csv
import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import re

host = 'https://market.csgo.com'
headers = {
    "User - Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML,"
                    " like Gecko) Chrome / 102.0.5005.167 YaBrowser / 22.7.3.822 Yowser / 2.5 Safari / 537.36",
    "Accept": "application / json, text / javascript, * / *; q = 0.01"
}
error_count = 0


def save_links():
    global error_count
    response = requests.get(url=host, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    last_page = int(soup.find('div', class_='page-counter').find('span', id='total_pages').get_text())
    print(f'[INFO] Total pages found: {last_page}')
    links = []
    for page in tqdm(range(last_page), ncols=100, unit=' page'):
        url = host + f'?s=price&p={page}&sd=desc'
        resp = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        try:
            res = soup.find('div', class_='market-items').find_all('a', class_='item')
        except:
            error_count += 1
        for i in res:
            links.append(host + i.get('href'))
    with open('links.txt', 'w', encoding='utf-8') as file:
        for i in set(links):
            file.write(i + '\n')


def collect_info(filename):
    global error_count
    all_data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for i in file:
            all_data.append(i.strip())
    print(f'[INFO] Total links found: {len(all_data)}')
    result = {}
    for item in tqdm(all_data, ncols=100, unit=' item'):
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
            best_price = "Price found"
            error_count += 1
        # Описание
        try:
            d_description = str(soup.find('div', id='descr').find_all('p')[2:]).replace('> <', '><').replace(',', '')
            clear_html = re.compile('<.*?>')
            c_description = re.sub(clear_html, '', d_description) \
                .replace('   ', ' ').replace('  ', '').strip().replace('[', '').replace(']', '')
        except:
            c_description = "Description found"
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
    print(f'{len(all_data)} items was parsed')
    print(f'Parse errors {error_count}')
    return result


def save_data(dictionary):
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(dictionary, file, indent=4, ensure_ascii=False)
    with open('data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for k, v in dictionary.items():
            writer.writerow((k, v['Title'], v['Status'], v['Type'],
                             v['Tags'], v['Best price'], v['Description'], v['Image']))


def main():
    save_links()
    tmp_dict = collect_info('links.txt')
    save_data(tmp_dict)


if __name__ == '__main__':
    main()
