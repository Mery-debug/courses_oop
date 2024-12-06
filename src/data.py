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
        total_vac = []
        for vacanc in vacancy:
            with open(file_name, "a+", encoding='utf-8') as json_file:
                json_obj = json.dumps(vacanc)
                if json_obj not in json_file:
                    total_vac.append(json_obj)
                    json_file.write(json_obj)
                    json_file.close()
                else:
                    continue
        return f'Запись прошла успешно, новые вакансии: {total_vac} добавлены в файл'

    def read_file(self, file_name):
        """Метод для чтения файла с json"""
        with open(file_name, "r+", encoding='utf-8') as file:
            # json_file = file.loads(file_name)



