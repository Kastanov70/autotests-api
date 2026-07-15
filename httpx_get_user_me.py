import httpx

# Базовый URL
base_url = "http://localhost:8000/api"
# Создаем клиента к нашему API
client = httpx.Client(base_url=base_url)
# Данные для аутентификации
login_payload = {
    "email": "user@example.com",
    "password": "string"
}

# Выполняем запрос на аутентификацию
login_response = client.post("/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
# Сохраняем токен
access_token = login_response_data.get("token", {}).get("accessToken", {})

# Выполняем запрос данных пользователя.
# Добавляем в заголовок токен
headers = {"Authorization": f"Bearer {access_token}"}
get_user_response = client.get("/v1/users/me", headers=headers)

# Выводим в консоль статус код и данные о пользователе
print(f"Статус код ответа: {get_user_response.status_code}")
print(f"JSON-ответ от сервера с данными о пользователе: {get_user_response.json()}")
