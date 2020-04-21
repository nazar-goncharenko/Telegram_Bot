import telebot
from telebot import types
from telebot import types
import shelve
import config

bot = telebot.TeleBot(config.token)



import  mysql.connector;


database = mysql.connector.connect(user='root', password='root', 
                              host='localhost', 
                              database='newschema')


@bot.message_handler(commands=['start'])
def start(mess):
    chat_id = mess.chat.id
    markup = types.ReplyKeyboardMarkup()
    btn_a = types.KeyboardButton('Show Subject')
    markup.add(btn_a)
    bot.send_message(chat_id, 'Привет', reply_markup = markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Show Subject":
        if database.is_connected():
            cursor = database.cursor()
            cursor.execute("select name, subject_id from subjects;")
            subjects = cursor.fetchall();
            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
            for tmp in subjects:
                keyboard.add(types.InlineKeyboardButton(text=str(tmp[0]), callback_data= 's' + str(tmp[1])))
            bot.send_message(message.from_user.id, text = "Subjects:" , reply_markup = keyboard)
                
            





@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print(call.data)
    if database.is_connected():

        if call.data[0] == 's':
            cursor = database.cursor()
            cursor.execute("select title, sSubject_id from sSubject where subject_id = " + str(call.data[1:]) + ";")
            subjects = cursor.fetchall();
            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
            for tmp in subjects:
                keyboard.add(types.InlineKeyboardButton(text=str(tmp[0]), callback_data='t' + str(tmp[1])))
            bot.send_message(call.from_user.id, text = "SubSubject:" , reply_markup = keyboard)
        elif call.data[0] == 't':
            cursor = database.cursor()
            cursor.execute("select title, topic_id from topic where ssubject_id = " + str(call.data[1:]) + ";")
            subjects = cursor.fetchall();
            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
            for tmp in subjects:
                keyboard.add(types.InlineKeyboardButton(text=str(tmp[0]), callback_data='u' + str(tmp[1])))
            bot.send_message(call.from_user.id, text = "Topic:" , reply_markup = keyboard)
        elif call.data[0] == 'u':
            cursor = database.cursor()
            cursor.execute("select url from links where topic_id = " + str(call.data[1:]) + " order by rating;")
            subjects = cursor.fetchall();
            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
            for tmp in subjects:
                keyboard.add(types.InlineKeyboardButton(text='Lection', url = tmp[0]))
            bot.send_message(call.from_user.id, text = "Лекции" , reply_markup = keyboard)
    
      




if __name__ == '__main__':
     bot.infinity_polling()