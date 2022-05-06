import json
from fastapi import FastAPI,requests
from pydantic import BaseModel


class Food(BaseModel):
    id:str
    name: str
    origination:str 
    created: str
    

app = FastAPI()

food_default = {"id": "None","name": "None", "origination":"None", "created":"None"}

food_db = [{"id": "0","name": "Panna Cotta", "origination":"Piemonte - Italy", "created":"20th century"},
{"id": "1","name": "Croissant", "origination":"Viena - Austria", "created":"1683"},
{"id": "2","name": "Capuccino", "origination":"Brasil", "created":"16th or 17th century"},
{"id": "3","name": "Gianduia", "origination":"Piemonte - Italy", "created":"1806 - 19th century"},
{"id": "4","name": "Crème brûlée", "origination":"France", "created":"17th century"},
{"id": "5","name": "Macarons", "origination":"Veneto - Italy", "created":"16th century"}]

#listar
@app.get("/foods/")
async def read_food_list(skip:int = 0, limit:int=10):return food_db[skip : skip + limit]  
#criar
@app.post("/foods/")
async def create_food(food:Food):
    food.id = len(food_db)
    food_db.append(food)
    return 'Data entered successfully,please list again to see it!'
#get by id
@app.get("/foods/{food_id}")
async def read_food(food_id: str):return food_db[int(food_id)]
#editar
@app.put("/foods/{food_id}")
async def update_food(food: Food):
    food_db[int(food.id)] = food
    return 'Data changed successfully,please list again to see it!'
    

@app.delete("/foods/{food_id}")
async def delete_food(food_id: str):
    food_default.update({"id": food_id})
    food_db[int(food_id)]= food_default
    return 'Data removed successfully,please list again to see it!'

food_insert = {
        "id":"None",
        "name": "Pizza",
        "origination": "Campania - Italy",
        "created": "18th century"
              }

food_edit =   {
        "id":"1",
        "name": "Capuccino",
        "origination": "Italy",
        "created": "16th or 17th century"
              }
