import pytest
import requests
import json
import allure
import urls

class TestCourier:

    @allure.step('Тестируем регистрацию курьера')
    def test_register_courier(self, random_user_data):
        self.user_data = random_user_data
        response = requests.post(urls.courier, data=self.user_data)

        assert response.status_code == 201  and response.text == '{"ok":true}'

    @allure.title('Проверка: нельзя создать двух одинаковых курьеров')
    def test_not_create_two_identical_couriers(self, random_registered_user_data):
        self.user_data = random_registered_user_data
        response = requests.post(urls.courier, data=self.user_data)

        assert response.status_code == 409

    @allure.title('Без передачи всех обязательных полей создание курьера невозможно')
    @pytest.mark.parametrize('key_ex', ["login", "password"])
    def test_registration_negative(self, key_ex, random_user_data):
        self.user_data_new = random_user_data
        self.user_data_new.pop(key_ex)
        response = requests.post(urls.courier, data=self.user_data_new)
        assert response.status_code == 400

    @allure.title('Если одного из полей нет, запрос возвращает ошибку')
    def test_register_courier_without_field(self, random_user_data_negative):
        self.user_data = random_user_data_negative
        response = requests.post(urls.courier, data=self.user_data)
        assert response.status_code == 400

    @allure.title('Если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_not_create_couriers_with_repeat_login(self, random_user_data_repeat_login):
        response1 = requests.post(urls.courier, data=random_user_data_repeat_login[0])
        response2 = requests.post(urls.courier, data=random_user_data_repeat_login[1])

        assert response2.status_code == 409
