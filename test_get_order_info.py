import allure
import requests


class TestGetOrderInfo:
    @allure.title('Проверка получения списка заказов')
    @allure.description("Отправляем GET запрос для получения списка заказов и проверяем ответ")
    @allure.step('Получаем список заказов и проверяем успешный ответ')
    def test_get_order_info(self):
        response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId=')
        assert response.status_code == 200 and 'id' in response.text
