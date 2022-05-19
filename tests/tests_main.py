from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_initial_data():
    response = client.get("/foods/")
    assert response.status_code == 200
    data = response.json()
    
    assert data[0]["name"] == "Panna Cotta"
    assert data[1]["name"] == "Croissant"
    assert data[2]["name"] == "Capuccino"
    assert data[3]["name"] == "Gianduia"
    assert data[4]["name"] == "Crème brûlée"
    assert data[5]["name"] == "Macarons"
    assert data[0]["origination"] == "Piemonte - Italy"
    assert data[1]["origination"] == "Viena - Austria"
    assert data[2]["origination"] == "Brasil"
    assert data[3]["origination"] == "Piemonte - Italy"
    assert data[4]["origination"] == "France"
    assert data[5]["origination"] == "Veneto - Italy"
    assert data[0]["created"] == "20th century"
    assert data[1]["created"] == "1683"
    assert data[2]["created"] == "16th or 17th century"
    assert data[3]["created"] == "1806 - 19th century"
    assert data[4]["created"] == "17th century"
    assert data[5]["created"] == "16th century"
    
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
    

def test_create_food():
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

def test_edit_food():
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

def test_delete_food():
    response = client.delete(
    food_id = "4"
    )
    assert response.status_code == 200
    assert response == 'Data removed successfully,please list again to see it!'