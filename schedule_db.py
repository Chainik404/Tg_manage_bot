from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from Context import *
from pymongo import *
from user_db import *
from uuid import *
context = Context

# cl = context.cluster
class schedule_db:
    def __init__(self):
        self.id = str(uuid4())  
        db = cluster['local'] #name of data base (cluster)
        self.Collection =db['schedule'] #name of collection
        
 
        self.date = 0
        self.type = 0
        self.duration = 0
        self.sport_type = 0
        self.plase = 'N.D.'
        self.prise = 0
        self.coach = 'N.D.'
        # self.coach = 0  how take coach???
        #.... more variables ???
        results = self.Collection.find_one({"train_id":self.id})

        if results != None:
            self.is_new = False
            self.step = results.get("step")
            self.ocupation = results.get("Ocupation")
            self.type = results.get("Type")
        else:
            self.is_new = True
            
    
            
            

    def save(self,message):
        # if self.is_new:
        user = User(message)
        db = cluster['local'] #name of data base (cluster)
        self.Collection = db['schedule'] #name of collection
        training = {"_id": self.id, "date": self.date,"coach": self.coach} #"name": name, "status": status, "ocupation": ocupation} #user example
        self.Collection.insert_one(training) # add one user 
        user.trainings.append(self.id)
        user.col.update_one({"Tg_id": user.id },{"$set": {"trainings_id":user.trainings}}, upsert=True)  
        # self.is_new = False
        # else:
        #     a = 1