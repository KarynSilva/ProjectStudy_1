from pymongo import MongoClient
from api.app.models.food import Food
import datetime


client = MongoClient('mongodb://karyn:pass@mongo-project:27017/?authSource=admin&authMechanism=SCRAM-SHA-1', connect=True)
db = client.Foods
food_db = []


class operations():
    def __init__(self):
        self = None
    def start(self):
        date_now = str(datetime.datetime.now())
    
        f_list = [{"_id":'0', "name": "Panna Cotta", "origination":"Piemonte - Italy", "created":"20th century","date": date_now},
        {"_id":'1',"name": "Croissant", "origination":"Viena - Austria", "created":"1683","date": date_now},
        {"_id":'2',"name": "Capuccino", "origination":"Brasil", "created":"16th or 17th century","date": date_now},
        {"_id":'3',"name": "Gianduia", "origination":"Piemonte - Italy", "created":"1806 - 19th century","date": date_now},
        {"_id":'4',"name": "Crème brûlée", "origination":"France", "created":"17th century","date": date_now},
        {"_id":'5',"name": "Macarons", "origination":"Veneto - Italy", "created":"16th century","date": date_now}]
        db.foodscoll.insert_many(f_list)
    def update(self):
        food_db = list(db.foodscoll.find())

op = operations()

class Mongo_Foods_Repository():
    def __init__(self):
        food_db = list(db.foodscoll.find())
        if(not food_db):
            op.start(None) 
            op.update(None)
    def list(self):
        return food_db

    def create(self,food:Food):
        food_i = {"_id": str(len(food_db)),"name": food.name,"origination": food.origination,"created": food.created,
        "date": str(datetime.datetime.now())}
        db.foodscoll.insert_one(food_i)
        op.update(None)

    def list_by_id(self, food_id : str):
        return food_db[int(food_id)]

    def edit(self,food:Food):
        for i in range(len(food_db)):
            if(food_db[i]["name"]==food.name):
                food_id = food_db[i].get("_id")
        db.foodscoll.replace_one({"_id" : food_id},{"name":food.name,"origination":food.origination,
        "created":food.created,"date": str(datetime.datetime.now())})
        op.update(None)

    def delete(self,food_id:str):
        db.foodscoll.delete_many({"_id":food_id})
        op.update(None)


        

