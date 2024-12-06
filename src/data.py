import json
from abc import ABC, abstractmethod

from src.vacancy import ProcessingVacancies


class BaseJsonVacancy(ABC):


    @abstractmethod
    def dict_to_json(self, vacancy, file_name):
        pass


class ReadJson(BaseJsonVacancy):
    """Класс для преобразования списка словарей с вакансиями в json-файл"""

    def __init__(self, file_name: str, vacancy: list[dict]):
        """Конструктор класса"""
        self.file_name: str = file_name
        self.vacancy: list[dict] = vacancy

    def dict_to_json(self, vacancy: list[dict], file_name: str):
        """Метод для записи данных в файл json"""
        with open(file_name, "a+", encoding='utf-8') as json_file:
            json_obj = json.dumps(vacancy)
            if json_obj not in json_file:
                json_file.write(json_obj)
                json_file.close()
                return 'Запись прошла успешно, новые вакансии добавлены'
            else:
                json_file.close()
                return 'Запись не произведена, такие вакансии уже есть в файле'

    def


