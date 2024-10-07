import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='bot.log', filemode='a')

logging.info('Бот запущен')
logging.error('Произошла ошибка при обработке сообщения')
