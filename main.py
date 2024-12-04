from src.API import HH


def user_info() -> list:
    """ Функция для взаимодействия с пользователем """
    name = input("Введите поисковой запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    keywords = input("Введите ключевые слова для фильтрации вакансий: ").lower()
    pay = input("Введите диапазон зарплат: ")
    lst = [name, top_n, keywords, pay]
    return lst


if __name__ == '__main__':
    hh_example = HH(user_info()).load_vacancies(user_info())
    print(hh_example)
