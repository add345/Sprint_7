import pytest
import requests
import json
import urls
import helpers
import allure

class TestCreatingOrder:

    @allure.title('Создание заказа, можно указать один из цветов — BLACK или GREY')
    @pytest.mark.parametrize('color', ['', [], ["GREY"], ["BLACK"], ["GREY", "BLACK"]])
    def test_creating_an_order_black_grey(self, color, order_data):
        payload = order_data
        if color != '':
            payload['color'] = color
        response = requests.post(urls.creating_an_order, data=payload)
        print(response.text)
        if response.status_code == 201:
            id = json.loads(response.text)['track']
            helpers.OrderHelper.add_order(id)

        assert response.status_code == 201



    @allure.title('Создание заказа, тело ответа содержит track')
    def test_response_body_contains_track(self, order_data):
        payload = order_data
        response = requests.post(urls.creating_an_order, data=payload)
        if response.status_code == 201:
            id = json.loads(response.text)['track']
            helpers.OrderHelper.add_order(id)
            print(json.loads(response.text)['track'])
            assert 'track' in json.loads(response.text).keys()
