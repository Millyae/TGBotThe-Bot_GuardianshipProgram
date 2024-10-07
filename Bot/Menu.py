from bot_config import bot
from telebot import types

def menu(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Готов', callback_data='quiz'))
    markup.add(types.InlineKeyboardButton('Инструкция', callback_data='instruction'))
    markup.add(types.InlineKeyboardButton('Программа Опеки', callback_data='guardianship_program'))
    markup.add(types.InlineKeyboardButton('Сайты', callback_data='sites'))
    markup.add(types.InlineKeyboardButton('Оставить отзыв', callback_data='feedback'))
    bot.send_message(
        message.chat.id,
        'Главное меню\nВыберите действие',
        reply_markup=markup,
        parse_mode='Markdown'
    )
