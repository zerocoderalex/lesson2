import requests
import pprint

# Параметры для запроса
params = {'userId': 1}

# Отправляем GET-запрос
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

# Проверяем статус-код ответа
if response.status_code == 200:
    # Получаем и распечатываем содержимое ответа в формате JSON
    response_json = response.json()
    pprint.pprint(response_json)
else:
    print("Ошибка при выполнении запроса:", response.status_code)
