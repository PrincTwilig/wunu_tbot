from moduls.globals import *

#log
def log(msg):
    try:
        if type(msg) != str:
            message = str(Date) + "|" + str(Time) + "; " + str(msg.from_user.first_name) + ": " + str(msg.text)
        else:
            message = str(Date) + "|" + str(Time) + "; " + "Bot: " + str(msg)
        print(message)
        with open("data/log.txt", 'a') as f:
            f.write(message + '\n')
    except Exception as e:
        print("Error in log\n" + str(e))


def BASE(msg):
    try:
        message = msg.text.lower().split(' ')
        basa = ["base", "basa", "база", "базований", "базовий"]
        # якщо в масиві message є елемент масив basa
        for i in message:
            if i in basa:
                # відправити рандомну .gif з папки data/baseGif в бот
                bot.send_document(msg.chat.id, open('data/baseGif/' + str(random.randint(1, len(os.listdir('data/baseGif')))) + '.gif', 'rb'))
                log("Відправлено базоване gif")
                break
    except Exception as e:
        print("Error in BASE\n" + str(e))


# bot takes text message
@bot.message_handler(content_types=['text'])
def text_handle(message):
    user = User(message.from_user.id, message.from_user.first_name, message.from_user.username, message.chat.id)
    if user.id not in Users:
        Users.append(user.id)
    log(message)
    if message.text == "Chat_Id":
        # bot sends chat id
        bot.send_message(message.chat.id, message.chat.id)

    BASE(message)





#############################################################################################################################

def every_day_send():
    try:
        day = datetime.datetime.now() - datetime.datetime(2022,6,11)
        message = f"День {day.days}\n\nqq Вадим @Kostya12f10\nСкиньте фото ножок!\n\n@ckazatn чекаєм на онлі фанс ☺️"
        bot.send_message(chat_id=-1001626241387, text=message)
    except Exception as e:
        print("Error in every_day_send\n" + str(e))

schedule.every().day.at("10:00").do(every_day_send)
load_users()

while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print('Bot crashed, Errore:\n' + str(e))
        time.sleep(30)
        print('Trying to restart bot...')