import pytest
import requests
from data import generate_random_string
from data import STANDARD_LOGIN_LENGTH, STANDARD_FIRSTNAME_LENGTH, STANDARD_PASSWORD_LENGTH
from helpers import CourierHelper, OrderHelper


@pytest.fixture
def random_user_data(request):
    return CourierHelper.create_random_user_data()

@pytest.fixture
def random_user_data_negative(request):
    user_data = {"login": generate_random_string(STANDARD_LOGIN_LENGTH),
    "firstname": generate_random_string(STANDARD_FIRSTNAME_LENGTH)}

    return user_data

@pytest.fixture
def random_user_data_repeat_login(request):
    user_data1 = {"login": generate_random_string(STANDARD_LOGIN_LENGTH),
    "password": generate_random_string(STANDARD_PASSWORD_LENGTH),
    "firstname": generate_random_string(STANDARD_FIRSTNAME_LENGTH)}
    user_data2 = {"login": user_data1['login'],
    "password": generate_random_string(STANDARD_PASSWORD_LENGTH),
    "firstname": generate_random_string(STANDARD_FIRSTNAME_LENGTH)}

    return [user_data1, user_data2]

@pytest.fixture
def random_user_data_negative_2(request):
    user_data = {"login": generate_random_string(STANDARD_LOGIN_LENGTH)}

    return user_data

@pytest.fixture
def order_data(request):
    result = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }
    return result


@pytest.fixture
def list_order(request):
    result = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }
    return result



@pytest.fixture
def registered_user_data(request):
    return CourierHelper.register_courier()

@pytest.fixture(scope="session", autouse=True)
def auto_delete_couriers():
    yield
    CourierHelper.delete_all_couriers()

@pytest.fixture(scope="session", autouse=True)
def auto_delete_orders():
    yield
    OrderHelper.delete_all_orders()

#@pytest.fixture
#def creating_order(request):
 #   user_data = {"login": generate_random_string(STANDARD_LOGIN_LENGTH),
 #   "password": generate_random_string(STANDARD_PASSWORD_LENGTH),
 #   "firstname": generate_random_string(STANDARD_FIRSTNAME_LENGTH)}

#    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', user_data)

#    user_data.pop("firstname")

#    if response.status_code != 201:
#        raise Exception("Ошибка регистрации")
#    print(response.text)
 #   return user_data