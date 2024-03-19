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

    @allure.title('Проверка ошибки создания курьера существующего курьера')
    @allure.description("Отправляем POST запрос на создание курьера с существующим логином и проверяем ответ")
    @allure.step('Регистрируем курьера c существующим логином и проверяем ошибку в ответе')
    def test_success_create_courier(self):
        login_pass = helpers.register_new_courier_and_return_login_password()

        payload = {
            "login": login_pass[0],
            "password": helpers.generate_random_string(10, 'US')
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', payload)

        # проверяем ответ
        assert response.status_code == 409 and "Этот логин уже используется" in response.text

    @allure.title('Проверка ошибки создания курьера без необходимых данных')
    @allure.description("Отправляем POST запрос на создание курьера без пароля и проверяем ответ")
    @allure.step('Регистрируем курьера без пароля и проверяем ошибку в ответе')
    def test_success_create_courier(self):
        payload = {
            "login": helpers.generate_random_string(10, 'US'),
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', payload)

        # проверяем ответ
        assert response.status_code == 400 and "Недостаточно данных для создания учетной записи" in response.text
