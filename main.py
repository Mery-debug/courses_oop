from src.API import HH


def user_info() -> list:
    """ Функция для взаимодействия с пользователем """
    keywords = input("Введите поисковой запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    name = input("Введите ключевые слова для фильтрации вакансий: ").lower().split(',')
    pay = input("Введите диапазон зарплат: ")
    lst = [name, top_n, keywords, pay]
    return lst


if __name__ == '__main__':
    example = user_info()[0]
    # hh_example = HH(example).load_vacancies(example)
    hh_example_1 = HH(example).expectation(example, HH(example).load_vacancies(example))
    print(hh_example_1)
