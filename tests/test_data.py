import json
import os

from src.data import ReadJson


def test_dict_to_json(result_1: str) -> None:
    """
    Тест для проверки метода, который заданный словарь преобразует в json-файл (запускается только из корня)
    """
    vacancies = [
        {"personal": "Jhon doe", "payment": "50000"},
        {"personal": "Jisus", "payment": "100000"}
    ]
    assert ReadJson("tests.json", vacancies).dict_to_json(vacancies, "tests.json") == result_1


def test_str_json(vacancy: list[dict], file_name: str, path: str) -> None:
    """
    Тест для проверки магического метода __str__
    """
    file_name = "test.json"
    path = os.path.abspath(file_name)
    j = ReadJson(file_name, vacancy)
    assert str(j) == f"Запись производиться в файл {file_name}, полный путь {path}"


def test_del_all() -> None:
    """
    Тест проверяющий работоспособность метода удаления всего из файла,
    но в файле что-то должно быть иначе тест не проходит
    """
    result = "Файл data/tests_1.json, полностью очищен"
    vacancy = [
        {"personal": "Jhon doe", "payment": "50000"},
        {"personal": "Jisus", "payment": "100000"}
    ]
    assert ReadJson("tests_1.json", vacancy).del_all("tests_1.json") == result


