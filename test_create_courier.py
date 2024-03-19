import allure
import requests
import helpers


class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера')
    @allure.description("Отправляем POST запрос на создание нового курье и проверяем ответ")
    @allure.step('Регистрируем нового курьера и проверяем успиешный ответ')
    def test_success_create_courier(self):

        # генерируем логин, пароль и имя курьера
        login = helpers.generate_random_string(10, 'US')
        password = helpers.generate_random_string(10, 'US')
        first_name = helpers.generate_random_string(10, 'US')

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', payload)

        # проверяем ответ
        assert response.status_code == 201 and response.text == '{"ok":true}'
        print(response.text)

