import allure
import requests
import helpers


class TestLoginCourier:
    @allure.title('Проверка успешной авторизации курьера')
    @allure.description("Отправляем POST запрос для авторизации курьера и проверяем ответ")
    @allure.step('Авторизовуемся и проверяем успешный ответ')
    def test_success_login_courier(self):
        login_pass = helpers.register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=payload)

        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка ошибки при авторизации без обязательных данных')
    @allure.description("Отправляем POST запрос для авторизации курьера без логина в теле и проверяем ответ")
    @allure.step('Авторизовуемся без логина и проверяем ошибку в ответе')
    def test_login_courier_without_required_data(self):
        payload = {
            "password": "password"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=payload)

        assert response.status_code == 400 and "Недостаточно данных для входа" in response.text

    @allure.title('Проверка ошибки при авторизации c невалидным паролем')
    @allure.description("Отправляем POST запрос для авторизации курьера с невалидным паролем в теле и проверяем ответ")
    @allure.step('Авторизовуемся с невалидным паролем и проверяем ошибку в ответе')
    def test_login_courier_without_required_data(self):
        login_pass = helpers.register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]+"12345qwert"
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                 data=payload)

        assert response.status_code == 404 and "Учетная запись не найдена" in response.text

