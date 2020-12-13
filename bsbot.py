import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup
import datetime
from flask import Flask, request
from urllib.request import urlopen

token = '1432717319:AAE_qoD6coUgmcT5CTQAb-jqP0Q2KtV_B20'
secret = 'ioufbvewgr2492yf2gh'
url = 'https://bshbot.pythonanywhere.com/' + secret

bot = telebot.TeleBot(token, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=url)

app = Flask(__name__)
@app.route('/'+secret, methods=['POST'])
def webhook():
    update = types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200


markup1 = telebot.types.InlineKeyboardMarkup()

japanese = telebot.types.InlineKeyboardButton(text='Японский гороскоп',
                                               callback_data='japanese_horoscope')
zodiac = telebot.types.InlineKeyboardButton(text='Зодиакальный гороскоп',
                                               callback_data='zodiac_horoscope')
markup1.add(japanese, zodiac)


markup2 = telebot.types.InlineKeyboardMarkup()

mouse = telebot.types.InlineKeyboardButton(text='Мышь',
                                               callback_data='mouse')
buffalo = telebot.types.InlineKeyboardButton(text='Буйвол',
                                               callback_data='buffalo')
tiger = telebot.types.InlineKeyboardButton(text='Тигр',
                                                 callback_data='tiger')
rabbit = telebot.types.InlineKeyboardButton(text='Кролик',
                                             callback_data='rabbit')
dragon = telebot.types.InlineKeyboardButton(text='Дракон',
                                         callback_data='dragon')
snake = telebot.types.InlineKeyboardButton(text='Змея',
                                              callback_data='snake')
horse = telebot.types.InlineKeyboardButton(text='Лошадь',
                                              callback_data='horse')
goat = telebot.types.InlineKeyboardButton(text='Коза',
                                                  callback_data='goat')
monk = telebot.types.InlineKeyboardButton(text='Обезьяна',
                                                 callback_data='monk')
cock = telebot.types.InlineKeyboardButton(text='Петух',
                                                 callback_data='cock')
dog = telebot.types.InlineKeyboardButton(text='Собака',
                                              callback_data='dog')
boar = telebot.types.InlineKeyboardButton(text='Кабан',
                                              callback_data='boar')

markup2.add(mouse, buffalo)
markup2.add(tiger, rabbit)
markup2.add(dragon, snake)
markup2.add(horse, goat)
markup2.add(monk, cock)
markup2.add(dog, boar)



markup3 = telebot.types.InlineKeyboardMarkup()

oven = telebot.types.InlineKeyboardButton(text='Овен',
                                               callback_data='oven')
telec = telebot.types.InlineKeyboardButton(text='Телец',
                                               callback_data='telec')
bliznec = telebot.types.InlineKeyboardButton(text='Близнец',
                                                 callback_data='bliznec')
rak = telebot.types.InlineKeyboardButton(text='Рак',
                                             callback_data='rak')
lev = telebot.types.InlineKeyboardButton(text='Лев',
                                             callback_data='lev')
deva = telebot.types.InlineKeyboardButton(text='Дева',
                                              callback_data='deva')
vesy = telebot.types.InlineKeyboardButton(text='Весы',
                                              callback_data='vesy')
skorpion = telebot.types.InlineKeyboardButton(text='Скорпион',
                                                  callback_data='scorpion')
strelec = telebot.types.InlineKeyboardButton(text='Стрелец',
                                                 callback_data='strelec')
kozerog = telebot.types.InlineKeyboardButton(text='Козерог',
                                                 callback_data='kozerog')
aqua = telebot.types.InlineKeyboardButton(text='Водолей',
                                              callback_data='aqua')
fish = telebot.types.InlineKeyboardButton(text='Рыбы',
                                              callback_data='fish')

markup3.add(oven, telec)
markup3.add(bliznec, rak)
markup3.add(lev, deva)
markup3.add(vesy, skorpion)
markup3.add(strelec, kozerog)
markup3.add(aqua, fish)


markup4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

ad = telebot.types.KeyboardButton(text='Ссылка на бота')
good = telebot.types.KeyboardButton(text='Что хотят наши создатели?')

markup4.add(ad, good)




@bot.message_handler(commands=['start'])
def start_msg(message):
    sti = open('/home/BShbot/mysite/static/BSbot.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id,
                     f'Привет {message.from_user.first_name}, я BSbot, который создавался для курсовой работы. Выберите нужный тип гороскопа:',
                     reply_markup=markup1, parse_mode='html')
    bot.send_message(message.chat.id, "А так же не забудь глянуть на кнопки в панели!", reply_markup=markup4)



@bot.message_handler(content_types=['text'])
def send_msg(message):
    if message.chat.type == 'private':
        if message.text == 'Ссылка на бота':
            bot.send_message(message.chat.id, 'Ссылка на бота: t.me/MichSNbot', reply_markup=markup4)
        elif message.text == 'Что хотят наши создатели?':
            bot.send_message(message.chat.id, 'Создатели хотят хорошие баллы за курсовую работу', reply_markup=markup4)
        elif message.text:
            bot.send_message(message.chat.id,
                         'Я не знаю что ответить')



@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'japanese_horoscope':
        bot.send_message( call.message.chat.id, "Выберите ваш гороскоп", reply_markup = markup2)
    elif call.data == 'zodiac_horoscope':
        bot.send_message(call.message.chat.id, "Выберите ваш гороскоп", reply_markup=markup3)
    elif call.data == 'mouse':
        url = 'https://orakul.com/horoscope/japanese/mouse.html'
        html = urlopen(url).read().decode('utf-8')
        res = str(html)
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("p", {"class": ""})
        info = cases.getText()
        bot.send_message(call.message.chat.id, f'Ваш гороскоп: *год Мыши* \n{info}', parse_mode='Markdown')
    elif call.data == 'buffalo':
        res = requests.get(
            'https://orakul.com/horoscope/japanese/buffalo.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("p", {"class": ""})
        info = cases.getText()
        bot.send_message(
            call.message.chat.id, f'Ваш гороскоп: *год Буйвола* \n{info}',parse_mode='Markdown')
    elif call.data == 'tiger':
        res = requests.get(
            'https://orakul.com/horoscope/japanese/tiger.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("p", {"class": ""})
        info = cases.getText()
        bot.send_message(
            call.message.chat.id, f'Ваш гороскоп:*год Тигра*\n{info}',parse_mode='Markdown')
    elif call.data == 'rabbit':
        res = requests.get(
            'https://orakul.com/horoscope/japanese/rabbit.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("p", {"class": ""})
        info = cases.getText()
        bot.send_message(
            call.message.chat.id, f'Ваш гороскоп: *год Кролика* \n{info}',parse_mode='Markdown')
    elif call.data == 'dragon':
        res = requests.get(
            'https://orakul.com/horoscope/japanese/dragon.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("p", {"class": ""})
        info = cases.getText()
        bot.send_message(
            call.message.chat.id, f'Ваш гороскоп: *год Дракона*\n{info}',parse_mode='Markdown')
    elif call.data == 'snake':
        url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"
        html = urlopen(url).read().decode('utf-8')
        s = str(html)

        soup = BeautifulSoup(s, "html.parser")
        body = soup.html.body

        country_names = body.findAll('th')[11:479]
        CDR =  body.findAll('td')[:936]#Cases-Deaths-Recoveries

        country_names_list = []
        CDR_list = []

        for i in country_names:
            name = i.getText().title().strip()
            if name != '':
                try:
                    country_names_list.append(name[:str(name).index('[')])
                except:
                    country_names_list.append(name)

        qwe = []
        for i in CDR:
            cdr_ = i.getText().title()
            if '[' in cdr_:
                CDR_list.append(qwe)
                qwe = []
                continue
            else:
                try:
                    qwe.append( int(cdr_.replace(',', '')) )
                except:
                    qwe.append("[НЕТ ИНФОРМАЦИЙ]")

        print(CDR_list, country_names_list)
        bot.send_message(call.message.chat.id, country_names_list[0])
    elif call.data == 'horse':
        res = requests.get(
            'https://orakul.com/horoscope/japanese/horse.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("p", {"class": ""})
        info = cases.getText()
        bot.send_message(
            call.message.chat.id, f'Ваш гороскоп: *год Лошади*\n{info}',parse_mode='Markdown')
    elif call.data == 'goat':
        res = requests.get(
            'https://orakul.com/horoscope/japanese/goat.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("p", {"class": ""})
        info = cases.getText()
        bot.send_message(
            call.message.chat.id, f'Ваш гороскоп: *год Козы*\n{info}',parse_mode='Markdown')
    elif call.data == 'monk':
        res = requests.get(
            'https://orakul.com/horoscope/japanese/monk.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("p", {"class": ""})
        info = cases.getText()
        bot.send_message(
            call.message.chat.id, f'Ваш гороскоп: *год Обезьяны*\n{info}',parse_mode='Markdown')
    elif call.data == 'cock':
        res = requests.get(
            'https://orakul.com/horoscope/japanese/cock.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("p", {"class": ""})
        info = cases.getText()
        bot.send_message(
            call.message.chat.id, f'Ваш гороскоп: *год Петуха*\n{info}',parse_mode='Markdown')
    elif call.data == 'dog':
        res = requests.get(
            'https://orakul.com/horoscope/japanese/dog.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("p", {"class": ""})
        info = cases.getText()
        bot.send_message(
            call.message.chat.id, f'Ваш гороскоп: *год Собаки*\n{info}',parse_mode='Markdown')
    elif call.data == 'boar':
        res = requests.get(
            'https://orakul.com/horoscope/japanese/boar.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("p", {"class": ""})
        info = cases.getText()
        bot.send_message(
            call.message.chat.id, f'Ваш гороскоп: *год Кабана* \n{info}',parse_mode='Markdown')
    if call.data == 'oven':
        res = requests.get(
            'https://orakul.com/horoscope/astrologic/general/aries/today.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
        info = cases.split('Подробнее')
        a = str(datetime.date.today())
        b = a.split('-')
        bot.send_message(
            call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
    elif call.data == 'telec':
        res = requests.get(
            'https://orakul.com/horoscope/astrologic/general/taurus/today.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
        info = cases.split('Подробнее')
        a = str(datetime.date.today())
        b = a.split('-')
        bot.send_message(
            call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
    elif call.data == 'bliznec':
        res = requests.get(
            'https://orakul.com/horoscope/astrologic/general/gemini/today.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
        info = cases.split('Подробнее')
        a = str(datetime.date.today())
        b = a.split('-')
        bot.send_message(
            call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
    elif call.data == 'rak':
        res = requests.get(
            'https://orakul.com/horoscope/astrologic/general/cancer/today.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
        info = cases.split('Подробнее')
        a = str(datetime.date.today())
        b = a.split('-')
        bot.send_message(
            call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
    elif call.data == 'lev':
        res = requests.get(
            'https://orakul.com/horoscope/astrologic/general/lion/today.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
        info = cases.split('Подробнее')
        a = str(datetime.date.today())
        b = a.split('-')
        bot.send_message(
            call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
    elif call.data == 'deva':
        res = requests.get(
            'https://orakul.com/horoscope/astrologic/general/virgo/today.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
        info = cases.split('Подробнее')
        a = str(datetime.date.today())
        b = a.split('-')
        bot.send_message(
            call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
    elif call.data == 'vesy':
        res = requests.get(
            'https://orakul.com/horoscope/astrologic/general/libra/today.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
        info = cases.split('Подробнее')
        a = str(datetime.date.today())
        b = a.split('-')
        bot.send_message(
            call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
    elif call.data == 'scorpion':
        res = requests.get(
            'https://orakul.com/horoscope/astrologic/general/scorpio/today.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
        info = cases.split('Подробнее')
        a = str(datetime.date.today())
        b = a.split('-')
        bot.send_message(
            call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
    elif call.data == 'strelec':
        res = requests.get(
            'https://orakul.com/horoscope/astrologic/general/sagittarius/today.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
        info = cases.split('Подробнее')
        a = str(datetime.date.today())
        b = a.split('-')
        bot.send_message(
            call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
    elif call.data == 'kozerog':
        res = requests.get(
            'https://orakul.com/horoscope/astrologic/general/capricorn/today.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
        info = cases.split('Подробнее')
        a = str(datetime.date.today())
        b = a.split('-')
        bot.send_message(
            call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
    elif call.data == 'aqua':
        res = requests.get(
            'https://orakul.com/horoscope/astrologic/general/aquarius/today.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
        info = cases.split('Подробнее')
        a = str(datetime.date.today())
        b = a.split('-')
        bot.send_message(
            call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
    elif call.data == 'fish':
        res = requests.get(
            'https://orakul.com/horoscope/astrologic/general/pisces/today.html').text
        soup = BeautifulSoup(res, features="html.parser")
        soup.encode('utf-8')
        cases = soup.find("div", {"class": "horoBlock"}).get_text().strip()
        info = cases.split('Подробнее')
        a = str(datetime.date.today())
        b = a.split('-')
        bot.send_message(
            call.message.chat.id, 'Ваш гороскоп на ' + b[2] + '.' + b[1] + ':\n ' + info[0])
    else:
        pass
