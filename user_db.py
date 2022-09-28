from typing import Collection
import pymongo
from pymongo import MongoClient
from pymongo import *
from pymongo import collection
from Context import *
from json import *
from telebot import *



cluster =MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
context = Context

class User:
    def __init__(self,message):
        self.id = message.from_user.id 
        
        db = cluster['local'] #name of data base (cluster)
        Collection =db['clients'] #name of collection
        self.type = 0
        self.step = 0
        self.ocupation = 'N.D.'
        self.trainings = []
        self.col = Collection# change to config 
        
        self.results = Collection.find_one({"Tg_id":self.id})

        if self.results != None:
            self.is_new = False
            self.step = self.results.get("step")
            self.ocupation = self.results.get("Ocupation")
            self.type = self.results.get("Type")
            # self.trainings = self.results.get("traiings_id")
        else:
            self.is_new = True
            
    
            
            

    def save(self):
        if self.is_new:

            db = cluster['local'] #name of data base (cluster)
            self.Col =db['clients'] #name of collection
            user = {"Tg_id": self.id, "step": self.step} #"name": name, "status": status, "ocupation": ocupation} #user example
            self.Col.insert_one(user) # add one user   
            self.is_new = False
        else:
            a = 1
    def add_training(self,train_id):
        
        
        self.trainings.append(train_id)
        self.col.update_one({"_id": self.id },{"$set": {"trainings_id":self.trainings}}, upsert=True)

        #collection.update_one({search parametr},{change/add parametr})
        #Collection.update_one({"_id": 10 },{"$set": {"name": "lo"}}, upsert=True)
    
        

    def find_by_id(id):
        results = Collection.find_one({"Tg_id":id})
        print(results)
            
    def find_by_name(name): 
        results = Collection.find_one({"name":name})
        print(results)
    
    


#User.add_one(10,"bob",5)
#User.add_one(12,"tod",10)
#User.add_one(16,"lufy",15)
#User.find_by_id(10)
#User.find_by_name("tod")
#User.find_by_score(15)


