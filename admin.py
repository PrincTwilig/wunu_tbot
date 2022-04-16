import telebot
bot = telebot.TeleBot('2030518741:AAGIODEOhmrpWEhoZ9z8u4roDjhbLHrnyV8')

def adminka(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = telebot.types.KeyboardButton('1. Скачати файл користувачів')
    itembtn2 = telebot.types.KeyboardButton('2. Відправити повідомлення всім користувачам')
    itembtn3 = telebot.types.KeyboardButton('3. Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    msg = bot.send_message(message.chat.id, 'Виберіть дію:', reply_markup=markup)
    bot.register_next_step_handler(msg, admin_menu)

def admin_menu(message):
    try:
        if message.text == '1. Скачати файл користувачів':
            admin_download(message)
        elif message.text == '2. Відправити повідомлення всім користувачам':
            msg = bot.reply_to(message, 'Введіть повідомлення:')
            bot.register_next_step_handler(msg, admin_send_message)
        elif message.text == '3. Назад':
            exit(message)
        else:
            bot.send_message(message.chat.id, 'Невірна команда')
            adminka(message)
    except Exception as e:
        bot.reply_to(message, 'Помилка: ' + str(e))

def admin_send_message(message):
    try:
        if message.text == '3. Назад':
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

def exit(message):
    # вихід з адмінки
    bot.send_message(message.chat.id, 'Вихід з адмінки')