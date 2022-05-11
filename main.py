import datetime
from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel
import operations as op

app = FastAPI()


class Food(BaseModel):
    _id:str
    name: str
    origination:str 
    created: str
    date: str



client = MongoClient('mongodb://karyn:pass@localhost:27017/?authSource=admin&authMechanism=SCRAM-SHA-1', connect=True)
db = client.Foods


@app.get("/foods/")
def read_food_list(skip:int =0, limit:int=10):

    food_db = list(db.foodscoll.find())
    if(not food_db):
        op.start() 
        food_db = list(db.foodscoll.find())
    return food_db[skip : skip + limit]  

#criar
@app.post("/foods/")
def create_food(food:Food):

    food_db = list(db.foodscoll.find())
    food_i = {"_id": str(len(food_db)),"name": food.name,"origination": food.origination,"created": food.created,
    "date": str(datetime.datetime.now())}
    db.foodscoll.insert_one(food_i)
    return 'Data entered successfully,please list again to see it!'

#get by id
@app.get("/foods/{food_id}")
def read_food(food_id: str):

    food_db = list(db.foodscoll.find())
    return food_db[int(food_id)]
#editar
@app.put("/foods/{food_id}")
def update_food(food: Food):

    food_db = list(db.foodscoll.find())
    for i in range(len(food_db)):
        if(food_db[i]["name"]==food.name):
            food_id = food_db[i].get("_id")

    db.foodscoll.replace_one({"_id" : food_id},{"name":food.name,"origination":food.origination,
    "created":food.created,"date": str(datetime.datetime.now())})

    return 'Data changed successfully,please list again to see it!'
    

@app.delete("/foods/{food_id}")
def delete_food(food_id: str):
    food_db = list(db.foodscoll.find())
    db.foodscoll.delete_many({"_id":food_id})
    food_db = db.foodscoll.find()
    return 'Data removed successfully,please list again to see it!'



'''
food_insert = {"_id":"None","name": "Pizza",
        "origination": "Campania - Italy",
        "created": "18th century",
        "date": "None"
              }

food_edit =   {"_id":"2","name": "Capuccino",
        "origination": "Italy",
        "created": "16th or 17th century",
        "date": "None"
              }

'''