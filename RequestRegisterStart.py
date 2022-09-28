
from telebot import *
from base_request import BaseRequest
import user_db 
from user_db import *
from Context import *
from text import *
 
class RequestRegisterStart(BaseRequest):
    
    def is_handler(self,message):
        return message.text == "/start"
        

    def request(self,context,message):
        
        user = User(message)
        # user.step = 0
        user.save()  
        if user.step == 0:
            
            context.rqRegisterStep1.display(context,message)

        if user.step == 1 :
            context.rqRegisterStep2.display(context,message)

        if user.step == 2 or user.step > 2 :
            context.rqMenu.display(context,message)

        

        
        
       
            #else:
                #bot.send_message(message.chat.id, 'даже не знаю что ответить')


        # buton_line = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
        # but3 = types.KeyboardButton('перезагрузка')
        # buton_line.add(but3)
        