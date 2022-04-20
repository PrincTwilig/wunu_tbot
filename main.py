import os

import telebot
import schedule
import time as tm
from threading import Thread
import datetime
from phys_lab5 import handle_spisk
from phys_lab8 import handle_spisk_lab8
bot = telebot.TeleBot('2030518741:AAGIODEOhmrpWEhoZ9z8u4roDjhbLHrnyV8')
from admin import *

# time = h, m, s
time = datetime.datetime.now().strftime('%H:%M:%S')
day = datetime.datetime.now().strftime('%d.%m.%Y')

# відповіді на текстові повідомлення
def answer(message):
    text = message.text.lower()
    # physics ================================================================
    if text == 'фізика':
        phys_markups(message)
        return 'Да'
    elif text == 'фізика лаб 1':
        return 'Фізика лаб 1: \nGithub:\nhttps://github.com/PrincTwilig/wunu_proj/releases/tag/Phys_lab1'
    elif text == 'фізика лаб 2':
        return 'Фізика лаб 2:\nДодатково:\nДумаю можна використати цей сайт для зображення всіх траекторій руху кульки:\nhttps://amesweb.info/Physics/Projectile-Motion-Calculator.aspx\n\nGithub:\nhttps://github.com/PrincTwilig/wunu_proj/releases/tag/Phys_lab2'
    elif text == 'фізика лаб 4':
        return 'Фізика лаб 4:\nДодатково:\n- pi = 3.1415\n- Ціна поділки секундоміра - 0.1 секунди\nФормули:\n- T1 = t1 / n1\n- dT1 = 0.05/n1 - дельта T1\n- g = 4pi^2 * ((h2-h1)/(T1^2 - T2^2))\n- g = 4pi^2 * ((h2-h1)/(T1сер^2 - T2сер^2)) - g середнє\n- dg = |gсер - g| - дельта g\n- E = dgсер / gсер\n\nGithub:\nhttps://github.com/PrincTwilig/wunu_proj/releases/tag/Phys_lab4'
    elif text == 'фізика лаб 5':
        return 'Фізика лаб 5:\nФормули:\n- alfa = 2d\n- V = alfa*v\n- fF = sqrt(F)\n- m = (F/V^2)*d\n\nGithub:\nhttps://github.com/PrincTwilig/wunu_proj/releases/tag/Phys_lab5\n\nАбо онлайн версія: https://colab.research.google.com/drive/1Uh8d4jaEYUzE-UsZKI61fL04u3dogN5g?usp=sharing#scrollTo=MP-1SanzexLb\n\nАбо завантажити з бота: /phys_lab5'
    elif text == 'фізика лаб 8':
        return 'Фізика лаб 8:\nФормули:\n- p = (pid^2U)/(4Il)\nGithub:\nhttps://github.com/PrincTwilig/wunu_proj/releases/tag/Phys_lab8\n\nАбо завантажити з бота:/phys_lab8'
    # physics ================================================================
    # якщо написав назад, виключає markups
    elif text == 'назад':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Все, немає дурацьких підсказок', reply_markup=a)
        return 'Да, їх ріл нема'
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
        store_users_info(message)
        bot.send_message(message.chat.id, 'Version: 1.0\n')
        bot.send_message(message.chat.id, 'Якщо ви хочете додати або відняти відсоткове значення до данних, які задає викладач, то введіть свій порядковий номер у списку вашої групи. \nНаприклад, ваш номер у списку рівний 15.\nВводите 15. До даних  додасться 15%. \nЯкщо потрібно відняти від даних відсотки, то ставите перед вашим числом знак мінус.\nВводите - 15, від даних віднімиться 15%.')
        msg = bot.send_message(message.chat.id, "Введіть цифру від -50 до 50")
        bot.register_next_step_handler(msg, handle_spisk) # запускає обробку данних в файлі phys_lab5.py
    except Exception as e:
        bot.send_message(message.chat.id, "Помилка: " + str(e))
        print("crashed" + str(e))

@bot.message_handler(commands=['phys_lab8'])
def phys_lab5(message):
    try:
        store_users_info(message)
        bot.send_message(message.chat.id, 'Version: 1.0\n')
        bot.send_message(message.chat.id, 'Якщо ви хочете додати або відняти відсоткове значення до данних, які задає викладач, то введіть свій порядковий номер у списку вашої групи. \nНаприклад, ваш номер у списку рівний 15.\nВводите 15. До даних  додасться 15%. \nЯкщо потрібно відняти від даних відсотки, то ставите перед вашим числом знак мінус.\nВводите - 15, від даних віднімиться 15%.')
        msg = bot.send_message(message.chat.id, "Введіть цифру від -50 до 50")
        bot.register_next_step_handler(msg, handle_spisk_lab8) # запускає обробку данних в файлі phys_lab5.py
    except Exception as e:
        bot.send_message(message.chat.id, "Помилка: " + str(e))
        print("crashed" + str(e))

# зберігати id;username користувачів
def grab(message):
    try:
        user = str(message.chat.username) + ";" +  str(message.chat.id) + ";"
        with open('users/new_users.txt', 'r') as f:
            with open('users/users.txt', 'r') as fa:
                if (user not in f.read()) and (user not in fa.read()):
                    with open('users/new_users.txt', 'a') as f:
                        f.write(user)
                        print(str(user) + " just enjoed!")
                        bot.send_message(761711722, str(user) + " just enjoed!")
        with open('users/users.txt', 'r') as f:
            if user not in f.read():
                with open('users/users.txt', 'a') as f:
                    f.write(user)
    except Exception as e:
        bot.send_message(message.chat.id, "Помилка: " + str(e))
        print("crashed" + str(e))

def store_users_info(message):
    try:
        global day, time
        if not os.path.exists("users"):
            os.mkdir("users")
        if not os.path.exists("users/" + str(message.chat.username) + '_' + str(message.chat.id)):
            os.mkdir("users/" + str(message.chat.username) + '_' + str(message.chat.id))
        with open("users/" + str(message.chat.username) + '_' + str(message.chat.id) + '/' + str(day) + '.txt', "a") as f:
            f.write(str(time) + ';' + str(message.chat.username) + '_' + str(message.chat.id) + ': ' + str(message.text) + '\n')
    except Exception as e:
        print(message.chat.id + ';' + str(e))



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
        store_users_info(message)
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = telebot.types.KeyboardButton('Фізика')
        itembtn2 = telebot.types.KeyboardButton('Назад')
        markup.add(itembtn1,itembtn2)
        menu_text = '     ⓂГоловне менюⓂ\n\n'
        menu_text += '🅿 Меню "Фізика"(кнопка замість клавіатури) - посилання на 1,2,4,5,8 лаб з фізики (5 та 8 можна виконати в боті)\n\n\n'
        menu_text += '#⃣INFO#⃣\n\n'
        menu_text += '🐈‍⬛ Github - посилання на гітхаб основної частини проекту\nhttps://github.com/PrincTwilig/wunu_proj\n\n'
        menu_text += '📈 Хто хоче підтримати цей проект, може відплатити своїм тілом, або по скучному на карту 4441 1144 2080 6695 Владислав М.\nhttps://send.monobank.ua/42VwSWkXn9\n\n'
        menu_text += '⛔ Всі ці проекти зроблені лише для ознайомлення з формулами і тим як працюють програми для рішення задач з фізики. За точність/правильність їх роботи я не ручаюсь.\n\n'
        menu_text += '📱 Контакти з адміном, якщо щось не працює чи не понятно @Princess_Twiligh\n\n'
        bot.send_message(message.chat.id, menu_text, reply_markup=markup, disable_web_page_preview=True)
    except Exception as e:
        bot.send_message(message.chat.id, "Помилка: " + str(e))
        print("crashed\n" + str(e))

def phys_markups(message):
    markups = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = telebot.types.KeyboardButton('Фізика лаб 1')
    itembtn2 = telebot.types.KeyboardButton('Фізика лаб 2')
    itembtn3 = telebot.types.KeyboardButton('Фізика лаб 4')
    itembtn4 = telebot.types.KeyboardButton('Фізика лаб 5')
    itembtn5 = telebot.types.KeyboardButton('Фізика лаб 8')
    itembtn6 = telebot.types.KeyboardButton('Назад')
    markups.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.send_message(message.chat.id, "Підсказки фізика", reply_markup=markups)

# реакція на відправку тексту
@bot.message_handler(content_types=["text"])
def handle_text(message):
    try:
        store_users_info(message)
        user_private_talk = user_id_back()
        admin_private_talk = admin_id_back()
        if (user_private_talk != None) and (str(message.chat.id) == str(user_private_talk)):
            print(str(message.chat.username) + ": Тільки що відправив повідомлення адміну " + admin_private_talk + ": " + message.text)
            bot.send_message(admin_private_talk, str(message.chat.username)+': '+message.text)
        else:
            print(str(message.chat.username) + ': ' + str(message.text))
            grab(message)
            bot_answer = answer(message)
            bot.send_message(message.chat.id, bot_answer, disable_web_page_preview=True)
    except Exception as e:
        bot.send_message(message.chat.id, "Помилка: " + str(e))
        print("crashed" + str(e))

def every_day_send():
    try:
        if os.path.exists('users'):
            # open zip file
            zip = ZipFile.ZipFile("users.zip", 'w')
            # walk through the folder
            for root, dirs, files in os.walk("users"):
                for file in files:
                    zip.write(os.path.join(root, file))
            zip.close()
            # send users.zip
            bot.send_document(761711722, open('users.zip', 'rb'))
        else:
            bot.send_message(761711722, "No one send anything(")
    except Exception as e:
        print('Cant send(\n' + str(e))

def shedl_check():
    while True:
        global time, day

        time = datetime.datetime.now().strftime('%H:%M:%S')
        day = datetime.datetime.now().strftime('%d.%m.%Y')

        schedule.run_pending()

        tm.sleep(1)


Thread(target=shedl_check).start()

schedule.every().day.at("22:00").do(every_day_send)


if not os.path.exists('users'):
    os.mkdir('users')
if not os.path.exists('users/new_users.txt'):
    open('users/new_users.txt', 'a').close()
if not os.path.exists('users/users.txt'):
    open('users/users.txt', 'a').close()
if not os.path.exists('phys_lab5'):
    os.mkdir('phys_lab5')
if not os.path.exists('phys_lab8'):
    os.mkdir('phys_lab8')

# Запускаем бота
try:
    bot.polling(none_stop=True, interval=0)
except Exception as e:
    print("crashed" + str(e))