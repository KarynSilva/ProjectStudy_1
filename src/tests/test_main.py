from fastapi.testclient import TestClient
from api.app.main import app, read_food_list, read_food, create_food, update_food, delete_food
from mocks.mock_mongodata import MockFoodRepository as mrep
import json


client = TestClient(app)


def test_list_all():

    response = client.get("/foods/list")
    assert response.status_code == 200
    
def test_getbyid():

    response = client.get(
        "/foods/list/3",        
    )
    assert response.status_code == 200

def test_createfood():

    response = client.post(
        "/foods/create",
        json.dumps({"_id":"None","name": "Pizza",
        "origination": "Campania - Italy",
        "created": "18th century",
        "date": "None"
              }, indent=2)
    )
    assert response.status_code == 201
   

def test_editfood():

    response = client.put(
        "/foods/edit/2",
        json.dumps({"_id":"2","name": "Capuccino",
        "origination": "Italy",
        "created": "16th or 17th century",
        "date": "None"
              }, indent=2)
    )
    assert response.status_code == 200
    

def test_deletefood():

    response = client.delete(
    "/foods/delete/4",
    )
    assert response.status_code == 200
    

def test_read_food_list():

    data_test = []
    data_test = read_food_list(0,10,mrep)
    flag = (not data_test)
    assert flag == False

def test_read_food():

    data_test = None
    data_test = read_food(1,mrep)
    assert (data_test == None) == False
    

def test_create_food():

    food_insert = {"_id":"None","name": "Pizza",
                   "origination": "Campania - Italy",
                   "created": "18th century",
                   "date": "None"
                  }
    data_test = None
    data_test = create_food(food_insert,mrep)
    assert data_test == 'Data entered successfully,please list again to see it!'

def test_update_food():

    data_test= None
    food_edit =   {"_id":"2","name": "Capuccino",
                   "origination": "Italy",
                   "created": "16th or 17th century",
                   "date": "None"
                  }
    data_test = update_food(food_edit,mrep)
    assert data_test == 'Data changed successfully,please list again to see it!'

def test_delete_food():

    data_test = None
    data_test = delete_food("4", mrep)
    assert data_test == 'Data removed successfully,please list again to see it!'



