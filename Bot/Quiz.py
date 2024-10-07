from bot_config import bot
from telebot import types
from Result_Handler import calculate_result

questions = [
    {
        'question': "Какое время года вам больше всего нравится?",
        'answers': {'Зима': 'bear', 'Весна': 'deer', 'Лето': 'lion', 'Осень': 'fox'}
    },
    {
        'question': "Какой ваш любимый вид отдыха?",
        'answers': {'Активный': 'lion', 'Пассивный': 'bear', 'На природе': 'deer', 'В городе': 'fox'}
    },
    {
        'question': "Что вам больше нравится?",
        'answers': {'Сладкое': 'bear', 'Соленое': 'fox', 'Кислое': 'lion', 'Горькое': 'deer'}
    }
]

user_answers = {}

def start_quiz(message):
    user_answers[message.chat.id] = []
    ask_question(message, 0)

def ask_question(message, question_index):
    if question_index < len(questions):
        question = questions[question_index]['question']
        answers = questions[question_index]['answers']

        markup = types.InlineKeyboardMarkup()
        for answer, animal in answers.items():
            markup.add(types.InlineKeyboardButton(answer, callback_data=f'answer_{question_index}_{animal}'))

        bot.send_message(message.chat.id, question, reply_markup=markup)
    else:
        calculate_result(message, user_answers[message.chat.id])

@bot.callback_query_handler(func=lambda call: call.data.startswith('answer_'))
def handle_answer(call):
    _, question_index, animal = call.data.split('_')
    question_index = int(question_index)
    if call.message.chat.id in user_answers:
        user_answers[call.message.chat.id].append(animal)

    next_question_index = question_index + 1
    ask_question(call.message, next_question_index)
