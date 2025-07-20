# from wsgiref.validate import check_errors

import pytest
import requests
import json


class TestCourier:

    def test_register_courier(self, random_user_data):
        self.user_data = random_user_data
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=self.user_data)

        assert response.status_code == 201

    # @allure.title('Проверка: нельзя создать двух одинаковых курьеров')
    def test_not_create_two_identical_couriers(self, random_user_data):
        self.user_data = random_user_data
        response1 = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=self.user_data)
        response2 = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=self.user_data)

        assert response2.status_code == 409

   # addresses = [
     #   'Тверская улица, дом 13',
     #   'улица Академика Колмогорова, дом 7',
     #   'Мышкинский проезд, дом 95',
     #   'Стандартная улица, дом 21',
     #   'Набережная реки Фонтанки, дом 154'
   # ]
    # @allure.title('Чтобы создать курьера, нужно передать в ручку все обязательные поля;')
    @pytest.mark.parametrize('key_ex', ["login", "password"])
    def test_registration_negative(self, key_ex, random_user_data):
        self.user_data_new = random_user_data
        self.user_data_new.pop(key_ex)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=self.user_data_new)
        assert response.status_code == 400

#Запрос возвращает правильный код ответа;

#import pytest

    def test_register_returns_the_correct_response_code(self, random_user_data):
        self.user_data = random_user_data
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=self.user_data)
        assert response.status_code == 201


 # Успешный запрос возвращает {"ok":true};

    def test_register_returns_the_correct_text(self, random_user_data):
        self.user_data = random_user_data
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=self.user_data)
        if response.status_code == 201:
            print(response.text)
            assert response.text == '{"ok":true}'

  # Если одного из полей нет, запрос возвращает ошибку;

    def test_register_courier_without_field(self, random_user_data_negative):
        self.user_data = random_user_data_negative
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=self.user_data)
        assert response.status_code == 400
            #assert json.loads(response.text)['message'] == 'Недостаточно данных для создания учетной записи'
          #  print({ "message": "Недостаточно данных для создания учетной записи"})

    # Если создать пользователя с логином, который уже есть, возвращается ошибка.
    def test_not_create_couriers_with_repeat_login(self, random_user_data_repeat_login):
        response1 = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=random_user_data_repeat_login[0])
        response2 = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=random_user_data_repeat_login[1])

        assert response2.status_code == 409

       # if response:
        #        print("Успешно получен ответ 201 после POST запроса!")
       # else:
          #      print("Не удалось получить ответ 201 после POST запроса.")
#@ptest.mark.parametrize("input_value, expected_result", [
#    (10, "больше 5"),
 #   (3, "меньше или равно 5"),
 #   (5, "меньше или равно 5"),
#])
#def test_if_else_in_parameterized(input_value, expected_result):
  #  if input_value > 5:
      #  result = "больше 5"
#else:
       # result = "меньше или равно 5"
    #assert result == expected_result, f"Ожидалось {expected_result}, получено {result}"

    # @pytest.mark.parametrize('login, password ', [{"data": " "}, {"data": " "}])
    # ("/login", {"name": "test_user", "email": "test@example.com"}, 201),
    # ("/products", {"name": "test_product", "price": 100}, 201)
   # 10022698


   # @pytest.fixture
   # def api_client(): return ApiClient(base_url=https

   # : // example.com / api)

   # @pytest.mark.parametrize(endpoint, status_code, [(/ users, 200), (/ posts, 200), (/ comments, 404), ])
   # def test_api_endpoints(api_client, endpoint, status_code): response = api_client.get(endpoint)

   # assert response.status_code == status_code


    # @pytest.mark.parametrize(a, b, expected, [(1, 2, 3), (3, 5, 8), (10, 10, 20)])
    # def test_addition(a, b, expected): assert addition(a, b) == expected
    #     pass
   # if response.status_code == 201:
           #     print("Успешно получен ответ 201 после POST запроса!")
        #else:
         #       print("Не удалось получить ответ 201 после POST запроса.")