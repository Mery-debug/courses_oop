import json
from abc import ABC, abstractmethod


class BaseJsonVacancy(ABC):

    @abstractmethod
    def dict_form(self):
        pass

    @abstractmethod
    def dict_to_json(self):
        pass


class ReadJson():
    def in_json(vacancy: list[dict], file_name):
        with open(file_name, "r+", encoding='utf-8') as json_file:
            data = json.load(json_file)
