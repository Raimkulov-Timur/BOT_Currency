from config import TOKEN
import telebot
from telebot import types
from parsing import a,b,c,d
import psycopg2

baza = psycopg2.connect(database = 'cur', user = 'tima' , password = '6969' , host = 'localhost')
baza.autocommit = True

cursor = baza.cursor()
# cursor.execute("create table valuta(id serial primary key, currency varchar ,buy varchar,sell varchar, data date default NOW())")
# print('dscsd')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def welcome(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton("ДОЛЛАРЫ 🇺🇸")
    b2 = types.KeyboardButton("ЕВРО 🇩🇪")
    b3 = types.KeyboardButton("ТЕНГЕ 🇰🇿")
    b4 = types.KeyboardButton("РУБЛИ 🇷🇺")
    menu.add(b1,b2,b3,b4)
    bot.send_message(message.chat.id , f"<b>Здравствуйте {message.from_user.username} о какой валюте хотели бы узнать курс???</b>" , parse_mode='html' , reply_markup=menu)

@bot.message_handler(content_types=['text'])

def infa(message):
    if message.text == "ДОЛЛАРЫ 🇺🇸":
        cursor.execute("insert into valuta(currency,buy,sell) values('ДОЛЛАРЫ', %s ,%s)" , tuple(a))
        bot.send_message(message.chat.id , f"<b>КУРС ДОЛЛАРА 🇺🇸</b> (<b>Покупка:</b> {a[0]} <b>сом</b>) (<b>Продажа:</b> {a[1]} <b>сом</b>)",parse_mode='html')
    elif message.text == "ЕВРО 🇩🇪":
        cursor.execute("insert into valuta(currency,buy,sell) values('ЕВРО', %s ,%s)" , tuple(b))
        bot.send_message(message.chat.id , f"<b>КУРС ЕВРО 🇩🇪</b> (<b>Покупка:</b> {b[0]} <b>сом</b>) (<b>Продажа:</b> {b[1]} <b>сом</b>)",parse_mode='html')
    elif message.text == "ТЕНГЕ 🇰🇿":
        cursor.execute("insert into valuta(currency,buy,sell) values('ТЕНГЕ', %s ,%s)" , tuple(c))
        bot.send_message(message.chat.id , f"<b>КУРС ТЕНГЕ 🇰🇿</b> (<b>Покупка:</b> {c[0]} <b>сом</b>) (<b>Продажа:</b> {c[1]} <b>сом</b>)",parse_mode='html')
    elif message.text == "РУБЛИ 🇷🇺":
        cursor.execute("insert into valuta(currency,buy,sell) values('РУБЛИ', %s ,%s)" , tuple(c))
        bot.send_message(message.chat.id , f"<b>КУРС РУБЛЯ 🇷🇺</b> (<b>Покупка:</b> {d[0]} <b>сом</b>) (<b>Продажа:</b> {d[1]} <b>сом</b>)",parse_mode='html')


bot.polling(non_stop=True)

