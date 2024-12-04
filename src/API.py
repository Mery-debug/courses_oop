from abc import ABC, abstractmethod

import requests


class Parser(ABC):

    def __init__(self, file_worker):
        self.file_worker: list = file_worker

    @staticmethod
    def expectation(self, vacancies):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, file_worker):
        """ Метод конструктор для класса работы с АПИ """
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)
        self.top_worker: list = file_worker

    def load_vacancies(self, keywords):
        """ Метод для вызова АПИ, с валидацией по ответу от сервера (статус 200) """
        vacancies = []
        for keyword in keywords:
            self.params['text'] = keyword
            while self.params.get('page') != 20:
                response = requests.get(self.url, headers=self.headers, params=self.params)
                if response.status_code == 200:
                    vacancies = response.json()['items']
                    self.vacancies.extend(vacancies)
                    self.params['page'] += 1
                else:
                    return f"Возможная причина {response.reason}"
            return vacancies

    def expectation(self, file_worker):
        """ Метод формирование в список, а так же проверка на пустую или нулевую зп """
        vacancies = self.load_vacancies(file_worker[2])
        total = []
        top_n = file_worker[1]
        for vac in vacancies:
            if vac.get('salary') == 0 or not vac.get('salary'):
                continue
            else:
                vacancy_total = {
                    "name": vac.get('name'),
                    "description": vac.get('snippet').get('requirement'),
                    "url": vac.get('url'),
                    "pay": vac.get('salary')
                                }
            if len(total) == top_n:
                total.append(vacancy_total)
        return total

    # def total(self):





