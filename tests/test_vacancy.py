from src.vacancy import ProcessingVacancies


def test_processing_vacancy_str() -> None:
    vacancies = [
        {"personal": "Jhon doe", "payment": "50000"},
        {"personal": "Jisus", "payment": "100000"}
    ]
    process = ProcessingVacancies(vacancies, 5, ['python'], '50000')
    assert str(process) == f"ProcessingVacancies ({vacancies}, 5, ['python'], 50000)"


def test_sort_for_top_n_vacancies() -> None:
    vacancies = [
        {"personal": "Jhon doe", "payment": "50000"},
        {"personal": "Jisus", "payment": "20000"},
        {"personal": "Jisu", "payment": "300000"},
        {"personal": "Jiss", "payment": "44440"},
        {"personal": "Jius", "payment": "100"}
    ]
    process = ProcessingVacancies(vacancies, 3, ['python'], '50000')
    assert process.sort_for_top_n_vacancies(vacancies) == vacancies[:3]

