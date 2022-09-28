from telebot import *



from RequestRegisterUserType import *
from user_db import *
from Context import *
from text import *


class RequestNewTrain:

    def is_handler(self,message):
        
       return message.text == backtomenu, message.text == schedule, 


    def display (self,context, message):
       
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)  
        but1 = types.KeyboardButton(backtomenu)
        but2 = types.KeyboardButton(schedule)
        but3 = types.KeyboardButton(findtrain)
        but4 = types.KeyboardButton(findcoach)

    def request(self,context,message):
        pass


