from telebot import *


from RequestRegisterUserType import *
from user_db import *
from Context import *
from text import *


class RequestRegisterOcupation:

    def is_handler(self,message):
        return message.text == volleyboll or message.text == basketball

    def display (self,context, message):

        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)  
        but1 = types.KeyboardButton(volleyboll)
        but2 = types.KeyboardButton(basketball)
        markup.add(but1, but2)
        context.bot.send_message(message.chat.id,"отлично, допро пожаловать игрок-{0.first_name}\n. Однако я все еще не знаю во что вы играете".format(message.from_user, context.bot.get_me()),parse_mode='html', reply_markup=markup)
    
    def request(self,context,message):
        user = User(message)
        user.step = 2
        
        user.ocupation = message.text
        user.col.update_one({"Tg_id": message.chat.id },{"$set": {"Ocupation":user.ocupation}}, upsert=True)
        user.col.update_one({"Tg_id": message.chat.id },{"$set": {"step":user.step}}, upsert=True)
        context.rqMenu.display(context,message)
        





