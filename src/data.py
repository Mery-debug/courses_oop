import json
from abc import ABC, abstractmethod
from pathlib import Path


class BaseJsonVacancy(ABC):

    @abstractmethod
    def dict_to_json(self, vacancy, file_name):
        pass

    @abstractmethod
    def read_file(self, file_name):
        pass

    @abstractmethod
    def del_all(self, file_name):
        pass


class ReadJson(BaseJsonVacancy):
    """Класс для преобразования списка словарей с вакансиями в json-файл"""

    def __init__(self, file_name: str, vacancy: list[dict]):
        """Конструктор класса"""
        if file_name and len(file_name) > 3:
            self.file_name: str = file_name
        self.vacancy: list[dict] = vacancy

    def dict_to_json(self, vacancy: list[dict], file_name: str) -> str:
        """Метод для записи данных в файл json"""
        total_vac = []
        try:
            with open(file_name, "r", encoding='utf-8') as json_file:
                total_vac = json.load(json_file)
        except FileNotFoundError:
            total_vac = []
        for vacanc in vacancy:
            if vacanc not in total_vac:
                total_vac.append(vacanc)
        with open(file_name, "w", encoding='utf-8') as json_file:
            json.dump(total_vac, json_file, ensure_ascii=False, indent=4)

        return f'Запись прошла успешно, новые вакансии: {total_vac} добавлены в файл'

    def read_file(self, file_name: str) -> str:
        """Метод для чтения файла с json"""
        with open(file_name, "r+", encoding='utf-8') as file:
            json_file = file.read()
            return json_file

    def del_all(self, file_name: str) -> str:
        """Метод для удаления содержимого файла"""
        with open(file_name, "r+", encoding='utf-8') as f:
            f.truncate(0)
            return f'Файл {file_name}, полностью очищен'


