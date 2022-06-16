import requests
from bs4 import BeautifulSoup as b
import random
import telebot

URL = 'https://www.anekdot.ru/last/good/'
API_key = '5238225700:AAGo86MOfTM2f75gOMKr2Q1jzjcL65SwCfM'


def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]


list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_key)


@bot.message_handler(commands=['Начать'])
def hello(message):
    bot.send_message(message.chat.id, 'Hi, man! Enter number 0-9: ')


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '0123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'No, man! Enter number 0-9: ')


bot.polling()
