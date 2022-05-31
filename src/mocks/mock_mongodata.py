import datetime, json
from api.app.models.food import Food
 
date_now = str(datetime.datetime.now())

class MockFoodRepository(): 
   
    food_db = []

    def __init__(self):
        self.food_db = [
                        {"_id":'0', "name": "Panna Cotta", "origination":"Piemonte - Italy", "created":"20th century","date": date_now},
                        {"_id":'1',"name": "Croissant", "origination":"Viena - Austria", "created":"1683","date": date_now},
                        {"_id":'2',"name": "Capuccino", "origination":"Brasil", "created":"16th or 17th century","date": date_now},
                        {"_id":'3',"name": "Gianduia", "origination":"Piemonte - Italy", "created":"1806 - 19th century","date": date_now},
                        {"_id":'4',"name": "Crème brûlée", "origination":"France", "created":"17th century","date": date_now},
                        {"_id":'5',"name": "Macarons", "origination":"Veneto - Italy", "created":"16th century","date": date_now}
                       ]


    def list(self):
        return (self.food_db)

    def create(self,food:Food):

        food_i = {"_id": str(len(self.food_db)),
                  "name": food.name,
                  "origination": food.origination,
                  "created": food.created,
                  "date": str(datetime.datetime.now())}

        self.food_db.append(food_i)
        

    def list_by_id(self,food_id : str):

        return self.food_db[int(food_id)]

    def edit(self,food:Food):
        
        food_i = {"_id": None,
                  "name": food.name,
                  "origination": food.origination,
                  "created": food.created,
                  "date": food.date}

        for i in range(len(self.food_db)):

            if(self.food_db[i]["name"]==food_i["name"]):
                food_id = self.food_db[i]["_id"]
                food_i["_id"] = self.food_db[i]["_id"]

        self.food_db[int(food_id)] = food_i

        return self.food_db

    def delete(self,food_id:str):
        
        self.food_db.pop(int(food_id))
        
        
    
    
