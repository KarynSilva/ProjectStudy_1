from pymongo import MongoClient
from api.app.models.food import Food
import datetime


client = MongoClient('mongodb://karyn:pass@mongo-project:27017/?authSource=admin&authMechanism=SCRAM-SHA-1', connect=True)
db = client.Foods

# nome de classes em python acaba seguindo o padrão do Java
# FoodRepository, tenho preferencia por usar no singular a entidade que está sendo persistida no repositorio
# Normalmente eu não coloco no nome das classes, funções ou metodos particularidades da implementação
# exemplo Mongo que é o banco de dados, ou int_codigo_cliente, somente em casos especificos.
# no futuro se você mudar a implementação de Mongo para Sql Server ou Postgres o FoodRepository se mantem valido.
# e mantemos a perspectiva do encapsulamento

class Mongo_Foods_Repository(): 

    food_db = []

    def __init__(self):
      self.food_db = list(db.foodscoll.find())
      # criaria uma variavel aqui
      # self.food_collection = db.foodscoll

    def list(self):

        # no sentido de o metodo ter somente uma responsabilidade, 
        # cria um outro arquivo fora do repositorio
        # que faz o insert inicial dos registros

        if(not self.food_db):
             date_now = str(datetime.datetime.now())
    
             f_list = [
                       {"_id":'0', "name": "Panna Cotta", "origination":"Piemonte - Italy", "created":"20th century","date": date_now},
                       {"_id":'1',"name": "Croissant", "origination":"Viena - Austria", "created":"1683","date": date_now},
                       {"_id":'2',"name": "Capuccino", "origination":"Brasil", "created":"16th or 17th century","date": date_now},
                       {"_id":'3',"name": "Gianduia", "origination":"Piemonte - Italy", "created":"1806 - 19th century","date": date_now},
                       {"_id":'4',"name": "Crème brûlée", "origination":"France", "created":"17th century","date": date_now},
                       {"_id":'5',"name": "Macarons", "origination":"Veneto - Italy", "created":"16th century","date": date_now}
                      ]
    
             db.foodscoll.insert_many(f_list)
             self.food_db = list(db.foodscoll.find()) 

        # itens = self.food_collection.find()
        # converte o dictionary em objeto do schema Food
        # 

        return self.food_db

    def create(self,food:Food):

        # é possivel usar o 
        #food.dict() para criar o dicionario food.dict()

        food_i = {
                  "_id": str(len(self.food_db)), "name": food.name, "origination": food.origination, "created": food.created,
                  "date": str(datetime.datetime.now())
                 }
        db.foodscoll.insert_one(food_i)
        self.food_db = list(db.foodscoll.find())

    def list_by_id(self, food_id : str):
        #
        return self.food_db[int(food_id)]

    def edit(self,food:Food):

        for i in range(len(self.food_db)):
            if(self.food_db[i]["name"]==food.name):
                food_id = self.food_db[i].get("_id")
                
        db.foodscoll.replace_one({
                                  "_id" : food_id}, {"name":food.name, "origination":food.origination,
                                  "created":food.created, "date": str(datetime.datetime.now())
                                })
        self.food_db = list(db.foodscoll.find())

    def delete(self,food_id:str):
        db.foodscoll.delete_many({"_id":food_id})
        self.createfood_db = list(db.foodscoll.find())


        

