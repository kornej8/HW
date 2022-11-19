import telebot
from telebot import types
import re

bot = telebot.TeleBot('')

#https://t.me/MISIS_Text_Analizer_bot


droped = ['без' , 'в' , 'до' , 'для' , 'за' , 'из' , 'к' , 'на' , 'над' , 'о' , 'об' , 'от' , 'по' , 'под' , 'пред', 'при' , 'про' , 'с' , 'у' , 'через',  'а', 'и', 'чтобы' , 'если','но', 'или', 'либо', 'что', 'хотя', 'будто', 'ли']

elems = {}
elems[0]= '.'
elems[1]= ','
elems[2]= '?'
elems[3]= '!'
elems[4]= '('
elems[5]= ')'
elems[6]= ';'
elems[7]= ':'
elems[8]= '\n'
elems[9]= '-'




def sorted_text(text):
    text = text.lower()
    i = 0
    while i <= 9:
        text = text.replace(elems[i], ' ')
        i = i + 1
    words = text.split(' ')
    sorted_1 = [word for word in words if word != '']
    sorted_2 = [word for word in sorted_1 if word not in droped]
    return sorted_2

def count_uniq_words(text):
    b = set(sorted_text(text))
    counted_uniq = len(b)
    return counted_uniq

def count_all_words(text):
    k = len(sorted_text(text))
    return k

def count_sentence(text):
    subed = re.sub(r'[!?.]\s', r'/', text)
    counted = len(subed.split('/'))
    return counted


def popular_words(text):
    popular_words=[]

    word_popular = sorted_text(text)
    word_popular_dict = dict.fromkeys(word_popular)

    for word in word_popular:
        word_popular_dict[word] = word_popular.count(word) / len(word_popular) * 100

    max_freq_word = max(word_popular_dict, key = word_popular_dict.get)

    for key in word_popular_dict.keys():
        if word_popular_dict[key]==word_popular_dict[max_freq_word]:
            popular_words.append(key)
    return popular_words

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет, пользователь! Напиши мне какой нибудь текст. Если, нужно что то еще напиши /help')



@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text=='/help':
        bot.send_message(message.chat.id, 'Напиши какой-нибудь текст и я попытаюсь его проанализировать.. Чтобы воспользоваться калькулятором напиши /calc, Чтобы проверить доступность сайта напиши /site')

    elif message.text=='/calc':
        bot.send_message(message.chat.id, 'Бот с калькулятором находится здесь --> https://t.me/KorneyCalcBot')
    elif message.text =='/site':
        bot.send_message(message.chat.id, 'Бот с проверкой доступности сайта находится здесь --> t.me/MISIS_Site_Analizer_bot')
    else:
        user_text = message.text
        text_length = len(user_text) 
        number_of_sentences = count_sentence(user_text)
        unique_counter = count_uniq_words(user_text)
        popular_words_list = popular_words(user_text)
        counter_all_words = count_all_words(user_text)

        bot.send_message(message.chat.id, f'Длина текста: {text_length} символов\nКоличество предложений: {number_of_sentences}\nЧисло уникальных слов: {unique_counter}\nСамые популярные слова(о): {popular_words_list}\nОбщее число слов: {counter_all_words}')






bot.polling(none_stop=True, interval=0)
