import requests
from bs4 import BeautifulSoup
import os.path

host = 'https://wordsonline.ru'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.5005.134 YaBrowser/22.7.0.1842 Yowser/2.5 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9 '
}
words_set = set()


def get_index_page() -> str:
    url = 'https://wordsonline.ru/dicts/orthography.html'
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        if os.path.exists('HTML/index.html'):
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


def get_alphabet_pages() -> list[str]:
    alphabet_links = []
    html_text = get_index_page()
    soup = BeautifulSoup(html_text, 'lxml')
    res = soup.find('div', class_='alphabet').find_all('a')
    for i in res:
        alphabet_links.append(host + i.get('href'))
    return alphabet_links


def get_pagination():
    pagination_pages = []
    for i in get_alphabet_pages():
        r = requests.get(url=i, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        try:
            last_page = int(soup.find('ul', class_='pagination').find_all('a')[-1].text)
            for j in range(2, last_page + 1):
                pagination_pages.append(f'{i}?page={j}')
        except AttributeError:
            print('Just one page found')
    return pagination_pages + get_alphabet_pages()


def get_words():
    links = get_pagination()
    count = 1
    for i in links:
        r = requests.get(url=i, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        words = soup.find('ul', class_='list-unstyled').findAll('li')
        for word in words:
            words_set.add(word.text)
        # time.sleep(0.1)
        print(f'Scrapping page {count}/{len(links)}')
        count += 1
    print(len(words_set))
    with open('DATA/words.txt', 'w', encoding='utf-8') as file:
        data = file.write(','.join(words_set))
        return data


def main():
    get_words()


if __name__ == '__main__':
    main()
