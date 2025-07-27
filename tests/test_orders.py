import pytest
import requests
import json
import urls
import allure


class TestListOrders:

    @allure.title('Проверь, что в тело ответа возвращается список заказов')
    def test_getting_list_of_orders (self):
        with allure.step('Отправка запроса на получение списка заказов'):
            response = requests.get(urls.list_of_order)
        assert 'orders' in json.loads(response.text).keys()