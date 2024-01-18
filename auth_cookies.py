import requests
payload = {"login": "secret_login", "password": "secret_pass"}
response = requests.get("https://playground.learnqa.ru/api/get_auth_cookie", params=payload)
print(response.text)
print(response.status_code)
print(dict(response.cookies))
print(response.headers)