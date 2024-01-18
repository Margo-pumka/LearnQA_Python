import json
sting_as_json_format = '{"answer":"Hello, User"}'
obj = json.loads(sting_as_json_format)
print(obj['answer'])
print(json.loads('{"answer":"Hello, User"}')['answer'])

key = "answer"
if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")