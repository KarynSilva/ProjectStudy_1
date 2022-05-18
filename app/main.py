import datetime
from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.testclient import TestClient
import app.operations as op

app = FastAPI()
client = TestClient(app)

class Food(BaseModel):
    _id:str
    name: str
    origination:str 
    created: str
    date: str



client = MongoClient('mongodb://karyn:pass@mongo-project:27017/?authSource=admin&authMechanism=SCRAM-SHA-1', connect=True)
db = client.Foods


@app.get("/foods/", status_code=200)
def read_food_list(skip:int =0, limit:int=10):

    food_db = list(db.foodscoll.find())
    if(not food_db):
        op.start() 
        food_db = list(db.foodscoll.find())
    return food_db[skip : skip + limit]  

#criar
@app.post("/foods/", status_code=201)
def create_food(food:Food):

    food_db = list(db.foodscoll.find())
    food_i = {"_id": str(len(food_db)),"name": food.name,"origination": food.origination,"created": food.created,
    "date": str(datetime.datetime.now())}
    db.foodscoll.insert_one(food_i)
    return 'Data entered successfully,please list again to see it!'

#get by id
@app.get("/foods/{food_id}", status_code=200)
def read_food(food_id: str):

    food_db = list(db.foodscoll.find())
    return food_db[int(food_id)]
#editar
@app.put("/foods/{food_id}", status_code=200)
def update_food(food: Food):

    food_db = list(db.foodscoll.find())
    for i in range(len(food_db)):
        if(food_db[i]["name"]==food.name):
            food_id = food_db[i].get("_id")

    db.foodscoll.replace_one({"_id" : food_id},{"name":food.name,"origination":food.origination,
    "created":food.created,"date": str(datetime.datetime.now())})

    return 'Data changed successfully,please list again to see it!'
    

@app.delete("/foods/{food_id}", status_code=200)
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

def test_initial_data():
    response = client.get("/foods/")
    assert response.status_code == 200
    data = response.json()
    
    assert data[0]["name"] == "Panna Cotta"
    assert data[1]["name"] == "Croissant"
    assert data[2]["name"] == "Capuccino"
    assert data[3]["name"] == "Gianduia"
    assert data[4]["name"] == "Crème brûlée"
    assert data[5]["name"] == "Macarons"
    assert data[0]["origination"] == "Piemonte - Italy"
    assert data[1]["origination"] == "Viena - Austria"
    assert data[2]["origination"] == "Brasil"
    assert data[3]["origination"] == "Piemonte - Italy"
    assert data[4]["origination"] == "France"
    assert data[5]["origination"] == "Veneto - Italy"
    assert data[0]["created"] == "20th century"
    assert data[1]["created"] == "1683"
    assert data[2]["created"] == "16th or 17th century"
    assert data[3]["created"] == "1806 - 19th century"
    assert data[4]["created"] == "17th century"
    assert data[5]["created"] == "16th century"
    
def test_getbyid():
    response = client.get(
        "/foods/{food_id}/",
        food_id = "3"         
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Gianduia"
    assert data["origination"] == "Piemonte - Italy"
    assert data["created"] == "1806 - 19th century"
    

def test_create_food():
    response = client.post(
        "/foods/",
        json={"_id":"None","name": "Pizza",
        "origination": "Campania - Italy",
        "created": "18th century",
        "date": "None"
              },
    )
    assert response.status_code == 201
    assert response == 'Data entered successfully,please list again to see it!'

def test_edit_food():
    response = client.put(
        "/foods/{food_id}/",
        json={"_id":"2","name": "Capuccino",
        "origination": "Italy",
        "created": "16th or 17th century",
        "date": "None"
              },
    )
    assert response.status_code == 200
    assert response == 'Data changed successfully,please list again to see it!'

def test_delete_food():
    response = client.delete(
    food_id = "4"
    )
    assert response.status_code == 200
    assert response == 'Data removed successfully,please list again to see it!'