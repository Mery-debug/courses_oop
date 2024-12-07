# from main import user_info
# from src.API import HH

# example = user_info()
# hh_example_1 = HH(example).expectation(example, HH(example).load_vacancies(example))


class ProcessingVacancies:
    """Класс обработки вакансий из полученного в АПИ результата, сравнение по зп, топ n и ключевые слова"""
    __slots__ = ["_total", "_top_n", "_keywords", "_pay"]

    def __init__(self, total: list[dict], top_n: int, keywords: list, pay: str):
        self._total: list = total
        self._top_n: int = top_n
        self._keywords: list = keywords
        self._pay: str = pay

    def __gt__(self, other: int) -> list[dict]:
        """Магический метод сравнения в большую сторону по зп"""
        tota = []
        for total in self._total:
            self._pay = total["pay"]
            if other < self._pay:
                tota.append(total)
        return tota

    def sort_for_top_n_vacancies(self, tota):
        """Метод для сортировки по убыванию списка вакансий"""
        lst = [tot.get('pay') for tot in tota]
        pass
        # return total[:int(self._top_n)]








