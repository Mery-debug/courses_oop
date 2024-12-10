from abc import ABC, abstractmethod

import requests


class Parser(ABC):

    def __init__(self, file_worker: list):
        self.file_worker: list = file_worker

    @abstractmethod
    def load_vacancies(self, keywords: list):
        pass

    @abstractmethod
    def expectation(self, file_worker: list, vacancies: dict):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self, file_worker: list):
        """ Метод конструктор для класса работы с АПИ """
        self._url: str = 'https://api.hh.ru/vacancies'
        self._headers: dict = {'User-Agent': 'HH-User-Agent'}
        self._params: dict = {'text': '', 'page': 0, 'per_page': 100}
        self._vacancies: list = []
        super().__init__(file_worker)
        self.top_worker: list = file_worker

    def load_vacancies(self, keywords: list):
        """ Метод для вызова АПИ, с валидацией по ответу от сервера (статус 200) """
        vacancies = []
        for keyword in keywords:
            self._params['text'] = keyword
            while self._params.get('page') != 20:
                response = requests.get(self._url, headers=self._headers, params=self._params)
                if response.status_code == 200:
                    vacancies = response.json()['items']
                    self._vacancies.extend(vacancies)
                    self._params['page'] += 1
                else:
                    return f"Возможная причина {response.reason}"
        return vacancies

    def expectation(self, file_worker: list, vacancies: list[dict]):
        """ Метод формирование в список, а так же проверка на пустую или нулевую зп """
        total = []
        for vac in vacancies:
            if vac.get("salary"):
                vacancy_total = {
                    "name": vac.get('name'),
                    "description": vac.get('snippet').get('requirement'),
                    "url": vac.get('url'),
                    "pay": vac.get("salary").get("from") or vac.get("salary").get("to")
                }
                total.append(vacancy_total)
            else:
                continue
        return total

    def __str__(self):
        return f'HH ({self._url}, {self._headers}, {self._params}, {self._vacancies})'





