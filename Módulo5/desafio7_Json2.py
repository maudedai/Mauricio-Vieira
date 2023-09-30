import json
desafio_json = """{
    "name": "john Smith",
    "age": 30,
    "city": "new York",
    "isStudent": true,
    "gpa": 3.5
}"""
with open('desafio3.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(desafio_json, arquivo_json)