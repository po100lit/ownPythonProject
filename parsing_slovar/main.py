import requests
from bs4 import BeautifulSoup
import os.path
import time

host = 'https://wordsonline.ru'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.5005.134 YaBrowser/22.7.0.1842 Yowser/2.5 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9 '
}
words_set = set()


def get_index_page():
    url = 'https://wordsonline.ru/dicts/orthography.html'
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        if os.path.exists('HTML/index.html') and os.path.getsize('HTML/index.html') > 100:
            with open('HTML/index.html', 'r', encoding='utf-8') as file:
                index_html = file.read()
        else:
            with open('HTML/index.html', 'w', encoding='utf-8') as file:
                index_html = file.write(r.text)
    else:
        print(f'Check connection, URL or site availability. Response {r.status_code}')
        with open('HTML/index.html', 'w', encoding='utf-8') as file:
            index_html = file.write(f'Error {r.status_code}')
    return index_html


def get_alphabet_pages():
    alphabet_links = []
    html_text = get_index_page()
    soup = BeautifulSoup(html_text, 'lxml')
    res = soup.find('div', class_='alphabet').find_all('a')
    for i in res:
        alphabet_links.append(host + i.get('href'))
    return alphabet_links


def get_pagination(url):
    pass


def get_words():
    links = get_alphabet_pages()
    for i in links:
        # TODO: пройтись по пагинации
        r = requests.get(url=i, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        words = soup.find('ul', class_='list-unstyled').findAll('li')
        for word in words:
            words_set.add(word.text)
        time.sleep(0.5)
        print(f'Scrapping page {i[-1]}')
    print(words_set)
    print(len(words_set))


def main():
    get_words()


if __name__ == '__main__':
    main()
