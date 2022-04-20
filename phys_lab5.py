import telebot
from prettytable import PrettyTable
import matplotlib.pyplot as plt
bot = telebot.TeleBot('2030518741:AAGIODEOhmrpWEhoZ9z8u4roDjhbLHrnyV8')

class Solution:

    def __init__(self,spisk,message):
        self.message = message
        self.spisk = spisk
        # Всі початкові значення таблиці, 6 елемент це середнє значення
        self.v = [275,197,111,55,49,0]
        self.F = [0.4,0.3,0.4,0.3,0.4,0]
        self.fF = [0,0,0,0,0,0]
        self.d1 = [610,300,195,140,145,0]
        self.d2 = [0,310,205,170,155,0]
        self.d3 = [0,0,200,145,165,0]
        self.d4 = [0,0,0,135,155,0]
        self.d = 0.61
        self.alfa = 0
        self.V = [0,0,0,0,0,0]

        self.m = 0 # масса одиниці струни

        # Значення похибок
        self.delta_V = [0,0,0,0,0,0]




    ## Функція для обчислення значень (приватні функції)
    # find alfa = 2*d
    def __find_alfa(self):
        self.alfa = 2*self.d

    # find V = alfa*v
    def __find_V(self):
        for i in range(5):
            self.V[i] = self.alfa*self.v[i]

    # корінь fF= sqrt(F)
    def __find_fF(self):
        for i in range(5):
            self.fF[i] = self.F[i]**0.5

    # малюємо таблицю
    def __draw_table(self):
        X = [self.fF[0], self.fF[1]+0.000001, self.fF[2]+0.000002, self.fF[3]+0.000003, self.fF[4]+0.000004]
        Y = [self.v[0], self.v[1], self.v[2], self.v[3], self.v[4]]

        plt.xlabel("√F")
        plt.ylabel("v")
        plt.plot(X, Y)

    # маса одиниці струни m = (F/V^2)*d
    def __find_m(self):
        self.m = (self.F[5]/self.V[5]**2)*self.d

    # find delta_V = V[5] - V[i] в модулі
    def __find_delta_V(self):
        for i in range(5):
            self.delta_V[i] = abs(self.V[5] - self.V[i])
        self.delta_V[5] = (self.delta_V[0] + self.delta_V[1] + self.delta_V[2] + self.delta_V[3] + self.delta_V[4]) / 5



    # find average value
    def __find_average(self):
        self.v[5] = (self.v[0] + self.v[1] + self.v[2] + self.v[3] + self.v[4])/5
        self.F[5] = (self.F[0] + self.F[1] + self.F[2] + self.F[3] + self.F[4])/5
        self.fF[5] = (self.fF[0] + self.fF[1] + self.fF[2] + self.fF[3] + self.fF[4])/5
        self.d1[5] = (self.d1[0] + self.d1[1] + self.d1[2] + self.d1[3] + self.d1[4])/5
        self.d2[5] = (self.d2[1] + self.d2[2] + self.d2[3] + self.d2[4])/4
        self.d3[5] = (self.d3[2] + self.d3[3] + self.d3[4])/3
        self.d4[5] = (self.d4[3] + self.d4[4])/2
        self.V[5] = (self.V[0] + self.V[1] + self.V[2] + self.V[3] + self.V[4])/5



    ## Публічні функції
    # Провести розрахунки всієї таблиці
    def calc(self):
        self.__find_alfa()
        self.__find_V()
        self.__find_fF()
        self.__find_average()
        self.__find_delta_V()
        self.__find_m()
        self.__draw_table()

    # Переводимо всі значення під номер в списку значення = значення * (spisk/100) + значення
    def normalize(self):
        for i in range(6):
            self.v[i] = self.v[i] * (self.spisk/100) + self.v[i]
            self.F[i] = self.F[i] * (self.spisk/100) + self.F[i]
            self.fF[i] = self.fF[i] * (self.spisk / 100) + self.fF[i]
            self.d1[i] = self.d1[i] * (self.spisk/100) + self.d1[i]
            self.d2[i] = self.d2[i] * (self.spisk/100) + self.d2[i]
            self.d3[i] = self.d3[i] * (self.spisk/100) + self.d3[i]
            self.d4[i] = self.d4[i] * (self.spisk/100) + self.d4[i]
            self.V[i] = self.V[i] * (self.spisk/100) + self.V[i]
        self.alfa = self.alfa * (self.spisk / 100) + self.alfa
        self.d = self.d * (self.spisk / 100) + self.d

    # заокруглити всі значення до 4 знаків після коми
    def round_values(self):
        for i in range(6):
            self.v[i] = round(self.v[i],5)
            self.F[i] = round(self.F[i],5)
            self.fF[i] = round(self.fF[i], 5)
            self.d1[i] = round(self.d1[i],5)
            self.d2[i] = round(self.d2[i],5)
            self.d3[i] = round(self.d3[i],5)
            self.d4[i] = round(self.d4[i],5)
            self.V[i] = round(self.V[i],5)
        self.d = round(self.d, 5)
        self.alfa = round(self.alfa, 5)
        self.m = round(self.m, 10)
        self.delta_V[5] = round(self.delta_V[5],5)


    # print table
    def print_table(self):
        text = "1. v: " + str(self.v[0]) + ", " + str(self.v[1])+ ", " + str(self.v[2]) + ", " + str(self.v[3]) + ", " + str(self.v[4]) + ", ser: " + str(self.v[5]) + "\n"
        text += "2. F: " + str(self.F[0]) + ", " + str(self.F[1])+ ", " + str(self.F[2]) + ", " + str(self.F[3]) + ", " + str(self.F[4]) + ", ser: " + str(self.F[5]) + "\n"
        text += "3. fF: " + str(self.fF[0]) + ", " + str(self.fF[1])+ ", " + str(self.fF[2]) + ", " + str(self.fF[3]) + ", " + str(self.fF[4]) + ", ser: " + str(self.fF[5]) + "\n"
        text += "4. d1: " + str(self.d1[0]) + ", " + str(self.d1[1])+ ", " + str(self.d1[2]) + ", " + str(self.d1[3]) + ", " + str(self.d1[4]) + ", ser: " + str(self.d1[5]) + "\n"
        text += "5. d2: " + "-" + ", " + str(self.d2[1])+ ", " + str(self.d2[2]) + ", " + str(self.d2[3]) + ", " + str(self.d2[4]) + ", ser: " + str(self.d2[5]) + "\n"
        text += "6. d3: " + "-" + ", " + "-"+ ", " + str(self.d3[2]) + ", " + str(self.d3[3]) + ", " + str(self.d3[4]) + ", ser: " + str(self.d3[5]) + "\n"
        text += "7. d4: " + "-" + ", " + "-"+ ", " + "-" + ", " + str(self.d4[3]) + ", " + str(self.d4[4]) + ", ser: " + str(self.d4[5]) + "\n"
        text += "8. d: " + str(self.d) + "\n"
        text += "9. alfa: " + str(self.alfa) + "\n"
        text += "10. V: " + str(self.V[0]) + ", " + str(self.V[1]) + ", " + str(self.V[2]) + ", " + str(self.V[3]) + ", " + str(self.V[4]) + ", ser: " + str(self.V[5]) + "\n\n"
        text += "Маса одиниці довжини струни m = (F/V^2)*d: " + str(self.m) + "\n"
        text += "Абсолютна похибка V: " + str(self.V[5]) + " +- " + str(self.delta_V[5]) + "\n"
        text += "Відносна похибка E: " + str(round((self.delta_V[5]/self.V[5])*100,5)) + "%\n"
        bot.send_message(self.message.chat.id, text)
        table = PrettyTable()
        table.field_names = ["No", "v", "F", "fF", "d1", "d2", "d3", "d4", "d", "alfa", "V"]
        for i in range(6):
            table.add_row(
                [i + 1 if i != 5 else "ser", self.v[i], self.F[i], self.fF[i], self.d1[i] if self.d1[i] != 0 else '-',
                 self.d2[i] if self.d2[i] != 0 else '-', self.d3[i] if self.d3[i] != 0 else '-',
                 self.d4[i] if self.d4[i] != 0 else '-', self.d if i == 2 else ' ', self.alfa if i == 2 else ' ',
                 self.V[i]])
        text = table.get_string()
        text += "\nМаса одиниці довжини струни m = (F/V^2)*d: " + str(self.m)
        text += "\nАбсолютна похибка V: " + str(self.V[5]) + " +- " + str(self.delta_V[5])
        text += "\nВідносна похибка E: " + str(round((self.delta_V[5] / self.V[5]) * 100, 5)) + "%\n"
        with open("phys_lab5/phys5t.txt", "w") as f:
            f.write(text)
            f.close()
        # send file phys5t.txt
        bot.send_document(self.message.chat.id, open("phys_lab5/phys5t.txt", "rb"))

    # show graph
    def show_graph(self):
        plt.savefig("phys_lab5/phys5g.png")
        #send image
        bot.send_photo(self.message.chat.id, open("phys_lab5/phys5g.png", "rb"))
        plt.close()

def handle_spisk(message):
    # якщо msg ціле число
    if not message.text.isdigit():
        bot.send_message(message.chat.id, 'Ви ввели не коректне значення')
        bot.send_message(message.chat.id, "Введіть цифру від -50 до 50\nСпробуйте ще раз /phys_lab5")
        return 0
    if not int(message.text) <= 50 or not int(message.text) >= -50:
        bot.send_message(message.chat.id, 'Ви ввели не коректне значення')
        bot.send_message(message.chat.id, "Введіть цифру від -50 до 50\nСпробуйте ще раз /phys_lab5")
        return 0
    bot.send_message(message.chat.id, 'Ви ввели коректне значення')
    spisk = int(message.text)
    print(str(message.chat.username) + ": Тільки що скачав лабу 5 варіант: "+ str(spisk))
    table = Solution(spisk,message)

    table.normalize()  # Переводимо значення під варіант
    table.calc()  # знаходимо невідомі
    table.round_values()  # Заокруглюємо значення до 4 цифр після коми
    table.print_table()  # Виводимо таблицю
    table.show_graph()