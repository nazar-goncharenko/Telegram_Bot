import telebot
from telebot import types
from telebot import types
import shelve
import config
import Controller

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

        bot.send_message(message.from_user.id, "Привет")
        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
        keyboard.add(key_yes); #добавляем кнопку в клавиатуру
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
        keyboard.add(key_no);
        question = 'Да или Нет?';
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    elif message.text == "Pull":
        bot.send_message(message.from_user.id, "НИЧЕГО")
        bot.send_message(message.from_user.id, "Push")
    if message.text == "Pull":
        bot.send_message(message.from_user.id, "Pull")
    elif message.text == "/hint":
        bot.send_message(message.from_user.id, "hint")


Controller.cnx


if __name__ == '__main__':
     bot.infinity_polling()
