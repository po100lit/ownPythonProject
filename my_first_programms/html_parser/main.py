import requests
from bs4 import BeautifulSoup

host = 'https://shop.kz/'
url = 'https://shop.kz/smartfony/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


def parse(url=url, params=''):
    req = requests.get(url=url, params=params, headers=headers)
    print(req)
    soup = BeautifulSoup(req.text, 'lxml')
    pgn = soup.find('div', class_='bx-pagination').find('div', class_='bx-pagination-container').find('ul').findAll('li')[-2].find('span').text
    print(type(pgn))
    print(pgn)


def main():
    parse(url, params='')


if __name__ == "__main__":
    main()
