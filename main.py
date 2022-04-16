import telebot
from phys_lab5 import handle_spisk
bot = telebot.TeleBot('2030518741:AAGIODEOhmrpWEhoZ9z8u4roDjhbLHrnyV8')
from admin import *


# відповіді на текстові повідомлення
def answer(message):
    text = message.text.lower()
    # physics ================================================================
    if text == 'фізика':
        phys_markups(message)
        return 'Да'
    elif text == 'фізика лаб 1':
        return 'Фізика лаб 1: https://github.com/PrincTwilig/wunu_proj/releases/tag/Phys_lab1'
    elif text == 'фізика лаб 2':
        return 'Фізика лаб 2: https://github.com/PrincTwilig/wunu_proj/releases/tag/Phys_lab2'
    elif text == 'фізика лаб 4':
        return 'Фізика лаб 4: https://github.com/PrincTwilig/wunu_proj/releases/tag/Phys_lab4'
    elif text == 'фізика лаб 5':
        return 'Фізика лаб 5: https://github.com/PrincTwilig/wunu_proj/releases/tag/Phys_lab5\n\nАбо онлайн версія: https://colab.research.google.com/drive/1Uh8d4jaEYUzE-UsZKI61fL04u3dogN5g?usp=sharing#scrollTo=MP-1SanzexLb\n\nАбо завантажити з проекту: /phys_lab5'
    # physics ================================================================
    # якщо написав назад, виключає markups
    else:
        return 'Команда не розпізнана, шось введено не так, спробуйте ще раз або перейдіть в /menu'

@bot.message_handler(commands=['admin'])
def adminka_check(message):
    try:
        if int(message.chat.id) == 761711722 or int(message.chat.id) == 455033874 or int(message.chat.id) == 802040396:
            bot.send_message(message.chat.id, 'Вітаю!')
            adminka(message)
        else:
            bot.send_message(message.chat.id, 'Ви не адміністратор')
    except Exception as e:
        bot.send_message(message.chat.id, "Помилка: " + str(e))
        print("crashed" + str(e))


# запуск розвязку лаб5
@bot.message_handler(commands=['phys_lab5'])
def phys_lab5(message):
    try:
        bot.send_message(message.chat.id, 'Version: 1.0\n')
        bot.send_message(message.chat.id, 'Введіть додатній номер списку щоб додати відсоток, та відємний щоб відняти відсоток від данних(якщо ви перший в списку, то впишіть 0)')
        msg = bot.send_message(message.chat.id, "Введіть цифру від -50 до 50")
        bot.register_next_step_handler(msg, handle_spisk) # запускає обробку данних в файлі phys_lab5.py
    except Exception as e:
        bot.send_message(message.chat.id, "Помилка: " + str(e))
        print("crashed" + str(e))

# зберігати id;username користувачів
def grab(message):
    try:
        user = str(message.chat.username) + ";" +  str(message.chat.id) + ";"
        with open('new_users.txt', 'r') as f:
            with open('users.txt', 'r') as fa:
                if (user not in f.read()) and (user not in fa.read()):
                    with open('new_users.txt', 'a') as f:
                        f.write(user)
                        print(str(user) + " just enjoed!")
                        bot.send_message(761711722, str(user) + " just enjoed!")
        with open('users.txt', 'r') as f:
            if user not in f.read():
                with open('users.txt', 'a') as f:
                    f.write(user)
    except Exception as e:
        bot.send_message(message.chat.id, "Помилка: " + str(e))
        print("crashed" + str(e))



# реакція на відправку start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    try:
        bot.send_message(m.chat.id, 'Я на звязку. Напиши мені що-небудь')
        grab(m)
    except Exception as e:
        bot.send_message(m.chat.id, "Помилка: " + str(e))
        print("crashed" + str(e))

# команда phys виводить список фізики
@bot.message_handler(commands=["menu"])
def main_menu(message):
    try:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = telebot.types.KeyboardButton('Фізика')
        markup.add(itembtn1)
        bot.send_message(message.chat.id, 'Головне меню\nВключити меню вибору лабораторної з фізики, кнопка "Фізика" нижче', reply_markup=markup)
    except Exception as e:
        bot.send_message(message.chat.id, "Помилка: " + str(e))
        print("crashed" + str(e))

def phys_markups(message):
    markups = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = telebot.types.KeyboardButton('Фізика лаб 1')
    itembtn2 = telebot.types.KeyboardButton('Фізика лаб 2')
    itembtn3 = telebot.types.KeyboardButton('Фізика лаб 4')
    itembtn4 = telebot.types.KeyboardButton('Фізика лаб 5')
    markups.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Підсказки фізика", reply_markup=markups)

# реакція на відправку тексту
@bot.message_handler(content_types=["text"])
def handle_text(message):
    try:
        print(str(message.chat.username) + ': ' + str(message.text))
        grab(message)
        bot_answer = answer(message)
        bot.send_message(message.chat.id, bot_answer)
    except Exception as e:
        bot.send_message(message.chat.id, "Помилка: " + str(e))
        print("crashed" + str(e))


# Запускаем бота
try:
    bot.polling(none_stop=True, interval=0)
except Exception as e:
    print("crashed" + str(e))