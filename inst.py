from libs import *

def inst_in(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = telebot.types.KeyboardButton('1. Рандомне число між min max')
    itembtn2 = telebot.types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2)
    msg = bot.send_message(message.chat.id, 'Виберіть дію:', reply_markup=markup)
    bot.register_next_step_handler(msg, inst_menu)

def inst_menu(message):
    try:
        if message.text == '1. Рандомне число між min max':
            random_start(message)
        elif message.text == 'Назад':
            exit(message)
        else:
            bot.send_message(message.chat.id, 'Невірна команда')
            inst_in(message)
    except Exception as e:
        bot.reply_to(message, 'Помилка: ' + str(e))

def random_start(message):
    msg = bot.send_message(message.chat.id, 'Введіть через пробіл два числа "min max"')
    bot.register_next_step_handler(msg, random_in)

def random_in(message):
    try:
        if message.text == 'Назад':
            inst_in(message)
            return 0
        if message.text.split(' ')[0].isdigit() and message.text.split(' ')[1].isdigit():
            min = int(message.text.split(' ')[0])
            max = int(message.text.split(' ')[1])
            if min > max:
                bot.send_message(message.chat.id, 'Невірні дані')
                random_start(message)
            else:
                random_out(message, min, max)
        else:
            bot.send_message(message.chat.id, 'Невірні дані')
            random_start(message)
    except Exception as e:
        bot.reply_to(message, 'Помилка: ' + str(e))
        print(str(e))
    inst_in(message)


def random_out(message, min, max):
    try:
        if min == max:
            bot.send_message(message.chat.id, 'Випадкове число: ' + str(min))
        else:
            bot.send_message(message.chat.id, 'Випадкове число: ' + str(random.randint(min, max)))
    except Exception as e:
        bot.reply_to(message, 'Помилка: ' + str(e))
        print(str(e))
    inst_in(message)

def exit(message):
    # вихід з адмінки
    bot.send_message(message.chat.id, 'Вихід з інструментів')