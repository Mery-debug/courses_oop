import pytest

from src.data import ReadJson


def test_dict_to_json(vacancy: list[dict], file_name: str) -> None:
    # assert ReadJson(file_name, vacancy).dict_to_json(vacancy, file_name) == f'Запись прошла успешно, новые вакансии: {vacancy} добавлены в файл'
