import telebot

bot = telebot.TeleBot("6717445789:AAHkNbtyQt3hT_3JKyFVaYeRIOjhiGQIWwI")


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_messege(message.chat.id, '*привет. рады вас видеть*', parse_mode='Markdown')


@bot.message_handler(commands=['meme'])
def main(message):
    bot.send_message(message.chat.id, 'ъуъ! n\ъуъ!')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'ВОТ И [ССЫЛОЧКА](https://youtu.be/WqGCbO4QW9k?si=gSIX0qFfA8orio7k)',
                     parse_mode='Markdown')


bot.infinity_polling()
