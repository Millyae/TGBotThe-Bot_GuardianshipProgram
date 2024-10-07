from bot_config import bot
from telebot import types

def send_sites_links(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Московский зоопарк', url='https://moscowzoo.ru/'))
    markup.add(types.InlineKeyboardButton('Возьми животного под опеку', url='https://moscowzoo.ru/about/guardianship'))
    markup.add(types.InlineKeyboardButton('Животные зоопарка', url='https://moscowzoo.ru/animals/kinds'))
    markup.add(types.InlineKeyboardButton('Telegram-канал', url='https://t.me/Moscowzoo_official'))
    markup.add(types.InlineKeyboardButton('Меню', callback_data='menu'))

    bot.send_message(
        message.chat.id,
        'Вот ссылки на сайты:',
        reply_markup=markup
    )
