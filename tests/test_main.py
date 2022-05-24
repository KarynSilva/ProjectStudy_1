from fastapi.testclient import TestClient
from api.app.main import app

client = TestClient(app)

def test_initialdata():
    response = client.get("/foods/")
    assert response.status_code == 200
    data = list(response.json())
    assert len(data) == 6
    assert data[0]["name"] == "Panna Cotta"
    assert data[0]["origination"] == "Piemonte - Italy"
    assert data[0]["created"] == "20th century"
    
def test_getbyid():
    response = client.get(
        "/foods/{food_id}/",
        food_id = "3"         
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Gianduia"
    assert data["origination"] == "Piemonte - Italy"
    assert data["created"] == "1806 - 19th century"
    

def test_createfood():
    response = client.post(
        "/foods/",
        json={"_id":"None","name": "Pizza",
        "origination": "Campania - Italy",
        "created": "18th century",
        "date": "None"
              },
    )
    assert response.status_code == 201
    assert response == 'Data entered successfully,please list again to see it!'

def test_editfood():
    response = client.put(
        "/foods/{food_id}/",
        json={"_id":"2","name": "Capuccino",
        "origination": "Italy",
        "created": "16th or 17th century",
        "date": "None"
              },
    )
    assert response.status_code == 200
    assert response == 'Data changed successfully,please list again to see it!'

def test_deletefood():
    response = client.delete(
    food_id = "4"
    )
    assert response.status_code == 200
    assert response == 'Data removed successfully,please list again to see it!'