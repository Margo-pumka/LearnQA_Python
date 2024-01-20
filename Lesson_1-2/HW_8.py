import requests
import time
response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response1.text)
token = {"token": response1.json()["token"]}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print(response2.text)
time.sleep(response1.json()["seconds"])
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print(response3.text)