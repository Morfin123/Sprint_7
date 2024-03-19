import json
import allure
import requests
import helpers


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа')
    @allure.description("Отправляем POST запрос для создания заказа и проверяем ответ")
    @allure.step('Создаем заказ и проверяем успешный ответ')
    @pytest.mark.parametrize('color', [[''], ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_success_create_order(self, color):
        payload = helpers.get_random_data_order(color)

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders',
                                 data=json.dumps(payload))
        assert response.status_code == 201 and 'track' in response.text

