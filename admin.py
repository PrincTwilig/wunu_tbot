import zipfile as ZipFile
import telebot
import os
bot = telebot.TeleBot('2030518741:AAGIODEOhmrpWEhoZ9z8u4roDjhbLHrnyV8')

user_private_talk = ''
admin_private_talk = ''

def adminka(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = telebot.types.KeyboardButton('1. Скачати файл користувачів')
    itembtn2 = telebot.types.KeyboardButton('2. Відправити повідомлення всім користувачам')
    itembtn3 = telebot.types.KeyboardButton('3. Говорити з користувачем по id')
    itembtn4 = telebot.types.KeyboardButton('4. Скачати лог чатів користувачів')
    itembtn5 = telebot.types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    msg = bot.send_message(message.chat.id, 'Виберіть дію:', reply_markup=markup)
    bot.register_next_step_handler(msg, admin_menu)

def admin_menu(message):
    try:
        if message.text == '1. Скачати файл користувачів':
            admin_download(message)
        elif message.text == '2. Відправити повідомлення всім користувачам':
            msg = bot.reply_to(message, 'Введіть повідомлення:')
            bot.register_next_step_handler(msg, admin_send_message)
        elif message.text == '3. Говорити з користувачем по id':
            msg = bot.reply_to(message, 'Введіть id користувача, щоб закінчити приватний чат, нажміть "Назад":')
            bot.register_next_step_handler(msg, admin_talk_with_user)
        elif message.text == '4. Скачати лог чатів користувачів':
            admin_download_chats(message)
        elif message.text == 'Назад':
            exit(message)
        else:
            bot.send_message(message.chat.id, 'Невірна команда')
            adminka(message)
    except Exception as e:
        bot.reply_to(message, 'Помилка: ' + str(e))

def admin_talk_with_user(message):
    try:
        global admin_private_talk, user_private_talk
        admin_id = str(message.chat.id)
        admin_private_talk = admin_id
        user_private_talk = message.text
        msg = bot.reply_to(message, 'Введіть повідомлення:')
        bot.register_next_step_handler(msg, admin_talk_with_user_send)
    except Exception as e:
        bot.reply_to(message, 'Помилка: ' + str(e))

def admin_talk_with_user_send(message):
    try:
        global admin_private_talk, user_private_talk
        if message.text == 'Назад':
            admin_private_talk = None
            user_private_talk = None
            adminka(message)
            return 0
        print(str(message.chat.username) + ": Тільки що відправив повідомлення користувачу " + user_private_talk + ": " + message.text)
        bot.send_message(user_private_talk, message.text)
        msg = bot.send_message(message.chat.id, 'Введіть повідомлення:')
        bot.register_next_step_handler(msg, admin_talk_with_user_send)
    except Exception as e:
        bot.reply_to(message, 'Помилка: ' + str(e))

def admin_send_message(message):
    try:
        if message.text == 'Назад':
            adminka(message)
        print(str(message.chat.username) + ": Тільки що відправив повідомлення всім користувачам: " + message.text)
        users = open('users.txt', 'r').read().split((';'))
        users = list(filter(lambda x: x.isdigit(), users))
        for user in users:
            print(user + ' ' + message.text)
            bot.send_message(user, message.text)
        bot.send_message(message.chat.id, 'Повідомлення відправлено')
    except Exception as e:
        bot.reply_to(message, 'Помилка: ' + str(e))
    adminka(message)

def admin_download(message):
    try:
        print(str(message.chat.username) + ": Тільки що спробував скачати файл нових користувачів!")
        users = open('new_users.txt', 'r').read().split((';'))
        bot.send_document(message.chat.id, open('new_users.txt', 'rb'))
        us = 0
        for i in range(0,len(users),2):
            us = us + 1
            bot.send_message(message.chat.id, str(us)+'. '+users[i] + ',' + users[i+1] + '\n')
    except Exception as e:
        bot.reply_to(message, 'Помилка: ' + str(e))
    adminka(message)

def admin_download_chats(message):
    try:
        if os.path.exists('users'):
            zfname = 'users.zip'
            with ZipFile.ZipFile(zfname, "w") as nz:
                nz.write('users')
            bot.send_document(message.chat.id, open('users.zip', 'r'))
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, e)
    adminka(message)


def exit(message):
    # вихід з адмінки
    bot.send_message(message.chat.id, 'Вихід з адмінки')

def admin_id_back():
    global admin_private_talk
    return admin_private_talk

def user_id_back():
    global user_private_talk
    return user_private_talk