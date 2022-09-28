
from telebot import *
import telebot
import config
from pymongo import *

class Context:
    def __init__(self):
        self.rqStart = None
        self.rqRegisterStep1 = None
        self.rqRegisterStep2 = None
        self.rqMenu = None
        self.rqUserProfile = None
        self.rqNewTrain = None
        self.rqRequestCoachNewTraining = None
        self.rqRequestCoachNewTrainingMenu = None
        self.rqRequestCoachNewTrainingTime = None
        Config = config
        self.bot = telebot.TeleBot(Config.TOKEN)
        self.requests = []
        self.cluster =MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
        self.db = self.cluster['local'] #name of data base (cluster)
        #requests.append(self.rqStart)
    def add_request(self,r):
        self.requests.append(r)
        return r



      

