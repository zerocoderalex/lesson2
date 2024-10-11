import requests
import pprint

# Создаем словарь с данными для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправляем POST-запрос
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

# Выводим статус-код ответа
print(response.status_code)

# Получаем и распечатываем содержимое ответа в формате JSON
response_json = response.json()
pprint.pprint(response_json)
