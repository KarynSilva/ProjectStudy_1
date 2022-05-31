import datetime
from api.app.models.food import Food
 
date_now = str(datetime.datetime.now())

class MockFoodRepository(): 
    global food_db 

    food_db =[
                 {"_id":'0', "name": "Panna Cotta", "origination":"Piemonte - Italy", "created":"20th century","date": date_now},
                 {"_id":'1',"name": "Croissant", "origination":"Viena - Austria", "created":"1683","date": date_now},
                 {"_id":'2',"name": "Capuccino", "origination":"Brasil", "created":"16th or 17th century","date": date_now},
            {"_id":'3',"name": "Gianduia", "origination":"Piemonte - Italy", "created":"1806 - 19th century","date": date_now},
            {"_id":'4',"name": "Crème brûlée", "origination":"France", "created":"17th century","date": date_now},
            {"_id":'5',"name": "Macarons", "origination":"Veneto - Italy", "created":"16th century","date": date_now}
                           ]
    def __init__():
        pass


    def list():
        return (food_db)

    def create(food:Food):
        food["_id"] = str(len(food_db))
        food["date"] = date_now
        food_db.append(food)
        

    def list_by_id(food_id : str):
        return food_db[int(food_id)]

    def edit(food:Food):
    
        food_db[int(food["_id"])] = food
        return food_db

    def delete(food_id:str):
        food_db.pop(int(food_id))
        
        
    
    
