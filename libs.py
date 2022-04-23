from private import firebaseConfig, BotToken
import os
import pyrebase
import telebot
from PIL import Image
import random
import schedule
import time as tm
from threading import Thread
import datetime
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import zipfile as ZipFile
bot = telebot.TeleBot(BotToken)
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()