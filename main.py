import telebot
import requests as rq
import json
from telebot import types


bot = telebot.TeleBot('5784927881:AAFtIlYShUXy0CVKvdgYHwPdRf8uDTiAUVs')


@bot.message_handler(commands=["start"])
def get_cat(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>!\nВот тебе котейка!'
    bot.send_message(message.chat.id, mess, parse_mode='html')

    url = 'https://api.thecatapi.com/v1/images/search'
    response = rq.get(url)
    answer = response.json()

    markup = types.InlineKeyboardMarkup()
    zero = types.InlineKeyboardButton(text="ещё котейка", callback_data='yes')
    one = types.InlineKeyboardButton(text="хватит", callback_data='no')
    markup.add(zero, one)
    bot.send_message(message.chat.id, answer[0]['url'], reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def cotej(call):
    url = 'https://api.thecatapi.com/v1/images/search'
    response = rq.get(url)
    answer = response.json()
    markup = types.InlineKeyboardMarkup()
    zero = types.InlineKeyboardButton(text="ещё котейка", callback_data='yes')
    one = types.InlineKeyboardButton(text="хватит", callback_data='no')
    markup.add(zero, one)
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, answer[0]['url'], reply_markup=markup)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'буш скучать по нам - возвращайся) Пока!')


def get_url(message):
    if message.text == 'ещё котейка':
        bot.send_message(message.chat.id, answer[0]['url'])
    elif message.text == 'хватит':
        bot.send_message(message.chat.id, answer[0]['url'])

bot.polling(non_stop=True)