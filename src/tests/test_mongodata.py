from mocks.mock_mongodata import MockFoodRepository as mrep
from collections import namedtuple


def test_list():

    m_data = mrep()
    data_test = []
    data_test = m_data.list()
    flag = (not data_test)
    assert flag is False
    assert len(data_test) == 6


def test_list_by_id():

    m_data = mrep()
    data_test = None
    data_test = m_data.list_by_id("1")
    assert data_test["name"] == "Croissant"
    assert data_test["origination"] == "Viena - Austria"
    assert data_test["created"] == "1683"


def test_create():

    m_data = mrep()
    food = {"_id": "None",
            "name": "Pizza",
            "origination": "Campania - Italy",
            "created": "18th century",
            "date": "None"
            }
    food_insert = namedtuple("Food", food.keys(), rename=True)(*food.values())
    data_test2 = None

    m_data.create(food_insert)
    data_test2 = m_data.list()

    assert len(data_test2) == 7
    assert data_test2[6]["name"] == "Pizza"


def test_edit():

    m_data = mrep()
    data_test2 = None
    food = {"_id": "2",
            "name": "Capuccino",
            "origination": "Italy",
            "created": "16th or 17th century",
            "date": "None"
            }
    food_edit = namedtuple("Food", food.keys(), rename=True)(*food.values())
    data_test2 = m_data.list()
    assert len(data_test2) == 6
    assert data_test2[2]["origination"] == "Brasil"

    m_data.edit(food_edit)
    data_test2 = m_data.list()
    assert len(data_test2) == 6
    assert data_test2[2]["origination"] == "Italy"


def test_delete():

    m_data = mrep()
    data_test2 = None
    m_data.delete("4")

    data_test2 = m_data.list()
    status = False
    assert len(data_test2) == 5
    for i in range(4):
        if(data_test2[i]["_id"] == "4"):
            status = True
    assert status is False
