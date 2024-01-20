from json import JSONDecodeError
import requests
response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
try:
    parsed_response_text = response.json()
    print(parsed_response_text['answer'])
    print(response.json()['answer'])
except JSONDecodeError:
    print('Response is not a JSON format')



response = requests.get("https://playground.learnqa.ru/api/get_text")
try:
    parsed_response_text = response.json()
    print(parsed_response_text['answer'])
    print(response.json()['answer'])
except JSONDecodeError:
    print('Response is not a JSON format')