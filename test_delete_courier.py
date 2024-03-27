import allure
import requests
import helpers


class TestDeleteCourier:
    @allure.title('Проверка успешного удаления курьера')
    @allure.description("Отправляем DELETE запрос для удаления курьера и проверяем ответ")
    @allure.step('Удаляем курьера  и получаем успешный ответ')
    def test_success_delete_courier(self):
        login_pass = helpers.register_new_courier_and_return_login_password()
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

