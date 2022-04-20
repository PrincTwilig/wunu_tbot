import telebot
bot = telebot.TeleBot('2030518741:AAGIODEOhmrpWEhoZ9z8u4roDjhbLHrnyV8')
from prettytable import PrettyTable


class Solution:

    def __init__(self,spisk,U,I,l,d, n, message):
        self.spisk = spisk
        # Всі початкові значення таблиці, 6 елемент це середнє значення
        self.U = U
        self.I = I
        self.l = l
        self.d = d
        self.p = [0,0,0,0]
        self.delta_p = [0,0,0,0]

        self.n = n

        self.message = message

        # масса одиниці струни

        # Значення похибок
        self.E = 0




    ## Функція для обчислення значень (приватні функції)
    # find p = (pi*d^2*U)/(4*I*l)
    def __find_p(self):
        self.p[0] = (3.14*self.d**2*self.U[0])/(4*self.I[0]*self.l)
        self.p[1] = (3.14*self.d**2*self.U[1])/(4*self.I[1]*self.l)
        self.p[2] = (3.14*self.d**2*self.U[2])/(4*self.I[2]*self.l)
        self.p[3] = (self.p[0] + self.p[1] + self.p[2]) / 3



    # find average value
    def __find_average(self):
        self.U[3] = (self.U[0] + self.U[1] + self.U[2]) / 3
        self.I[3] = (self.I[0] + self.I[1] + self.I[2]) / 3


    # find delta_p = p[3] - p[i] module
    def __find_delta_p(self):
        self.delta_p[0] = abs(self.p[3] - self.p[0])
        self.delta_p[1] = abs(self.p[3] - self.p[1])
        self.delta_p[2] = abs(self.p[3] - self.p[2])
        self.delta_p[3] = (self.delta_p[0] + self.delta_p[1] + self.delta_p[2]) / 3




    ## Публічні функції
    # Провести розрахунки всієї таблиці
    def calc(self):
        self.__find_p()
        self.__find_delta_p()
        self.__find_average()

    # Переводимо всі значення під номер в списку значення = значення * (spisk/100) + значення
    def normalize(self):
        for i in range(4):
            self.U[i] = self.U[i] * (self.spisk/100) + self.U[i]
            self.I[i] = self.I[i] * (self.spisk/100) + self.I[i]
            self.p[i] = self.p[i] * (self.spisk/100) + self.p[i]
        self.l = self.l * (self.spisk/100) + self.l
        self.d = self.d * (self.spisk/100) + self.d

    # заокруглити всі значення до 4 знаків після коми
    def round_values(self):
        for i in range(4):
            self.U[i] = round(self.U[i],5)
            self.I[i] = round(self.I[i],5)
            self.p[i] = round(self.p[i],5)
        self.l = round(self.l,5)
        self.d = round(self.d,5)


    # print table
    def print_table(self):
        f = open("phys_lab8_" + str(self.n) + ".txt", 'w')
        table = PrettyTable()
        table.field_names = ["No", "U", "I", "l", "d", "p"]
        for i in range(4):
            table.add_row([i+1 if i != 3 else "ser",self.U[i],self.I[i],' ' if i != 1 else self.l,' ' if i != 1 else self.d,self.p[i]])
        text = "\nTable "+ str(self.n) + ", variant " + str(self.spisk) + ":\n\n"
        text += table.get_string()
        text += "\nАбсолютна похибка V: " + str(self.p[3]) + " +- " + str(self.delta_p[3]) + "\nВідносна похибка E: " + str(round((self.delta_p[3]/self.p[3])*100,5)) + "%\n"
        f.write(text)
        f.close()
        bot.send_document(self.message.chat.id, open("phys_lab8_" + str(self.n) + ".txt", 'r'))





# main
def handle_spisk_lab8(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, 'Ви ввели не коректне значення')
        bot.send_message(message.chat.id, "Введіть цифру від -50 до 50\nСпробуйте ще раз /phys_lab8")
        return 0
    if not int(message.text) <= 50 or not int(message.text) >= -50:
        bot.send_message(message.chat.id, 'Ви ввели не коректне значення')
        bot.send_message(message.chat.id, "Введіть цифру від -50 до 50\nСпробуйте ще раз /phys_lab8")
        return 0
    bot.send_message(message.chat.id, 'Ви ввели коректне значення')
    spisk = int(message.text)
    print(str(message.chat.username) + ": Тільки що скачав лабу 8 варіант: " + str(spisk))
    table1 = Solution(spisk, [1,1.3,1.5,0], [0.23,0.2,0.23,0], 0.3, 0.7, 1, message)  # Створюєм об'єкт класу Solution
    table2 = Solution(spisk, [2.3,2.5,2.5,0], [19,19,18.5,0], 0.6, 0.7, 2, message)
    table3 = Solution(spisk, [20,20.5,20.3,0], [0.5,0.56,0.58,0], 0.2, 0.05, 3, message)

    table1.normalize() # Переводимо значення під варіант
    table2.normalize()
    table3.normalize()
    table1.calc() # знаходимо невідомі
    table2.calc()
    table3.calc()
    table1.round_values() # Заокруглюємо значення до 4 цифр після коми
    table2.round_values()
    table3.round_values()
    table1.print_table() # Виводимо таблицю
    table2.print_table()
    table3.print_table()


