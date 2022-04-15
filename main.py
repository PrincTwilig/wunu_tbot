import telebot
from phys_lab5 import handle_spisk
bot = telebot.TeleBot('2030518741:AAGIODEOhmrpWEhoZ9z8u4roDjhbLHrnyV8')
from admin import *

# відповіді на текстові повідомлення
def answer(text):
    text = text.lower()
    # physics ================================================================
    if text == 'фізика лаб 1':
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
        return 'не розумію'

@bot.message_handler(commands=['admin'])
def adminka_check(message):
    try:
        if int(message.chat.id) == 761711722 or int(message.chat.id) == 455033874 or int(message.chat.id) == 802040396:
            bot.send_message(message.chat.id, 'Вітаю!')
            adminka(message)
        else:
            bot.send_message(message.chat.id, 'Ви не адміністратор')
    except Exception as e:
        bot.send_message(message.chat.id, "error:\n" + str(e))


# запуск розвязку лаб5
@bot.message_handler(commands=['phys_lab5'])
def phys_lab5(message):
    try:
        bot.send_message(message.chat.id, 'Version: 1.0\n')
        bot.send_message(message.chat.id, 'Введіть додатній номер списку щоб додати відсоток, та відємний щоб відняти відсоток від данних(якщо ви перший в списку, то впишіть 0)')
        msg = bot.send_message(message.chat.id, "Введіть цифру від -50 до 50")
        bot.register_next_step_handler(msg, handle_spisk) # запускає обробку данних в файлі phys_lab5.py
    except Exception as e:
        bot.send_message(message.chat.id, 'Щось пішло не так')

# зберігати id;username користувачів
def grab(message):
    try:
        user = message.chat.username + ";" +  str(message.chat.id)
        with open('users.txt', 'r') as f:
            if user not in f.read():
                with open('users.txt', 'a') as f:
                    f.write(user + ';')
    except Exception as e:
        bot.send_message(message.chat.id, 'Щось пішло не так\n' + str(e))


# реакція на відправку start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на звязку. Напиши мені що-небудь')
    grab(m)

# команда phys виводить список фізики
@bot.message_handler(commands=["phys"])
def buttons_phys(message):
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row('Фізика лаб 1', 'Фізика лаб 2')
    markup.row('Фізика лаб 4', 'Фізика лаб 5')
    bot.send_message(message.chat.id, 'Вибери лабораторну роботу:', reply_markup=markup)

# реакція на відправку тексту
@bot.message_handler(content_types=["text"])
def handle_text(message):
    print(str(message.chat.id) + ";" + message.text)
    grab(message)
    user = message.chat.username + "_" +  str(message.chat.id)
    bot_answer = answer(message.text)
    bot.send_message(message.chat.id, bot_answer)

# реакція на відправку фото
@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    user = message.chat.username + "_" +  str(message.chat.id)
    bot.send_message(message.chat.id, 'Супер! Я получив фото')



# Запускаем бота
bot.polling(none_stop=True, interval=0)