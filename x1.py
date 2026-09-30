import os
import threading
from flask import Flask
import telebot

TOKEN = os.getenv('TOKEN')  # Токен возьмем из настроек Render (безопасно)

TEXT_LOVE = (
    "я тоже тебя очень сильно люблю мышонок."
)
TEXT_MISS = "я тоже очень сильно скучаю мышонок, наверное я сейчас занят ну или как обычно сплю, но знай я тебя очень очень люблю и скучаю"

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
        "👉 я скучаю"
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


if __name__ == '__main__':
    keep_alive()  # Запускаем мини-сервер в фоне
    print('Бот запущен на сервере!')
    bot.infinity_polling()