import requests
from bs4 import BeautifulSoup
import csv
import time


start_time = time.time()
url = 'https://habr.com/ru/company/yandex/blog/'
host = 'https://habr.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
error_count = 0
total_pages_count = 0
with open('habr.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Дата', 'Название', 'Ссылка', 'Краткое содержание'])


def get_pagination():
    """Находим номер последней страницы пагинации"""
    request = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(request.text, 'lxml')
    last_pgn_page = int(
        soup.find('div', class_='tm-pagination').findAll('a', class_='tm-pagination__page')[-1].get_text().strip())
    return last_pgn_page


def collect_pages():
    """Собираем страницы для парсинга"""
    list_pages = []
    for i in range(1, get_pagination() + 1):
        list_pages.append(f'{url}page{i}')
    return list_pages


def collect_links():
    """Парсим страницы"""
    page_count = 0
    global error_count
    global total_pages_count
    for page in collect_pages():
        request = requests.get(url=page, headers=headers)
        soup = BeautifulSoup(request.text, 'lxml')
        articles_links = soup.findAll('a', class_='tm-article-snippet__title-link')
        for link in articles_links:
            pub_link = str(host + link.get('href'))
            r = requests.get(url=pub_link, headers=headers)
            soup = BeautifulSoup(r.text, 'lxml')
            pub_date = soup.find('span', class_='tm-article-snippet__datetime-published').find('time').get('datetime').split('T')[0]
            pub_title = soup.find('h1', class_='tm-article-snippet__title_h1').get_text().strip().replace('&nbsp;', ' ')
            try:
                pub_content = soup.find('div', class_='article-formatted-body_version-1').get_text().strip().replace('&nbsp;', ' ')[:200]
                total_pages_count += 1
            except Exception as ex:
                pub_content = f'[X] - ошибка парсинга {ex}'
                error_count += 1
            with open('habr.csv', 'a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow([pub_date, pub_title, pub_link, pub_content])
        page_count += 1
        print(f'[i] Страница {page_count} обработана...')


def main():
    collect_links()
    print()
    print(f'[✓] Парсинг закончен. Получены данные с {total_pages_count} статей.')
    print(f'[!] Ошибок парсинга {error_count}')
    print(f'Затрачено времени: {round(((time.time() - start_time)/60), 2)} минут.')


if __name__ == "__main__":
    main()
