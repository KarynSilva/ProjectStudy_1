import datetime,json
from pymongo import MongoClient


client = MongoClient('mongodb://karyn:pass@localhost:27017/?authSource=admin&authMechanism=SCRAM-SHA-1', connect=True)
db = client.Foods

date_now ="None"


def start():
    date_now = str(datetime.datetime.now())
    
    f_list = [{"_id":'0', "name": "Panna Cotta", "origination":"Piemonte - Italy", "created":"20th century","date": date_now},
    {"_id":'1',"name": "Croissant", "origination":"Viena - Austria", "created":"1683","date": date_now},
    {"_id":'2',"name": "Capuccino", "origination":"Brasil", "created":"16th or 17th century","date": date_now},
    {"_id":'3',"name": "Gianduia", "origination":"Piemonte - Italy", "created":"1806 - 19th century","date": date_now},
    {"_id":'4',"name": "Crème brûlée", "origination":"France", "created":"17th century","date": date_now},
    {"_id":'5',"name": "Macarons", "origination":"Veneto - Italy", "created":"16th century","date": date_now}]
    
    db.foodscoll.insert_many(f_list)

