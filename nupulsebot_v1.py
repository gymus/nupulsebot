#nupulsebot for Telegram (MrRobot)
#Guillermo Vallejo 2016 GPL License
#e-mail:nupulse@ymail.com
#you need to install bitcoin_price_master_api, TelegramBotAPI and dateutil

import exchanges
import telebot

#exchanges

from exchanges.bitfinex import Bitfinex
from exchanges.coinapult import Coinapult
a= Bitfinex().get_current_price()
b= 'BTC-USD Bitfinex'
c= Coinapult().get_current_price(currency = 'EUR')
d= 'BTC-EUR Coinapult'
print (a , b)

#telegram

TOKEN = 'paste here your telegram token'
tb = telebot.TeleBot(TOKEN)

#commands

@tb.message_handler(commands=['help', 'start'])
def send_welcome(message):
    tb.reply_to(message,"""\
Hola, soy Mr Robot, escribe /usd y te dare el precio del Bitcoin en Dolares, escribe /eur y te lo dare en Euros. Escribe /Fair y te dare el precio del Faircoin en Bittrex!\
""")



@tb.message_handler(commands=['usd'])
def precios_divisas(message):
    tb.reply_to(message, a)
    tb.reply_to(message, b)
   

@tb.message_handler(commands=['eur'])
def precios_divisas(message):
    tb.reply_to(message, c)
    tb.reply_to(message, d)


@tb.message_handler(commands=['love'])
def precios_divisas(message):
    tb.reply_to(message,'<3')


@tb.message_handler(func=lambda message: True)
def mensaje_general(message):
    tb.reply_to(message, """Escribe /usd para precio en dolares /eur para precio en euros o /fair para ver el precio de Faircoin!\
""")
    
    
tb.polling()
