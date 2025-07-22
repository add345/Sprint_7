import pytest
import requests
import json
import urls
import allure


class TestLoginCourier:

    @allure.title('Курьер может авторизоваться')
    def test_courier_can_log_in(self, registered_user_data):
        self.user_data = registered_user_data
        response = requests.post(urls.login_courier, data=self.user_data)

        assert response.status_code == 200

    @allure.step('Логин курьера, для авторизации нужно передать все обязательные поля;')
    @pytest.mark.parametrize('key_ex', ["login", "password"])
    def test_courier_can_log_in_required_fields(self, key_ex, registered_user_data):
        self.user_data = registered_user_data
        self.user_data[key_ex] = ''

        response = requests.post(urls.login_courier, data=self.user_data)
        assert response.status_code == 400


    @allure.title('Логин курьера, система вернёт ошибку, если неправильно указать логин или пароль')
    @pytest.mark.parametrize('key_ex', ["login", "password"])
    def test_courier_log_in_negative_return_an_error(self, key_ex, registered_user_data):
        payload = registered_user_data
        payload[key_ex] = f'{registered_user_data[key_ex]}1'
        response = requests.post(urls.login_courier, data=payload)
        assert response.status_code == 404


    @allure.title('Логин курьера, если какого-то поля нет, запрос возвращает ошибку')
    @pytest.mark.parametrize('key_ex', ["login", "password"])
    def test_courier_log_in_without_field(self, key_ex, registered_user_data):
        self.user_data = registered_user_data
        self.user_data[key_ex] = ''

        response = requests.post(urls.login_courier, data=self.user_data)
        assert response.status_code == 400

    @allure.title('Логин курьера, если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    @pytest.mark.parametrize('key_ex', ["login", "password"])
    def test_courier_log_in_non_existent_login_password_return_an_error(self, key_ex, registered_user_data):
        payload = registered_user_data
        payload[key_ex] = f'{registered_user_data[key_ex]}1'
        response = requests.post(urls.login_courier, data=payload)
        assert response.status_code == 404



    @allure.title('Логин курьера, успешный запрос возвращает id.')
    def test_courier_can_log_in_returns_id(self, registered_user_data):
        self.user_data = registered_user_data
        response = requests.post(urls.login_courier, data=self.user_data)

        if response.status_code == 200:
            print(json.loads(response.text)['id'])
            assert 'id' in json.loads(response.text).keys()


