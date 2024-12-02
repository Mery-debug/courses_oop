# Курсовой проект "Поиск вакансий"

## Описание:

Курсовой проект, направленный на отработку знаний полученных в курсе 4. Объектно-ориентированное программирование.
Требовалось реализовать поиск вакансий с помощью АПИ от hh.ru, при помощи классов, принципа наследования, абстрактного 
класса, инкапсуляции и полиморфизма. А так же класс в котором получаемый ответ преобразуется в json-файл. 

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Mery-debug/
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:




## Классы:




## Тестирование:

Проект покрыт тестами не менее чем на 75% (97%). 
Ссылка на файл с подробной информацией на покрытие кода проекта тестами: [index.html](index.html)
Тесты запускаются командой pytest из терминала проекта.
Для каждого модуля папки src создан соответствующий модуль в папке tests, называющийся test_<имя тестируемого модуля>.py.
В тестовых модулях, для удобства тестирования вызываемых ошибок сделаны классы TestCase, наследуемые от класса 
unittest.TestCase которые упрощают работу с ошибками типа TypeError. 

## Соответствие PEP8:

Проект проверен линтерами: isort, black, flake8 и mypy. Ошибок или правок в нем не обнаружено.

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).