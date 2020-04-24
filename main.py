import telebot
from telebot import types
import config
from database_connector import database

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    btn_a = types.KeyboardButton('Show Subject')
    markup.add(btn_a)
    bot.send_message(chat_id,
                     'Привіт, я бот який допоможе тобі швидко знаходити корисну інформацію з різних предметів, або ж поділитися посиланнями на цікаві джерела.',
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Show Subject":
        if database.is_connected():
            cursor = database.cursor()
            cursor.execute("select name, subject_id from subjects;")
            subjects = cursor.fetchall()
            keyboard = types.InlineKeyboardMarkup()
            for tmp in subjects:
                keyboard.add(types.InlineKeyboardButton(text=str(tmp[0]), callback_data='s' + str(tmp[1])))
            global sended_message
            sended_message = bot.send_message(message.from_user.id, text="Subjects:", reply_markup=keyboard)
            print(sended_message)

    elif message.text == '/add':
        bot.send_message(message.from_user.id, 'Введіть коротку назву посилання:')
        bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name


def get_name(message):  # отримуюм лінк
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Введіть посиллання:')
    bot.register_next_step_handler(message, get_url)


def get_url(message):
    global url
    url = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Додати', callback_data='add')  # кнопка «Да»
    keyboard.add(key_yes);  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Відмінити', callback_data='cancel')
    keyboard.add(key_no)
    question = 'Назва: ' + str(name) + '\nПосилання: ' + url
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print(call.data, call.from_user.first_name)
    # print(call)
    # data = call.split('/')
    if database.is_connected():
        if call.data[0] == 'z':
            cursor = database.cursor()
            cursor.execute("select name, subject_id from subjects;")
            global subject_back
            subject_back = str(call.data[1:])
            subjects = cursor.fetchall()
            keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
            for tmp in subjects:
                keyboard.add(types.InlineKeyboardButton(text=str(tmp[0]), callback_data='s' + str(tmp[1])))
            bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text="Subjects:",
                                  reply_markup=keyboard)
        elif call.data[0] == 's':
            cursor = database.cursor()
            cursor.execute("select title, sSubject_id from sSubject where subject_id = " + str(call.data[1:]) + ";")
            global ssubject_back
            ssubject_back = str(call.data[1:])
            subjects = cursor.fetchall()
            keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
            for tmp in subjects:
                keyboard.add(types.InlineKeyboardButton(text=str(tmp[0]), callback_data='t' + str(tmp[1])))
            keyboard.add(types.InlineKeyboardButton(text="Back", callback_data='z'))
            bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text="SubSubject:",
                                  reply_markup=keyboard)
        elif call.data[0] == 't':
            cursor = database.cursor()
            cursor.execute("select title, topic_id from topic where ssubject_id = " + str(call.data[1:]) + ";")
            global topic_back
            topic_back = str(call.data[1:])
            subjects = cursor.fetchall()
            keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
            for tmp in subjects:
                keyboard.add(types.InlineKeyboardButton(text=str(tmp[0]), callback_data='u' + str(tmp[1])))
            keyboard.add(types.InlineKeyboardButton(text="Back", callback_data='s' + ssubject_back))
            bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text="Topic:",
                                  reply_markup=keyboard)
        elif call.data[0] == 'u':
            cursor = database.cursor()
            cursor.execute("select url, title from links where topic_id = " + str(call.data[1:]) + " order by rating;")

            global url_back
            url_back = str(call.data[1:])

            subjects = cursor.fetchall()
            keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
            for tmp in subjects:
                keyboard.add(types.InlineKeyboardButton(text=tmp[1], url=tmp[0]))
            keyboard.add(types.InlineKeyboardButton(text="Add Link", callback_data='Send_add'))
            keyboard.add(types.InlineKeyboardButton(text="Back", callback_data='t' + topic_back))
            bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text="Посилання",
                                  reply_markup=keyboard)
        elif call.data == "Send_add":
            markup = types.ReplyKeyboardMarkup()
            btn_a = types.KeyboardButton('/add')
            markup.add(btn_a)
            bot.send_message(call.from_user.id, "Клацніть /add будь ласка", reply_markup=markup)
        elif call.data == "add":
            print(name, url, url_back)
            request = "INSERT INTO links(url, title, topic_id, userId) VALUES(%s,%s,%s,%s)"
            arquments = (url, name, url_back, call.from_user.id)
            cursor = database.cursor()
            try:
                cursor.execute(request, arquments)
                database.commit()
                print("comited")
                markup = types.ReplyKeyboardMarkup()
                btn_a = types.KeyboardButton('Show Subject')
                markup.add(btn_a)
                bot.send_message(call.from_user.id, "Successful", reply_markup=markup)
            except Error as error:
                print(error)
        elif call.data == "cancel":
            markup = types.ReplyKeyboardMarkup()
            btn_a = types.KeyboardButton('Show Subject')
            markup.add(btn_a)
            bot.send_message(call.from_user.id, "Okey, Let's bck to Show Subject", reply_markup=markup)


if __name__ == '__main__':
    bot.infinity_polling()
