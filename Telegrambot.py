import telebot
from telebot import types
from binance.client import Client
from binance.enums import *

bot = telebot.TeleBot("6454670625:AAH1QrbgJBKoEXdROlqGRPV5eOvb5oelyMA")

# Configura las credenciales de la API de Binance Futures
API_KEY_BINANCE = 'TU_API_KEY'
API_SECRET_BINANCE = 'TU_API_SECRET'

# Inicializa el cliente de Binance Futures
client_binance = Client(API_KEY_BINANCE, API_SECRET_BINANCE)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	
    markup = types.InlineKeyboardMarkup(row_width=2)
    boton1= types.InlineKeyboardButton('Crear', callback_data='crear')
    boton2= types.InlineKeyboardButton('Vender', callback_data='vender')
    boton3= types.InlineKeyboardButton('Ver' ,callback_data='ver')
    boton4= types.InlineKeyboardButton('Balance', callback_data='balance')
    boton5= types.InlineKeyboardButton('Cerrar Posiciones', callback_data='cerrar')
    markup.add(boton1,boton2,boton3, boton4, boton5)
    bot.send_message(message.chat.id, 'Elige una', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(callback):
        if callback.data == 'crear':
            bot.send_message(callback.message.chat.id, "creando posicion")
        elif callback.data == 'vender':
            bot.send_message(callback.message.chat.id, "Vender posicion")
        elif callback.data == 'ver':
            bot.send_message(callback.message.chat.id, "/ver_posiciones")
        elif callback.data == 'balance':
            bot.send_message(callback.message.chat.id, "/balance")

@bot.message_handler(commands=['balance'])
def check_balance(message):
    account_info = client_binance.futures_account()
    balance = account_info['totalWalletBalance']
    bot.reply_to(message, f"Tu saldo en Binance Futures es: {balance} USDT")


 

bot.infinity_polling()