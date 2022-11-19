import telebot
from telebot import types
import re
from math import sqrt
import requests
import urllib3
http = urllib3.PoolManager()
from statistics import mode



bot = telebot.TeleBot('')

#https://t.me/KorneyCalcBot

string = ''
prev_string = ''
URL = ''


keyboard = types.InlineKeyboardMarkup()

keyboard.row(
    types.InlineKeyboardButton(text = '√', callback_data='√'),
    types.InlineKeyboardButton(text='C', callback_data='C'),
    types.InlineKeyboardButton(text = 'CE', callback_data='CE')

)
keyboard.row(
    types.InlineKeyboardButton(text = '7', callback_data='7'),
    types.InlineKeyboardButton(text = '8', callback_data='8'),
    types.InlineKeyboardButton(text = '9', callback_data='9'),
    types.InlineKeyboardButton(text = '/', callback_data='/')
)
keyboard.row(
    types.InlineKeyboardButton(text = '4', callback_data='4'),
    types.InlineKeyboardButton(text = '5', callback_data='5'),
    types.InlineKeyboardButton(text = '6', callback_data='6'),
    types.InlineKeyboardButton(text = '*', callback_data='*')
)
keyboard.row(
    types.InlineKeyboardButton(text = '1', callback_data='1'),
    types.InlineKeyboardButton(text = '2', callback_data='2'),
    types.InlineKeyboardButton(text = '3', callback_data='3'),
    types.InlineKeyboardButton(text = '-', callback_data='-')
)
keyboard.row(
    types.InlineKeyboardButton(text = '0', callback_data='0'),
    types.InlineKeyboardButton(text = '.', callback_data='.'),
    types.InlineKeyboardButton(text = '=', callback_data='='),
    types.InlineKeyboardButton(text = '+', callback_data='+')
)

mm = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

button1 = types.KeyboardButton("Калькулятор")
button2 = types.KeyboardButton('Доступность сайта')
button3 = types.KeyboardButton('Анализатор текста')
mm.add(button1,button2,button3)

keyboard_friends = types.InlineKeyboardMarkup()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, что ты хочешь от меня?", reply_markup=mm)

@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text == "Калькулятор":
        bot.send_message(message.chat.id, "Отлично, давай что-то посчитаем")
        global string
        if string == '':
            bot.send_message(message.from_user.id, text='0', reply_markup=keyboard)
        else:
            bot.send_message(message.from_user.id, text=string, reply_markup=keyboard)
    elif message.text == "Доступность сайта":
        bot.send_message(message.chat.id, "Пока я не умею этого делать :( Можешь заглянуть сюда --> https://t.me/MISIS_Site_Analizer_bot")
    elif message.text == "Анализатор текста":
        bot.send_message(message.chat.id, "Пока я не умею этого делать :( Можешь заглянуть сюда --> https://t.me/MISIS_Text_Analizer_bot")
    else:
        bot.send_message(message.chat.id, "Я общаюсь по другому... Напиши /start")


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global string, prev_string
    data = query.data
    if data == 'CE':
        string = ''
    elif data =='C':
        if string!='':
            string = string[:-1]
    elif data == '√':
        try:
            string = str(sqrt(eval(string)))
        except:
            string = 'Что-то не так..'            
    elif data == '=':
        try:
            string = str(eval(string))
        except:
            string = 'Что-то не так..'

    else:
       string+=data


    if string =='':
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text = '0', reply_markup=keyboard)
        prev_string = '0'
    else:
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=string, reply_markup=keyboard)
        prev_string = string
    if string == 'Что-то не так..':
        string = ''


bot.polling(none_stop=True, interval=0)