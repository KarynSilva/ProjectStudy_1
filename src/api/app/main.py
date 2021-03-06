import uvicorn
from fastapi import FastAPI, Depends
#from api.app.repositories.mongodata import FoodRepository as mrep # Official repository, connected at mongo # noqa
from mocks.mock_mongodata import MockFoodRepository as mrep # Repository "local" just to run the tests # noqa
from api.app.models.food import Food

app = FastAPI()

#Attention: integration tests referring to 'test_main_requests.py' also work with Official repository # noqa


@app.get("/foods/list", status_code=200)
def read_food_list(skip: int = 0, limit: int = 10,
                   repository: mrep = Depends(mrep)):

    Data = repository.list()
    return Data[skip: skip + limit]


@app.post("/foods/create", status_code=201)
def create_food(food: Food, repository: mrep = Depends(mrep)):
    repository.create(food)
    return 'Data entered successfully,please list again to see it!'


@app.get("/foods/list/{food_id}", status_code=200)
def read_food(food_id: str, repository: mrep = Depends(mrep)):

    return repository.list_by_id(food_id)


@app.put("/foods/edit/{food_id}", status_code=200)
def update_food(food: Food, repository: mrep = Depends(mrep)):

    repository.edit(food)
    return 'Data changed successfully,please list again to see it!'


@app.delete("/foods/delete/{food_id}", status_code=200)
def delete_food(food_id: str, repository: mrep = Depends(mrep)):

    repository.delete(food_id)
    return 'Data removed successfully,please list again to see it!'


if __name__ == "__main__":
    uvicorn.run(app=app)
