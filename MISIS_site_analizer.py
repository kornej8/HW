import telebot
from telebot import types
import urllib3

http = urllib3.PoolManager()
bot = telebot.TeleBot('')

#https://t.me/MISIS_Site_Analizer_bot

@bot.message_handler(commands=["start"])
def start(m, res=False):
        bot.send_message(m.chat.id, 'Привет! Пришли мне ссылку, а я тебе скажу доступен сайт или нет')



@bot.message_handler(content_types=["text"])
def handle_text(message):
    if ('http' and '.') not in message.text:
        bot.send_message(message.chat.id, 'Попробуй ввести корректную ссылку')
    else:
        try:
            r = http.request('GET', message.text)
            status = r.status
        except:
            status = -1
        if status == 200:
            bot.send_message(message.chat.id, f'Сайт {message.text} работает!')
        else:
            bot.send_message(message.chat.id, 'Что-то с твоим сайтом не так..')

bot.polling(none_stop=True, interval=0)