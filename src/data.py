import json


# Добавить в класс с json
def in_json(vacancy: list[dict], file_name):
    with open(file_name, "r+", encoding='utf-8') as json_file:
        data = json.load(json_file)
