from pymongo import MongoClient
from api.app.models.food import Food
import datetime
from api.app.tools import operations

#docker mongo connection
#client = MongoClient('mongodb://karyn:pass@mongo-project:27017/?authSource=admin&authMechanism=SCRAM-SHA-1', connect=True)

#mongo local for tests connection
client = MongoClient('mongodb://localhost:27018/?readPreference=primary&ssl=false', connect=True)

db = client.Foods

class FoodRepository(): 

    food_db = []

    def __init__(self):
        
        operations.Initial_Check()
        self.food_collection = db.foodscoll
        self.food_db = list(self.food_collection.find())

    def list(self):
        
        return operations.Cast_Many_to_Object(list(self.food_collection.find()))

    def create(self,food:Food):

        food_i = food.dict()
        food_i["_id"] = str(len(self.food_db))
        food_i["date"] = str(datetime.datetime.now())
        db.foodscoll.insert_one(food_i)
        self.food_db = list(self.food_collection.find())

    def list_by_id(self, food_id : str):
        
        return operations.Cast_One_to_Object(self.food_db[int(food_id)])

    def edit(self,food:Food):
        
        for i in range(len(self.food_db)):

            if(self.food_db[i]["name"]==food.name):
                food_id = self.food_db[i].get("_id")
                

        db.foodscoll.replace_one({
                                  "_id" : food_id}, {"name":food.name, "origination":food.origination,
                                  "created":food.created, "date": str(datetime.datetime.now())
                                })
        self.food_db = self.food_collection.find()

    def delete(self,food_id:str):

        db.foodscoll.delete_many({"_id":food_id})
        self.food_db = list(self.food_collection.find())


        

