import telebot
from telebot import types
import shelve
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(mess):
    chat_id = mess.chat.id
    markup = types.ReplyKeyboardMarkup()
    btn_a = types.KeyboardButton('Push')
    btn_b = types.KeyboardButton('Pull')
    markup.add(btn_a, btn_b)
    bot.send_message(chat_id, 'Привет', reply_markup = markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
  
    if message.text == "Push":
        bot.send_message(message.from_user.id, "Task 1, /hint")
    elif message.text == "/hint":
        bot.send_message(message.from_user.id, "Hint 1")
  
  
@bot.message_handler(content_types=['text'])
def handle_text(message):
  
    if message.text == "Pull":
        bot.send_message(message.from_user.id, "Task 2, /hint")
    elif message.text == "/hint":
        bot.send_message(message.from_user.id, "Hint 2")


if __name__ == '__main__':
    bot.polling(True)