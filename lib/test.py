import requests

url = 'http://localhost:5000/post'  # Укажите URL вашего Flask-приложения

data = {
    'key1': 'value1',
    'key2': 'value2'
}

response = requests.post(url, json=data)

print(response.status_code)  # Код статуса ответа
print(response.json())  # Декодированный JSON-ответ
