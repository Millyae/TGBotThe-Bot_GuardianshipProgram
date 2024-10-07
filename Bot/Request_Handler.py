from bot_config import bot
from Sites_Links import send_sites_links
import Guardianship_program, Menu, Instructions
from Quiz import start_quiz
from telebot.types import Message

feedback_data = {}

ADMIN_USER_ID = 5803315773

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'feedback':
        bot.send_message(call.message.chat.id, 'Пожалуйста, оцените нашего бота от 1 до 5:')
        bot.register_next_step_handler(call.message, get_feedback_rating)
    elif call.data == 'instruction':
        Instructions.instruction(call.message)
    elif call.data == 'guardianship_program':
        Guardianship_program.guardianship_program(call.message)
    elif call.data == 'sites':
        send_sites_links(call.message)
    elif call.data == 'quiz':
        bot.send_message(call.message.chat.id, "Готов? Давай начнем!")
        start_quiz(call.message)
    elif call.data == 'menu':
        Menu.menu(call.message)

def get_feedback_rating(message: Message):
    try:
        rating = int(message.text)
        if rating < 1 or rating > 5:
            bot.send_message(message.chat.id, 'Некорректные данные. Пожалуйста, оцените от 1 до 5:')
            bot.register_next_step_handler(message, get_feedback_rating)
            return
        feedback_data[message.chat.id] = {'rating': rating}
        bot.send_message(message.chat.id, 'Спасибо! Можете поделиться вашими впечатлениями или предложениями для улучшения нашего бота:')
        bot.register_next_step_handler(message, get_feedback_text)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите число от 1 до 5')
        bot.register_next_step_handler(message, get_feedback_rating)

def get_feedback_text(message: Message):
    feedback_text = message.text
    feedback_data[message.chat.id]['text'] = feedback_text
    bot.send_message(message.chat.id, 'Благодарим за обратную связь. Мы ценим ваше мнение!')

    feedback = feedback_data[message.chat.id]
    feedback_message = f"Новый отзыв:\nОценка: {feedback['rating']}\nОтзыв: {feedback['text']}"

    bot.send_message(ADMIN_USER_ID, feedback_message)

    del feedback_data[message.chat.id]
