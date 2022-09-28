from telebot import *

#from pyTelegramBotAPI import *
# import Settings

from requests.models import Response
import random
import user_db
from RequestRegisterStart import *
from RequestRegisterUserType import *
from RequestRegisterOcupation import *
from RequestNewTrain import *
from RequestMenu import *
from UserProfile import *
from RequestCoachNewTraining import *
from RequestCoachNewTrainingMenu import *
from RequestCoachNewTrainingTime import *
#from request_2 import *
from Context import *

context = Context()
context.rqStart = context.add_request(RequestRegisterStart())
context.rqRegisterStep1 = context.add_request(RequestRegisterUserType())
context.rqRegisterStep2 = context.add_request(RequestRegisterOcupation())
context.rqMenu = context.add_request(RequestMenu())
context.rqUserProfile = context.add_request(UserProfile())
context.rqRequestCoachNewTraining = context.add_request(RequestCoachNewTraining())
context.rqRequestCoachNewTrainingMenu = context.add_request(RequestCoachNewTrainingMenu())
context.rqRequestCoachNewTrainingTime = context.add_request(RequestCoachNewTrainingTime())
context.rqNewTraining  = RequestNewTrain
# context.bot.remove_webhook()
#bot.remove_webhook()

@context.bot.message_handler()
def welcome(message):
    for r in context.requests: 
        if r.is_handler(message):
            r.request(context,message) 
            break
@context.bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def callback(callback):
        RequestCoachNewTraining.callback(callback,callback)


context.bot.polling(none_stop=True)









