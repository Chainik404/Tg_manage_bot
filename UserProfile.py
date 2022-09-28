from telebot import *


from RequestRegisterUserType import *
from user_db import *
from Context import *
from text import *

class UserProfile:

    def is_handler(self,message):
        return message.text == backtomenu or message.text == changeprofile

    def display (self,context, message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)  
        but1 = types.KeyboardButton(changeprofile)
        but2 = types.KeyboardButton(backtomenu)
        markup.add(but1, but2)
        context.bot.send_message(message.chat.id,"здесь что то будет".format(message.from_user, context.bot.get_me()),parse_mode='html', reply_markup=markup)
        
    def request(self,context,message):
        user = User
        
        if message.text == changeprofile:
            pass
            
        if message.text == backtomenu:
            
            context.rqMenu.display(context,message)





