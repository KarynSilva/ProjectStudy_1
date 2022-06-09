import datetime
from mocks.mock_operations import Initial_Check, Cast_Many_to_Object
from mocks.mock_operations import Cast_One_to_Object


def test_Initial_Check():
    data_test = []
    assert (not data_test) is True

    data_test = Initial_Check(data_test)
    assert (not data_test) is False
    assert (len(data_test)) == 6


def test_Cast_Many_to_Object():

    date_now = str(datetime.datetime.now())
    data_test = []
    data_test = [
                        {"_id": '0',
                         "name": "Panna Cotta",
                         "origination":
                         "Piemonte - Italy",
                         "created": "20th century",
                         "date": date_now},
                        {"_id": '1',
                         "name": "Croissant",
                         "origination":
                         "Viena - Austria",
                         "created": "1683",
                         "date": date_now},
                        {"_id": '2',
                         "name": "Capuccino",
                         "origination": "Brasil",
                         "created": "16th or 17th century",
                         "date": date_now},
                        {"_id": '3',
                         "name": "Gianduia",
                         "origination": "Piemonte - Italy",
                         "created": "1806 - 19th century",
                         "date": date_now},
                        {"_id": '4',
                         "name": "Crème brûlée",
                         "origination": "France",
                         "created": "17th century",
                         "date": date_now},
                        {"_id": '5',
                         "name": "Macarons",
                         "origination": "Veneto - Italy",
                         "created": "16th century",
                         "date": date_now}
                       ]

    data_test_obj = []
    data_test_obj = Cast_Many_to_Object(data_test)

    assert (not data_test_obj) is False
    assert (len(data_test_obj)) == 6
    assert data_test_obj[0].name == "Panna Cotta"
    assert data_test_obj[0].origination == "Piemonte - Italy"
    assert data_test_obj[0].created == "20th century"


def test_Cast_One_to_Object():

    data_test = None
    date_now = str(datetime.datetime.now())
    food_test = {"_id": '3',
                 "name": "Gianduia",
                 "origination": "Piemonte - Italy",
                 "created": "1806 - 19th century",
                 "date": date_now}
    data_test = Cast_One_to_Object(food_test)
    assert (data_test is None) is False
    assert data_test.name == "Gianduia"
    assert data_test.origination == "Piemonte - Italy"
    assert data_test.created == "1806 - 19th century"
