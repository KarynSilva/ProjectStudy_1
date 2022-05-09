import datetime,json
from pymongo import MongoClient
from fastapi import FastAPI,requests
from pydantic import BaseModel

app = FastAPI()


class Food(BaseModel):
    _id:str
    name: str
    origination:str 
    created: str
    date: str

    
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.FoodsDatabase
food_db = list(db.foodscoll.find())

@app.get("/foods/")
async def read_food_list(skip:int =0, limit:int=10):return food_db[skip : skip + limit]  

#criar
@app.post("/foods/")
async def create_food(food:Food):
    food.date = str(datetime.datetime.now())
    db.foodscoll._insert_one(food)
    return 'Data entered successfully,please list again to see it!'

#get by id
@app.get("/foods/{food_id}")
async def read_food(food_id: str):
    return food_db[int(food_id)]
#editar
@app.put("/foods/{food_id}")
async def update_food(food: Food):
    db.foodscoll.replace_one({"id_" : food.id},{"name":food.name,"origination":food.origination,
    "created":food.created,"date": str(datetime.datetime.now())})
    food_db = db.foodscoll
    return 'Data changed successfully,please list again to see it!'
    

@app.delete("/foods/{food_id}")
async def delete_food(food_id: str):
    db.foodscoll.delete_many({"id_":food_id})
    food_db = db.foodscoll
    return 'Data removed successfully,please list again to see it!'

food_insert = {"name": "Pizza",
        "origination": "Campania - Italy",
        "created": "18th century",
        "date": "None"
              }

food_edit =   {"name": "Capuccino",
        "origination": "Italy",
        "created": "16th or 17th century",
        "date": "None"
              }

