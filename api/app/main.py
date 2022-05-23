import uvicorn
from fastapi import FastAPI,Depends
from api.app.repositories.mongodata import Mongo_Foods_Repository as mrep
from api.app.models.food import Food

app = FastAPI()


@app.get("/foods/", status_code=200)
def read_food_list(skip:int =0, limit:int=10, repository: mrep = Depends(mrep)):
    Data =repository.list()
    return Data[skip : skip + limit]  


@app.post("/foods/", status_code=201)
def create_food(food:Food, repository: mrep = Depends(mrep)):
   repository.create(food)
   return 'Data entered successfully,please list again to see it!'


@app.get("/foods/{food_id}", status_code=200)
def read_food(food_id: str, repository: mrep = Depends(mrep)):
    return repository.list_by_id(food_id)


@app.put("/foods/{food_id}", status_code=200)
def update_food(food: Food, repository: mrep = Depends(mrep)):
    
    repository.edit(food)
    return 'Data changed successfully,please list again to see it!'
    
@app.delete("/foods/{food_id}", status_code=200)
def delete_food(food_id: str, repository: mrep = Depends(mrep)):
    repository.delete(food_id)
    return 'Data removed successfully,please list again to see it!'

if __name__ == "__main__":
    uvicorn.run(app=app)