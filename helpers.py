from datetime import date
import allure
import requests
import random
import string


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length, lang):
    if lang == 'RU':
        letters = "аБгрвЗСМолпЫ"
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string
    if lang == 'US':
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


def get_random_phone():
    phone = f"+79{random.randint(100000000, 999999999)}"
    return phone


def get_date_today():
    date_now = f"{date.today()}"
    return date_now


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@allure.step('Получаем логин и пароль зарегистрированного курьера')
def register_new_courier_and_return_login_password():
    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10, 'US')
    password = generate_random_string(10, 'US')
    first_name = generate_random_string(10, 'US')

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass


@allure.step('Получаем данные для заполнения полей заказа')
def get_random_data_order(color):
    first_name = generate_random_string(10, 'RU')
    last_name = generate_random_string(10, 'RU')
    address = generate_random_string(10, 'RU')
    metro_station = random.randint(1, 237)
    phone = get_random_phone()
    rent_time = random.randint(1, 10)
    delivery_date = get_date_today()
    comment = generate_random_string(10, 'RU')
    test_color = color

    payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": test_color
    }
    return payload
