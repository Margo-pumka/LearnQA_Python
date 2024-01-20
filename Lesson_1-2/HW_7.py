import requests
response = requests.get("https://playground.learnqa.ru/api/compare_query_type")
print(response.text)
response = requests.post("https://playground.learnqa.ru/api/compare_query_type")
print(response.text)
response = requests.put("https://playground.learnqa.ru/api/compare_query_type")
print(response.text)
response = requests.delete("https://playground.learnqa.ru/api/compare_query_type")
print(response.text)

response = requests.head("https://playground.learnqa.ru/api/compare_query_type")
print(response.text)

response = requests.get("https://playground.learnqa.ru/api/compare_query_type", params={"method": "GET"})
print(response.text)
response = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": "POST"})
print(response.text)
response = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method": "PUT"})
print(response.text)
response = requests.delete("https://playground.learnqa.ru/api/compare_query_type", data={"method": "DELETE"})
print(response.text)

methods = ["GET", "POST","PUT", "DELETE"]
for i in methods:
        response = requests.get("https://playground.learnqa.ru/api/compare_query_type", params={"method": i})
        print(response.text)
        response = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": i})
        print(response.text)
        response = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method": i})
        print(response.text)
        response = requests.delete("https://playground.learnqa.ru/api/compare_query_type", data={"method": i})
        print(response.text)
# для метода delete при подставновке "method": "GET"






