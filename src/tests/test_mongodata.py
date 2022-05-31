from mocks.mock_mongodata import MockFoodRepository as mrep

def test_list():

    data_test = []
    data_test = mrep.list()
    flag = (not data_test)
    assert flag == False
    assert len(data_test) == 6

def test_list_by_id():

    data_test = None
    data_test = mrep.list_by_id("1")
    assert data_test["name"] == "Croissant"
    assert data_test["origination"] == "Viena - Austria"
    assert data_test["created"] == "1683"

def test_create():

    food_insert = {"_id":"None","name": "Pizza",
                   "origination": "Campania - Italy",
                   "created": "18th century",
                   "date": "None"
                  }
    data_test = None
    data_test2 = None

    data_test = mrep.create(food_insert)
    data_test2 = mrep.list()

    assert len(data_test2) == 7
    assert data_test2[6]["name"] == "Pizza"

def test_edit():

    data_test= None
    data_test2 = None
    food_edit =   {"_id":"2","name": "Capuccino",
                   "origination": "Italy",
                   "created": "16th or 17th century",
                   "date": "None"
                  }
    data_test2 = mrep.list()
    assert len(data_test2) == 6
    assert data_test2[2]["origination"] == "Brasil"

    data_test = mrep.edit(food_edit)
    
    data_test2 = mrep.list()
    assert len(data_test2) == 6
    assert data_test2[2]["origination"] == "Italy"

def test_delete():

    data_test = None
    data_test2 = None
    data_test = mrep.delete("4")

    data_test2 = mrep.list()
    status = False
    assert len(data_test2) == 5
    
    for i in range(4):
        if(data_test2[i]["_id"]=="4"):
            status = True

    assert status == False