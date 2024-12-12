from unittest.mock import Mock, patch

from src.API import HH


@patch("requests.get")
def test_api(mocked_get):
    response = Mock(status_code=200)
    response.json.return_value = {"items": [{"name": "python developer"}]}
    mocked_get.return_value = response
    result = HH(["python", 4, "junior", "50000-10000"]).load_vacancies(["python"])
    assert result == [{"name": "python developer"}]


@patch("requests.get")
def test_api_failed(mocked_get: Mock) -> None:
    response = Mock(status_code=400)
    response.json.return_value = 400
    mocked_get.return_value = response
    result = HH(["python", 4, "junior", "50000-10000"]).load_vacancies(["python"])
    assert result == f"Возможная причина {response.reason}"


def test_expectation(lst, vacancy: list[dict]) -> None:
    total = HH(lst).expectation(lst, vacancy)
    assert total == [
        {
            "description": "Встроенные в Excel инструменты извлечения, подготовки, "
            "обработки данных PowerQuery, PowerPivot. - VBA или <highlighttext>Python</highlighttext>, "
            "умение создавать макросы. - PowerBI - загрузка данных, создание...",
            "name": "Специалист по внутренней отчётности",
            "pay": 150000,
            "url": "https://api.hh.ru/vacancies/106796145?host=hh.ru",
        },
        {
            "description": "IT образование (высшее). Не менее 1 года опыт работы системного администрирования: "
            "выполнение задач по настройке ПО, в качестве специалиста технической...",
            "name": "Специалист по работе с информационными системами",
            "pay": 60000,
            "url": "https://api.hh.ru/vacancies/109545918?host=hh.ru",
        },
    ]
