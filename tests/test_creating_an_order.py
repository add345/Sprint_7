import pytest
import requests
import json
import urls
import helpers
import allure
import data

class TestCreatingOrder:

    @allure.step('Создание заказа, можно указать один из цветов — BLACK или GREY')
    @pytest.mark.parametrize('color', [[], ["GREY"], ["BLACK"], ["GREY", "BLACK"]])
    def test_creating_an_order_black_grey(self, color):
        payload = data.order_data
        payload['color'] = color
        response = requests.post(urls.creating_an_order, data=payload)
        id = json.loads(response.text)['track']
        helpers.OrderHelper.add_order(id)

        assert response.status_code == 201 and 'track' in json.loads(response.text).keys()

    @allure.step('Создание заказа, без передачи поля color')
    def test_creating_an_order_no_color_field(self):
        payload = data.order_data
        response = requests.post(urls.creating_an_order, data=payload)
        id = json.loads(response.text)['track']
        helpers.OrderHelper.add_order(id)

        assert response.status_code == 201 and 'track' in json.loads(response.text).keys()

