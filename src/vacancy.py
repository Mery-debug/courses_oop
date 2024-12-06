from main import user_info
from src.API import HH

example = user_info()
hh_example_1 = HH(example).expectation(example, HH(example).load_vacancies(example))


class ProcessingVacancies:
    """Класс обработки вакансий из полученного в АПИ результата, сравнение по зп, топ n и ключевые слова"""
    __slots__ = ["_total", "_top_n", "_keywords", "_pay"]

    def __init__(self, top_n, keywords, pay):
        self._total: list = hh_example_1
        self._top_n: str = top_n
        self._keywords: list = keywords
        self._pay: int = int(pay.split("-"))

    def __gt__(self, other):
        """Магический метод сравнения в большую сторону по зп"""
        tota = []
        for total in self._total:
            total["pay"] = int(other.pay)
            var = self._pay > other.pay
            if var == self._pay:
                self._total = tota.append(total)
                return self._total
            else:
                return f'Вакансия не подходит по диапазону зп'

    def sort_for_top_n_vacancies(self):
        """Метод для сортировки по убыванию списка вакансий"""
        total = sorted(self._total, reverse=True)
        return total[:self._top_n]








