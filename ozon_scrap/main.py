import requests

url = 'https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=/searchSuggestions/?text=&url=/search/?text={value}&from_global=true'
host = 'https://www.ozon.ru'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.4.904 Yowser/2.5 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


def get_data():
    r = requests.get(url=url, headers=headers)
    print(r)
    # TODO error 403 found, try json


def main():
    get_data()


if __name__ == "__main__":
    main()
