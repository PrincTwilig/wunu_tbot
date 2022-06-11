import time
import datetime
import os
import threading
import random

import telebot
import telebot.types as types
import schedule

# Получаем ключ бота
bot = telebot.TeleBot("2030518741:AAGIODEOhmrpWEhoZ9z8u4roDjhbLHrnyV8")

# Auto update time and date every second
Date = datetime.datetime.now().strftime("%d.%m.%Y")
Time = datetime.datetime.now().strftime("%H:%M:%S")
def shedl():
    global Date, Time
    try:
        while True:
            Date = datetime.datetime.now().strftime("%d.%m.%Y")
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            schedule.run_pending()

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSome error in time thread\n" + str(KeyboardInterrupt))
        time.sleep(15)
        shedl()

threading.Thread(target=shedl).start()
# End of auto update time and date

# Users list and class
Users = []
class User:
    def __init__(self, id, name, username, current_chat):
        self.id = id
        self.name = name
        self.username = username
        self.current_chat = current_chat

        self.save()

    def __str__(self):
        return str(self.id) + " " + self.name + " " + self.username + " " + str(self.current_chat)

    # save user to file
    def save(self):
        # check if user already exists
        if open("data/users.txt", "r").read().find(str(self.id)) != -1:
            return
        # if not, save user
        with open("data/users.txt", "a") as f:
            f.write(str(self.id) + ";" + self.name + ";" + self.username + "\n")

# load users from file
def load_users():
    with open("data/users.txt", "r") as f:
        for line in f:
            try:
                line = line.split(";")
                Users.append(User(line[0], line[1], line[2]))
            except:
                pass