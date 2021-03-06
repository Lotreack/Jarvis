import telebot

botToken = ""
bot = telebot.TeleBot(botToken)


# telebot.apihelper.proxy = {}
# прокси, если нужен, в
# формате {'https': 'login:password@address:port'}


@bot.message_handler(commands=["start"])  # Реакция на команду start
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в Jarvis!\n"
        "Это помощник, сценарии поведения которого настраиваются через ",
        "web-приложение на Flask\n",
    )


def send_message(user_id, text):
    bot.send_message(user_id, text=text)
