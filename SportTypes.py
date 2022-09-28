from typing import Collection
import pymongo
from pymongo import MongoClient
from pymongo import *
from Context import *


cluster =MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
context = Context

class SportTypes:
    def __init__(self):
        db = cluster['local'] #name of data base (cluster)
        self.Collection =db['SpotTypes'] #name of collection
        
        