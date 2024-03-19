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

