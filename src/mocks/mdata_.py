from os import remove
from api.app.models.food import Food
import datetime
import op_ as op

db_foodscoll = []

class MockFoodRepository(): 

    food_db = []

    def __init__(self):
        
        if(not db_foodscoll):
            db_foodscoll = op.Initial_Check
        self.food_db = db_foodscoll


    def list(self):
        
        return op.Cast_Many_to_Object(self.food_db)

    def create(self,food:Food):

        food_i = food.dict()
        food_i["_id"] = str(len(self.food_db))
        food_i["date"] = str(datetime.datetime.now())
        db_foodscoll.append(food_i)
        self.food_db = db_foodscoll

    def list_by_id(self, food_id : str):
        
        return op.Cast_One_to_Object(self.food_db[int(food_id)])

    def edit(self,food:Food):

        for i in range(len(self.food_db)):

            if(self.food_db[i]["name"]==food.name):
                food_id = self.food_db[i].get("_id")
                

        db_foodscoll.insert(food_id,{
                                  "_id" : food_id}, {"name":food.name, "origination":food.origination,
                                  "created":food.created, "date": str(datetime.datetime.now())
                                })
        self.food_db = db_foodscoll

    def delete(self,food_id:str):
        
        for i in range(len(db_foodscoll)):
            if(db_foodscoll[i]["_id"]== food_id):
                db_foodscoll.remove(db_foodscoll[i])
        self.food_db = db_foodscoll






