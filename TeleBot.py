# -- coding: utf-8 --
#import config
import telebot

token = "1086478120:AAENzfoluFzk4OYpFPsoJ-sO8ib_Lxp3crI"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    else:
        bot.send_message(message.chat.id, "Ты пидор")

if __name__ == '__main__':
     bot.infinity_polling()