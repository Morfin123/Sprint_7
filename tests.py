import allure
import pytest
import requests
import data
import random
import string
import json


class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера')
    @allure.description("Отправляем POST запрос на создание нового курье и проверяем ответ")
    def test_success_create_courier(self):

        # генерируем логин, пароль и имя курьера
        login = data.generate_random_string(10)
        password = data.generate_random_string(10)
        first_name = data.generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # проверяем ответ
        assert response.status_code == 201 and response.text == '{"ok":true}'


class TestLoginCourier:
    @allure.title('Проверка успешной авторизации курьера')
    @allure.description("Отправляем POST запрос для авторизации курьера и проверяем ответ")
    def test_success_login_courier(self):
        login_pass = data.register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=payload)

        assert response.status_code == 200 and 'id' in response.text


class TestDeleteCourier:
    @allure.title('Проверка успешного удаления курьера')
    @allure.description("Отправляем DELETE запрос для удаления курьера и проверяем ответ")
    def test_success_delete_courier(self):
        login_pass = data.register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=payload)
        data_answer = response.json()

        payload = {
            "id": str(data_answer["id"])
        }
        response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{data_answer["id"]}',
                                   data=payload)
        assert response.status_code == 200 and response.text == '{"ok":true}'


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа')
    @allure.description("Отправляем POST запрос для создания заказа и проверяем ответ")
    @pytest.mark.parametrize('color', [[''], ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_success_create_order(self, color):
        payload = data.get_random_data_order(color)

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders',
                                 data=json.dumps(payload))
        assert response.status_code == 201 and 'track' in response.text


class TestGetOrderInfo:
    @allure.title('Проверка получения списка заказов')
    @allure.description("Отправляем GET запрос для получения списка заказов и проверяем ответ")
    def test_get_order_info(self):
        response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId=')
        assert response.status_code == 200 and 'id' in response.text
