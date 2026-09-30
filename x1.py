import os
import threading
from flask import Flask
import telebot

TOKEN = os.getenv('TOKEN')  # Токен возьмем из настроек Render (безопасно)

TEXT_LOVE = "я тоже тебя очень сильно люблю мышонок."
TEXT_MISS = "я тоже очень сильно скучаю мышонок, наверное я сейчас занят ну или как обычно сплю, но знай я тебя очень очень люблю и скучаю"
TEXT_SAD = 'не грусти мышонок я всегда рядом давай посмотрим рик и морти?)'
TEXT_SAY = 'я тоже очень хочу с тобой пообщаться, но сейчас наверное занят, давай я расскажу, как прошел мой день, а как освобожусь пообщаемся или че нибудь посмотрим) напиши в чатик (как прошел твой день?)'
TEXT_DAY = 'ой мышонок вижу ты хочешь узнать, как прошел мой день я постораюсь обновлять каждый день, сегодня у меня все хорошо было две пары не особо устал щас вот сижу делаю для тебя бота впринципе денек довольно скучный, у тебя как все прошло? а вообще завтра в военкомат нужно и в больничку, ну я думаю на сегодня все люблю тебя мышонок)'
bot = telebot.TeleBot(TOKEN)

# --- МИНИ-СЕРВЕР ЧТОБЫ БОТ НЕ ЗАСЫПАЛ ---
app = Flask('')


@app.route('/')
def home():
    return "Я живой!"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = threading.Thread(target=run)
    t.start()
# ----------------------------------------


@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda message: message.text.lower() == 'старт')
def send_welcome(message):
    text = (
        "Приветик мышонок напиши сюда вот эти фразы)\n"
        "👉 я тебя люблю\n"
        "👉 я скучаю\n"
        "👉 мне грустно\n"
        "👉 я хочу пообщаться\n"
    )
    bot.send_message(message.chat.id, text)


@bot.message_handler(
    func=lambda message: 'я тебя люблю' in message.text.lower()
)
def love_reply(message):
    bot.reply_to(message, TEXT_LOVE)


@bot.message_handler(func=lambda message: 'я скучаю' in message.text.lower())
def miss_reply(message):
    bot.reply_to(message, TEXT_MISS)

@bot.message_handler(func=lambda message: 'мне грустно' in message.text.lower())
def miss_reply(message):
    bot.reply_to(message, TEXT_SAD)

@bot.message_handler(func=lambda message: 'я хочу пообщаться' in message.text.lower())
def miss_reply(message):
    bot.reply_to(message, TEXT_SAY)

@bot.message_handler(func=lambda message: 'как прошел твой день?' in message.text.lower())
def miss_reply(message):
    bot.reply_to(message, TEXT_DAY)


if __name__ == '__main__':
    keep_alive()  # Запускаем мини-сервер в фоне
    print('Бот запущен на сервере!')
    bot.infinity_polling()