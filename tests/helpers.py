from data import generate_random_string, STANDARD_LOGIN_LENGTH, STANDARD_FIRSTNAME_LENGTH, STANDARD_PASSWORD_LENGTH
import requests
import urls
import json
import allure


class CourierHelper:

    couriers = []

    @staticmethod
    @allure.step('Генерируем случайные данные пользователя')
    def create_random_user_data():
        user_data = {"login": generate_random_string(STANDARD_LOGIN_LENGTH),
                     "password": generate_random_string(STANDARD_PASSWORD_LENGTH),
                     "firstname": generate_random_string(STANDARD_FIRSTNAME_LENGTH)}

        return user_data

    @staticmethod
    @allure.step('Регистрируем курьера')
    def register_courier():
        user_data = CourierHelper.create_random_user_data()

        response = requests.post(urls.courier, user_data)

        if response.status_code != 201:
           raise Exception("Ошибка регистрации")

        user_data.pop("firstname")
        CourierHelper.couriers.append(user_data)

        return user_data

    @staticmethod
    @allure.step('Удаляем курьера')
    def delete_courier(id):
        response = requests.delete(f'{urls.courier}:{id}')

        if response.status_code == 200:
            return True
        else:
            return False

    @staticmethod
    @allure.step('Удаляем всех курьеров')
    def delete_all_couriers():

        for courier in CourierHelper.couriers:
            payload = courier.copy()
            response = requests.post(urls.login_courier, payload)
            if response.status_code == 200:
                id = int(json.loads(response.text)["id"])
                CourierHelper.delete_courier(id)


class OrderHelper:

    orders = []

    @staticmethod
    @allure.step('Запоминаем заказ для последующего удаления')
    def add_order(id):
        OrderHelper.orders.append(id)


    @staticmethod
    @allure.step('Запоминаем заказ для последующего удаления')
    def add_order_from_json_str(json_str):
        if 'track' in json.loads(json_str).keys():
            OrderHelper.orders.append(json.loads(json_str)['track'])
        else:
            return False


    @staticmethod
    @allure.step('Удаляем заказ')
    def delete_order_by_id(id):
        payload = {'track': id}
        response = requests.put(urls.cancel_order, payload)
        if response.status_code == 200:
            return True
        else:
            return False

    @staticmethod
    @allure.step('Удаляем все заказы')
    def delete_all_orders():
        for id in OrderHelper.orders:
            OrderHelper.delete_order_by_id(id)
