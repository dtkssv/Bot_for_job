import data_search
import telebot


bot = telebot.TeleBot()

USERS = []  # Список ID чатов кто имеет доступ к боту


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "")


"""Обработки команды для получения метрик"""
@bot.message_handler(commands=['check'])
def get_metrics(message):
    if message.chat.id in USERS:
        bot.send_message(message.chat.id, "")
        data_search.search_grey_metricks()
        send_massage(message.chat.id, data_search.LINKS_WITH_GREY_METRIC)
        data_search.LINKS_WITH_GREY_METRIC = []
    else:
        bot.send_message(message.chat.id, "У Вас нет доступа к боту")


"""Функция для отправки сообщений и конвертации списка в построчный вид"""
def send_massage(id, text: list):
    text = '\n'.join(text)
    bot.send_message(chat_id=id, text=text)


bot.polling(none_stop=True)
