from collections import namedtuple
from api.app.main import read_food_list, read_food, create_food, update_food
from api.app.main import delete_food
from mocks.mock_mongodata import MockFoodRepository as mdata


def test_read_food_list():
    mrep = mdata()
    data_test = []
    data_test = read_food_list(0, 10, mrep)
    flag = (not data_test)
    assert not flag


def test_read_food():

    mrep = mdata()
    data_test = None
    data_test = read_food(1, mrep)
    assert (data_test is None) is False


def test_create_food():

    mrep = mdata()
    food = {"_id": "None",
            "name": "Pizza",
            "origination": "Campania - Italy",
            "created": "18th century",
            "date": "None"
            }
    food_insert = namedtuple("Food", food.keys(), rename=True)(*food.values())
    data_test = None
    data_test = create_food(food_insert, mrep)
    assert data_test == 'Data entered successfully,please list again to see it!' # noqa


def test_update_food():

    mrep = mdata()
    data_test = None
    food = {"_id": "2",
            "name": "Capuccino",
            "origination": "Italy",
            "created": "16th or 17th century",
            "date": "None"
            }
    food_edit = namedtuple("Food", food.keys(), rename=True)(*food.values())
    data_test = update_food(food_edit, mrep)
    assert data_test == 'Data changed successfully,please list again to see it!' # noqa


def test_delete_food():

    mrep = mdata()
    data_test = None
    data_test = delete_food("4", mrep)
    assert data_test == 'Data removed successfully,please list again to see it!' # noqa
