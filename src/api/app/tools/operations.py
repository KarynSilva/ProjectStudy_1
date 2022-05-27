from pymongo import MongoClient
from collections import namedtuple
import datetime

client = MongoClient('mongodb://karyn:pass@mongo-project:27017/?authSource=admin&authMechanism=SCRAM-SHA-1', connect=True)
db = client.Foods
f_list = []
food_db = []

def Initial_Check():

    food_db = list(db.foodscoll.find())

    if(not food_db):

        date_now = str(datetime.datetime.now())
        f_list = [
                {"_id":'0', "name": "Panna Cotta", "origination":"Piemonte - Italy", "created":"20th century","date": date_now},
                {"_id":'1',"name": "Croissant", "origination":"Viena - Austria", "created":"1683","date": date_now},
                {"_id":'2',"name": "Capuccino", "origination":"Brasil", "created":"16th or 17th century","date": date_now},
                {"_id":'3',"name": "Gianduia", "origination":"Piemonte - Italy", "created":"1806 - 19th century","date": date_now},
                {"_id":'4',"name": "Crème brûlée", "origination":"France", "created":"17th century","date": date_now},
                {"_id":'5',"name": "Macarons", "origination":"Veneto - Italy", "created":"16th century","date": date_now}
                 ]
    
        db.foodscoll.insert_many(f_list)

def Cast_Many_to_Object(food_list:list):

    food_objects = []

    for i in range(len(food_list)):

        obj = namedtuple("Food", food_list[i].keys(), rename=True)(*food_list[i].values())
        food_objects.append(obj)

    return food_objects 

def Cast_One_to_Object(food_item):

    obj_one = namedtuple("Food", food_item.keys(), rename=True)(*food_item.values())

    return obj_one

