
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
            if other < int(self._pay):
                tota.append(total)
        return tota

    def sort_for_top_n_vacancies(self, tota: list[dict]) -> list[dict]:
        """Метод для сортировки по убыванию списка вакансий"""
        sorted_tota = sorted(tota, key=lambda x: x.get("pay", 0), reverse=True)
        return sorted_tota[: int(self._top_n)]

    def __str__(self):
        return f"ProcessingVacancies ({self._total}, {self._top_n}, {self._keywords}, {self._pay})"

    @staticmethod
    def sort_by_keywords(sorted_tota: list[dict], keywords) -> list:
        finish = []
        for tota in sorted_tota:
            for keyw in keywords:
                if keyw in tota.get('name'):
                    finish.append(tota)
        return finish


