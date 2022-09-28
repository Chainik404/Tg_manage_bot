
from cgitb import text
from distutils.command.config import config
from email import message
from secrets import choice
from tkinter import E
from unittest import result
from telebot import *
from user_db import *
from Context import *
from text import *
from datetime import datetime
from datetime import *
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from telegram_bot_calendar import *
from RequestCoachNewTrainingMenu import *
from schedule_db import *
from config import *
Config = config
bot = telebot.TeleBot(Config.TOKEN)
sd = schedule_db()
class RequestCoachNewTraining():
    def is_handler(self,message):
        return message.text == "y"or message.text == "yes" or message.text == "YES" or message.text == "NO" or message.text == "N" or message.text == "no"

    def display(self,context,message):
        calendar, step = WMonthTelegramCalendar().build()
        context.bot.send_message(message.chat.id,
                        f"Select {LSTEP[step]}",
                        reply_markup=calendar)
        user = User(message)
        user.step = 4
        user.col.update_one({"Tg_id": message.chat.id },{"$set": {"step":user.step}}, upsert=True)
    def callback(self,callback):
        result, key, step = WMonthTelegramCalendar().process(callback.data)
        
        if not result and key:
            bot.edit_message_text(f"Select {LSTEP[step]}",  
                                callback.message.chat.id,
                                callback.message.message_id,
                            reply_markup=key)

        elif result:
            sd.date = str(result)
            d = datetime.today().strftime('%d') # take today's day
            m = datetime.today().strftime('%m') # take today's month
            d1 = result.strftime('%d')
            m1= result.strftime('%m')
            print(d1,"- date ", m1 ,"-month") # choosen date and month 
            print(d,"- date", m,"-month") # today 's day and month
            if m < m1:
                bot.edit_message_text(f"You selected {result} is it right? Y/N",
                            callback.message.chat.id,
                            callback.message.message_id) 
            elif m == m1:
                if d < d1:  

                     bot.edit_message_text(f"You selected {result} is it right? Y/N",
                            callback.message.chat.id,
                            callback.message.message_id)
                elif d == d1: 
                    bot.edit_message_text(f"You selected {result} is it right? Y/N",
                            callback.message.chat.id,
                            callback.message.message_id)
                else:
                    bot.edit_message_text(f"You selected {result} this date hapend in next year are you shure? Y/N",
                            callback.message.chat.id,
                            callback.message.message_id)
            else:
               bot.edit_message_text(f"You selected {result} this date hapend in next year are you shure? Y/N",
                            callback.message.chat.id,
                            callback.message.message_id)
           



           
            
            
    def request(self,context,message):
        user = User(message)
        
        if user.step == 4 :
            if message.text == "y"or "yes" or "YES":
                sd.coach = user.results
                
                sd.save(message)
                context.rqRequestCoachNewTrainingMenu.display(context,message)

            elif message.text == "NO" or "N" or "no":
                context.rqRequestCoachNewTraining.display(context,message)
            
        
       
        