import requests
response = requests.post("https://playground.learnqa.ru/api/get_500")
print(response.status_code)
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/something")
print(response.status_code)
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print(response.status_code)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
print(response.status_code)
first_response = response.history[0]
print(first_response.url)
print(response.url)

