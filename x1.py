import telebot

# Сюда вставьте ваш токен от @BotFather
TOKEN = '8922800335:AAGUfMgyDTMWL79iS8LyzgBQDPG1nzLVnK0'

# ==========================================
# ТУТ ВЫ МОЖЕТЕ НАПИСАТЬ ЛЮБОЙ СВОЙ ТЕКСТ:
TEXT_LOVE = "я тоже тебя очень сильно люблю мышонок"
TEXT_MISS = "я тоже очень сильно скучаю мышонок, наверное я сейчас занят ну или как обычно сплю, но знай я тебя очень очень люблю и скучаю"
# ==========================================

bot = telebot.TeleBot(TOKEN)

# Обработка команды /start или слова "старт"
@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda message: message.text.lower() == 'старт')
def send_welcome(message):
    text = (
        "Приветик мышонок напиши сюда вот эти фразы)\n\n"
        "👉 я тебя люблю\n"
        "👉 я скучаю"
    )
    bot.send_message(message.chat.id, text)

# Ответ на фразу "я тебя люблю"
@bot.message_handler(func=lambda message: 'я тебя люблю' in message.text.lower())
def love_reply(message):
    bot.reply_to(message, TEXT_LOVE)

# Ответ на фразу "я скучаю"
@bot.message_handler(func=lambda message: 'я скучаю' in message.text.lower())
def miss_reply(message):
    bot.reply_to(message, TEXT_MISS)

# Запуск бота
if __name__ == '__main__':
    print("Бот успешно запущен и ждет сообщения!")
    bot.infinity_polling()