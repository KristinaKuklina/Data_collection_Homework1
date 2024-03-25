'''Напишите сценарий на языке Python, который предложит пользователю ввести интересующую
его категорию (например, кофейни, музеи, парки и т.д.).
Используйте API Foursquare для поиска заведений в указанной категории.
Получите название заведения, его адрес и рейтинг для каждого из них.
Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль'''

import requests
import json

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
query = input("Введите интересующую категорию: ")
params = {
    "limit": 5,
    "query": query,
    'fields': 'name,location,rating'
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq36ImGK8Q4eJ2cDhupsG+tFR8PKtfxvG9t5OZRvC+OKJ0="
}

# Отправка запроса API и получение ответа
response = requests.get(endpoint, params=params,headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    print("\n")
    data = json.loads(response.text)
    venues = data["results"]
    for venue in venues:
        print("Название:", venue["name"])
        print("Адрес:", venue["location"]['formatted_address'])
        print('Рейтинг',  venue["rating"] if 'rating' in venue else "Рейтинг не определялся")
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)