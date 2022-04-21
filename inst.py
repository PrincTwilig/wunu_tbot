from libs import *

im_list = []

def inst_in(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = telebot.types.KeyboardButton('1. Рандомне число між min max')
    itembtn2 = telebot.types.KeyboardButton('2. Фото в pdf')
    itembtn3 = telebot.types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3)
    msg = bot.send_message(message.chat.id, 'Виберіть дію:', reply_markup=markup)
    bot.register_next_step_handler(msg, inst_menu)

def inst_menu(message):
    try:
        if message.text == '1. Рандомне число між min max':
            random_start(message)
        elif message.text == '2. Фото в pdf':
            photo_start(message)
        elif message.text == 'Назад':
            exit(message)
        else:
            bot.send_message(message.chat.id, 'Невірна команда')
            inst_in(message)
    except Exception as e:
        bot.reply_to(message, 'Помилка: ' + str(e))
# random ===============================================================
def random_start(message):
    msg = bot.send_message(message.chat.id, 'Введіть через пробіл два числа "min max"')
    bot.register_next_step_handler(msg, random_in)

def random_in(message):
    try:
        if message.text == 'Назад':
            inst_in(message)
            return 0
        try:
            min = int(message.text.split(' ')[0])
            max = int(message.text.split(' ')[1])
            if min > max:
                bot.send_message(message.chat.id, 'Невірні дані')
                random_start(message)
            else:
                random_out(message, min, max)
        except:
            bot.send_message(message.chat.id, 'Невірні дані')
            random_start(message)
    except Exception as e:
        bot.reply_to(message, 'Помилка: ' + str(e))
        print(str(e))


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
# photo ===============================================================
def photo_start(message):
    msg = bot.send_message(message.chat.id, 'Відправте всі фото по черзі, коли закінчите напишіть "ок"')
    bot.register_next_step_handler(msg, photo_in)

def photo_in(message):
    try:
        if message.text == 'Назад':
            inst_in(message)
            return 0
        if message.text == 'Ок' or message.text == 'ок':
            pdf_out(message)
            return 0
        try:
            if message.photo:
                file_id = message.photo[-1].file_id
                file_info = bot.get_file(file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                with open('pdf_con/photo.png', 'wb') as new_file:
                    new_file.write(downloaded_file)
                pdf_out(message)
            else:
                bot.send_message(message.chat.id, 'Невірні дані')
                photo_start(message)
        except Exception as e:
            bot.reply_to(message, 'Помилка: ' + str(e))
            print(str(e))
    except Exception as e:
        bot.reply_to(message, 'Помилка: ' + str(e))
        print(str(e))

def pdf_out(message):
    try:
        global im_list
        im = Image.open('pdf_con/photo.png')
        im = im.convert('RGB')
        im_list.append(im)
        if message.text == 'ок' or message.text == 'Ок':
            im = im_list[0]
            im_list.pop(0)
            #delete last element
            im_list.pop(len(im_list)-1)
            im.save('pdf_con/photo.pdf', save_all=True, append_images=im_list)
            bot.send_document(message.chat.id, open('pdf_con/photo.pdf', 'rb'))
            im_list.clear()
            inst_in(message)
        else:
            photo_start(message)
    except Exception as e:
        bot.reply_to(message, 'Помилка: ' + str(e))
        print(str(e))



def exit(message):
    # вихід з інструментів
    bot.send_message(message.chat.id, 'Вихід з інструментів')

