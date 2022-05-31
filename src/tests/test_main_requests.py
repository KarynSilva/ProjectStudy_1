from fastapi.testclient import TestClient
from api.app.main import app
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
    
