import requests
payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", params=payload)
cookies_value = response1.cookies.get('auth_cookie')

cookies = {'auth_cookie': cookies_value}

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print(response2.text)