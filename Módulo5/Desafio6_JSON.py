import json
with open('desafio1.json', encoding='utf-8') as data_json:
    data = json.load(data_json)
    print(data["user"][1]["email"])
    print(data["user"][0]["address"]["city"])
    print(data["user"][1]["orders"][0]["total"])