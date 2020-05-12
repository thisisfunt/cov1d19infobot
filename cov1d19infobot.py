import telebot
import requests
from bs4 import BeautifulSoup

url = "https://xn--80aesfpebagmfblc0a.xn--p1ai/"
user = {"UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

bot = telebot.TeleBot("1252908404:AAF0z9g97wHQKnBqDjMyuFmbWq8-1UfiEwk")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "<b>Приветствую, {0}!\nЯ бот который может дать тебе информацию о ситуации с Covid19.\nЧтобы получить эту информацию напиши мне команду 'info'</b>".format(message.from_user.first_name), parse_mode = "html")
    print(message.from_user)
@bot.message_handler(content_types=["text"])
def send_info(message):
    if(message.text == "info"):
        full_page = requests.get(url, user)
        soup = BeautifulSoup(full_page.content, "html.parser")
        info = soup.findAll("div", {"class":"cv-countdown__item-value"})
        returned = "Заражено - " + info[1].text + " 🤒" + "\n" + "Выздоровело - " + info[3].text + " 🙂" + "\n" + "Умерло - " + info[4].text + " ☠️"
        bot.send_message(message.chat.id, returned)
bot.polling(none_stop=True)
