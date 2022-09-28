
from telebot import *


import user_db 
from RequestRegisterUserType import *
from RequestRegisterOcupation import *
from user_db import *
from Context import *
from text import *
class RequestRegisterUserType:
    
    def is_handler(self,message):
        return message.text == icoach or message.text == iplayer
        
    def display(self,context, message):
        context.bot.send_sticker(message.chat.id, welcome_stiker)
        buton_line = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
        but1 = types.KeyboardButton(icoach)
        but2 = types.KeyboardButton(iplayer)
        buton_line.add(but1, but2)
        context.bot.send_message(message.chat.id, 'добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот-менеджер созданный чтобы автоматизировать рутину людей.'.format(message.from_user, context.bot.get_me()),parse_mode='html', reply_markup = buton_line)
        context.bot.send_message(message.chat.id, 'могу ли я узнать, вы игрок или же тренер'.format(message.from_user, context.bot.get_me()),parse_mode='html', reply_markup = buton_line)


    def request(self,context,message):
        # buton_line = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
        # but3 = types.KeyboardButton('перезагрузка')
        # buton_line.add(but3)
        #user_tg_id = user.id 
        user = User(message)
        user.type = 1
        user.step = 1
        user.col.update_one({"Tg_id": message.chat.id },{"$set": {"step":user.step}}, upsert=True)
        if message.text == icoach:
            user.type  = 1
            user.col.update_one({"Tg_id": message.chat.id },{"$set": {"Type":coach}}, upsert=True)
        elif message.text == iplayer:
            user.type = 2
            user.col.update_one({"Tg_id": message.chat.id },{"$set": {"Type":player}}, upsert=True)
        else:
            a = 1
        
           
        
        context.rqRegisterStep2.display(context,message)
     