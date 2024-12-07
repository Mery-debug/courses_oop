from pathlib import Path

import pytest


@pytest.fixture
def vacancy() -> list[dict]:
    return [
        {
            "id": "106796145",
            "premium": False,
            "name": "Специалист по внутренней отчётности",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "salary": {"from": 150000, "to": 200000, "currency": "RUR", "gross": True},
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": None,
                "street": None,
                "building": None,
                "lat": None,
                "lng": None,
                "description": None,
                "raw": None,
                "metro": {
                    "station_name": "Серпуховская",
                    "line_name": "Серпуховско-Тимирязевская",
                    "station_id": "9.37",
                    "line_id": "9",
                    "lat": 55.726548,
                    "lng": 37.624792,
                },
                "metro_stations": [
                    {
                        "station_name": "Серпуховская",
                        "line_name": "Серпуховско-Тимирязевская",
                        "station_id": "9.37",
                        "line_id": "9",
                        "lat": 55.726548,
                        "lng": 37.624792,
                    }
                ],
                "id": "5702808",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2024-11-24T17:11:46+0300",
            "created_at": "2024-11-24T17:11:46+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=106796145",
            "show_logo_in_search": None,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/106796145?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/106796145",
            "relations": [],
            "employer": {
                "id": "1169425",
                "name": "HIPER",
                "url": "https://api.hh.ru/employers/1169425",
                "alternate_url": "https://hh.ru/employer/1169425",
                "logo_urls": {
                    "90": "https://img.hhcdn.ru/employer-logo/4266880.jpeg",
                    "240": "https://img.hhcdn.ru/employer-logo/4266881.jpeg",
                    "original": "https://img.hhcdn.ru/employer-logo-original/956588.jpg",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1169425",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Встроенные в Excel инструменты извлечения, подготовки, обработки данных PowerQuery, "
                               "PowerPivot. - VBA или <highlighttext>Python</highlighttext>, умение создавать макросы. - "
                               "PowerBI - загрузка данных, создание...",
                "responsibility": "Использование DAX в данных Excel и PowerBI. - Построение запросов на SQL. - "
                                  "<highlighttext>Python</highlighttext> для задач сбора и анализа данных.",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "professional_roles": [{"id": "10", "name": "Аналитик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between3And6", "name": "От 3 до 6 лет"},
            "employment": {"id": "full", "   name": "Полная занятость"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        },
        {
            "id": "109545918",
            "premium": False,
            "name": "Специалист по работе с информационными системами",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {
                "id": "41",
                "name": "Калининград",
                "url": "https://api.hh.ru/areas/41",
            },
            "salary": {"from": None, "to": 60000, "currency": "RUR", "gross": False},
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Калининград",
                "street": "улица Александра Невского",
                "building": "14",
                "lat": 54.724775,
                "lng": 20.527879,
                "description": None,
                "raw": "Калининград, улица Александра Невского, 14",
                "metro": None,
                "metro_stations": [],
                "id": "11716743",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2024-10-29T12:18:12+0300",
            "created_at": "2024-10-29T12:18:12+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109545918",
            "show_logo_in_search": None,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/109545918?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/109545918",
            "relations": [],
            "employer": {
                "id": "882766",
                "name": "ФГАОУ ВО Балтийский Федеральный университет имени Иммануила Канта",
                "url": "https://api.hh.ru/employers/882766",
                "alternate_url": "https://hh.ru/employer/882766",
                "logo_urls": {
                    "90": "https://img.hhcdn.ru/employer-logo/6774958.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/1288665.png",
                    "240": "https://img.hhcdn.ru/employer-logo/6774959.png",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=882766",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "IT образование (высшее). Не менее 1 года опыт работы системного администрирования: "
                               "выполнение задач по настройке ПО, в качестве специалиста технической...",
                "responsibility": "...IBM_SPSS, MatLab, GIMP, DaVinci Resolve, Darktable, Anaconda, Delphi7, "
                                  "Visual Studio, OBS Studio, <highlighttext>Python</highlighttext>, Virtual Box ) и "
                                  "систем электронного документооборота.",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "professional_roles": [{"id": "113", "name": "Системный администратор"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        },
        {
            "id": "109832789",
            "premium": False,
            "name": "Системный аналитик DWH",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "salary": None,
            "type": {"id": "open", "name": "Открытая"},
            "address": None,
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2024-11-01T11:06:03+0300",
            "created_at": "2024-11-01T11:06:03+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=109832789",
            "branding": {"type": "MAKEUP", "tariff": None},
            "show_logo_in_search": True,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/109832789?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/109832789",
            "relations": [],
            "employer": {
                "id": "49357",
                "name": "МАГНИТ, Розничная сеть",
                "url": "https://api.hh.ru/employers/49357",
                "alternate_url": "https://hh.ru/employer/49357",
                "logo_urls": {
                    "90": "https://img.hhcdn.ru/ichameleon/310823.png",
                    "240": "https://img.hhcdn.ru/ichameleon/310823.png",
                    "original": "https://img.hhcdn.ru/ichameleon/310823.png",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=49357",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Уверенное владение Excel, <highlighttext>Python</highlighttext>, SQL. Опыт разработки "
                               "ETL/ELT. Знание инструментов BI. Знание подходов Agile/Scrum.",
                "responsibility": "Выявлять требования к данным, сценарии их использования и анализа в КХД и отчетности в "
                                  "тесном взаимодействии с бизнес-подразделениями. ",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "professional_roles": [{"id": "148", "name": "Системный аналитик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }]


@pytest.fixture
def lst() -> list:
    return ['python', 5, 'junior', '50000-10000']


@pytest.fixture
def file_name() -> str:
    return '../../data/tests.json'
