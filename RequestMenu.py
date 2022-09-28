from telebot import *



from RequestRegisterUserType import *
from user_db import *
from Context import *
from text import *
from RequestCoachNewTraining import *

class RequestMenu:

    def is_handler(self,message):
        
        return message.text == schedule or message.text == myprofile or message.text == findtrain or message.text == findcoach or message.text == createtrain


    def display (self,context, message):
        user = User(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)  
        but1 = types.KeyboardButton(myprofile)
        but2 = types.KeyboardButton(schedule)
        but3 = types.KeyboardButton(findtrain)
        but4 = types.KeyboardButton(findcoach)
        but5 = types.KeyboardButton(createtrain)
        if user.type == 1:
            but1 = types.KeyboardButton(myprofile)
            but2 = types.KeyboardButton(schedule)
            but3 = types.KeyboardButton(createtrain)
            but4 = types.KeyboardButton(mytrain)
        markup.add(but1, but2, but3, but4, but5)
        context.bot.send_message(message.chat.id,"вот вы и зарегестрировались, {0.first_name}\n. что ж я жду ваши запросы".format(message.from_user, context.bot.get_me()),parse_mode='html', reply_markup=markup)
    def request(self,context,message):
        
        user=User
        # user.step = 3
        if message.text == myprofile:
            context.rqUserProfile.display(context,message)
        if message.text == schedule:
            pass
            # context.rqNewTrain.display(context,message)
        if message.text == createtrain:
            context.rqRequestCoachNewTrainingMenu.display(context,message)



