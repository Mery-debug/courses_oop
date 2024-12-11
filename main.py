from src.API import HH
from src.data import ReadJson
from src.vacancy import ProcessingVacancies


def user_info() -> list:
    """ Функция для взаимодействия с пользователем """
    keywords = input("Введите поисковой запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    name = input("Введите ключевые слова для фильтрации вакансий: ").lower().split(',')
    pay = input("Введите диапазон зарплат: ")
    lst_dict = [name, top_n, keywords, pay]
    return lst_dict


def point(lst: list) -> str:
    """
    Функция 'точка входа'
    """
    hh = HH(lst)
    hh_1 = hh.load_vacancies(lst[0])
    hh_2 = hh.expectation(lst, hh_1)
    vac = ProcessingVacancies(hh_2, lst[1], lst[2], lst[3])
    vac_1 = vac.__gt__(int(lst[3]))
    vac_2 = vac.sort_for_top_n_vacancies(vac_1)
    read = ReadJson("test.json", vac_2)
    read_1 = read.dict_to_json(vac_2, "test.json")
    return read_1


if __name__ == '__main__':
    lst = user_info()
    result = point(lst)
    print(result)
