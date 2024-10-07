import telebot
from telebot import types
from bot_config import bot
import Guardianship_program, Result_Handler, Request_Handler, Quiz, Sites_Links, Instructions

@bot.message_handler(commands=['start'])
def message_start(message: telebot.types.Message):
    print(message.from_user.id, message.from_user.username)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Готов', callback_data='quiz'))
    markup.add(types.InlineKeyboardButton('Инструкция', callback_data='instruction'))
    markup.add(types.InlineKeyboardButton('Программа Опеки', callback_data='guardianship_program'))
    markup.add(types.InlineKeyboardButton('Сайты', callback_data='sites'))
    markup.add(types.InlineKeyboardButton('Оставить отзыв', callback_data='feedback'))

    greeting_message = f'Привет {message.from_user.first_name}!'
    if message.from_user.last_name:
        greeting_message += f' {message.from_user.last_name}'

    greeting_message += (
        '\nЯ бот [Московского зоопарка](https://moscowzoo.ru/), и я помогу тебе узнать, какое животное здесь '
        'является твоим тотемом. \nГотов? Тогда начнем наше увлекательное путешествие по миру животных!'
    )

    bot.send_message(
        message.chat.id,
        greeting_message,
        parse_mode='Markdown',
        reply_markup=markup
    )

if __name__ == "__main__":
    bot.polling()
