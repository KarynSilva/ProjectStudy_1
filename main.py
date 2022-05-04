from fastapi import FastAPI
from pydantic import BaseModel


class Food(BaseModel):
    name: str
    origination:str 
    created: str
    

app = FastAPI()

food_db = [{"name": "Panna Cotta", "origination":"Piemonte - Italy", "created":"20th century"},
{"name": "Croissant", "origination":"Viena - Austria", "created":"1683"},
{"name": "Capuccino", "origination":"Brasil", "created":"16th or 17th century"},
{"name": "Gianduia", "origination":"Piemonte - Italy", "created":"1806 - 19th century"},
{"name": "Crème brûlée", "origination":"France", "created":"17th century"},
{"name": "Macarons", "origination":"Veneto - Italy", "created":"16th century"}]

#listar
@app.get("/foods/")
async def read_food_list(skip:int = 0, limit:int=10):
    print("read_food_list\n")
    return food_db[skip : skip + limit]

#get by id
@app.get("/foods/{food_id}")
async def read_food(food_id: str):
    
    return food_db[int(food_id)]

#criar
@app.post("/foods/")
async def insert_food(food:Food):
    print("insert_food\n")
    food_db.append(food)
    return food

#editar
@app.put("/foods/{food_id}")
async def update_food(food_id: str, food: Food):
    print("update_food\n")
    results = {"food_id": food_id, "food": food}
    return food_db[int(food_id)]
    return results

@app.delete("/foods/{food_id}")
async def delete_food(food_id: str):
    print("delete_food")
    food_db.remove(food_id)
    return "ID:"+{"food_id": food_id}+" REMOVIDO!"


food_insert = {"name": "Pizza", "origination":"Campania - Italy", "created":"18th century"}
food_edit = {"name": "Capuccino", "origination":"Italy", "created":"16th or 17th century"}

read_food_list(2,3)
read_food("2")
#insert_food(food_insert)
#update_food("2",food_edit)
#delete_food("5")