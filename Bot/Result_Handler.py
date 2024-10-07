from bot_config import bot
from telebot import types

animals_data = {
    'bear': {
        'image': 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/5fd470b9-2a87-4652-9755-8976895706dd.jpeg',
        'name': 'Медведь',
        'description': 'Вы спокойный и любите отдыхать, как настоящий медведь!\nСистематика\nРусское название подвида — Гималайский медведь, белогрудый медведь, чёрный уссурийский, или чёрный гималайский медведь'
        'Латинское название — Selenarctos (Ursus) tibetanus\nАнглийское название — Asiatic black bear, Manchurian black bear\nКласс — Млекопитающие\nОтряд — Хищные\nСемейство — Медвежьи\nРод — Selenarctos (Ursus)'
    },
    'lion': {
        'image': 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/114939dc-d35b-4999-a317-9858875cf56c.jpeg',
        'name': 'Лев',
        'description': 'Вы сильный лидер, как лев!\n Систематика\nРусское название подвида — Индийский или азиатский лев'
        'Латинское название — Pantera leo persica\nАнглийское название — Asian lion\nКласс — Млекопитающие\nОтряд — Хищные\nСемейство — Кошачьи (Felidae)\nРод — Крупные кошки (Panthera)'
    },
    'deer': {
        'image': 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/b823ecd9-82ad-4b2a-be30-9e49e3b8360c.jpeg',
        'name': 'Антилопа',
        'description': 'Вы грациозны и быстры, как олень!\nСистематика\nРусское название подвида — Черная антилопа\nАнглийское название — Sable antelope\nКласс — Млекопитающие'
        'Отряд — Парнокопытные\nСемейство — Полорогие\nРод — Лошадиные антилопы'
    },
    'fox': {
        'image': 'https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/0a440c09-f451-4665-930d-de09bf6af09b.jpg',
        'name': 'Лиса',
        'description': 'Вы хитры и умны, как лиса!\nСистематика\nРусское название подвида — Обыкновенная или рыжая лисица'
        'Латинское название — Vulpes vulpes\nАнглийское название — Red fox\nКласс — Млекопитающие\nОтряд — Хищныеw\nСемейство — Псовые\nРод — Лисицы'
    }
}

def calculate_result(message, answers):
    if not answers:
        bot.send_message(message.chat.id, "Произошла ошибка при подсчете результатов. Попробуйте снова.")
        return

    result_animal = max(set(answers), key=answers.count)
    result_data = animals_data[result_animal]

    if 'image' in result_data:
        bot.send_photo(message.chat.id, result_data['image'])

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Инструкции', callback_data='instruction'))
    markup.add(types.InlineKeyboardButton('Программа Опеки', callback_data='guardianship_program'))
    markup.add(types.InlineKeyboardButton('Сайты', callback_data='sites'))
    markup.add(types.InlineKeyboardButton('Заново', callback_data='quiz'))
    markup.add(types.InlineKeyboardButton('Обратная связь', callback_data='feedback'))

    bot.send_message(
        message.chat.id,
        f"Ваше тотемное животное - {result_data['name']}!\n{result_data['description']}",
        reply_markup=markup
    )

