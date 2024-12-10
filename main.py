from src.API import HH
from src.data import ReadJson
from src.vacancy import ProcessingVacancies


# from src.vacancy import ProcessingVacancies


def user_info() -> list:
    """ Функция для взаимодействия с пользователем """
    keywords = input("Введите поисковой запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    name = input("Введите ключевые слова для фильтрации вакансий: ").lower().split(',')
    pay = input("Введите диапазон зарплат: ")
    lst = [name, top_n, keywords, pay]
    return lst


if __name__ == '__main__':
    # example = user_info()
    # # hh_example = HH(example).load_vacancies(example)
    # hh_example_1 = HH(example).expectation(example, HH(example).load_vacancies(example))
    # print(hh_example_1)
    lst_dct = [{'name': 'Специалист технической поддержки',
                'description': 'Знание английского языка на уровне B2. '
                'Хорошие коммуникативные навыки. Уверенное владение компьютером. '
                'Ориентированность на клиента, ответственность. Способность работать в...',
                'url': 'https://api.hh.ru/vacancies/110794669?host=hh.ru', 'pay': 100000},
               {'name': 'Бизнес-аналитик / аналитик данных',
                'description': 'опыт работы бизнес/дата аналитиком от 2х лет. '
                               '-знание продуктовых метрик, умение их анализировать и рассчитывать, '
                               'понимание unit-экономики. -',
                'url': 'https://api.hh.ru/vacancies/111258497?host=hh.ru', 'pay': 190000},
               {'name': 'Fullstack-разработчик',
                'description': 'Владение Docker и Linux для контейнеризации и деплоя приложений. '
                               '- Понимание работы Telegram API. - Знание <highlighttext>Python</highlighttext> '
                               'для выполнения вспомогательных задач. - ',
                'url': 'https://api.hh.ru/vacancies/112282417?host=hh.ru', 'pay': 225000},
               {'name': 'Финансовый инженер (Инвестиционный департамент)',
                'description': 'Отличная математическая подготовка. Хорошие навыки программирования. '
                               'Знание языков программирования: <highlighttext>Python</highlighttext> или C++/C#. '
                               'Как преимущество: знание основ market microstructure и...',
                'url': 'https://api.hh.ru/vacancies/112354348?host=hh.ru', 'pay': 150000},
               {'name': 'Старший инженер телематических сервисов',
                'description': '...bash, <highlighttext>python</highlighttext>, perl). '
                               'Понимание и работа с распределенной файловой системой (большой плюс знание ceph). '
                               'Опыт работ с VMWare, OpenStack, <highlighttext>Python</highlighttext>. ',
                'url': 'https://api.hh.ru/vacancies/103025623?host=hh.ru', 'pay': 126000},
               {'name': 'Инженер-программист',
                'description': 'Опыт программирования на одном или нескольких из языков: PHP, JavaScript, '
                               '<highlighttext>Python</highlighttext>. Опыт работы с виртуализацией, '
                               'СУБД и системами мониторинга (Zabbix). ',
                'url': 'https://api.hh.ru/vacancies/111228000?host=hh.ru', 'pay': 70000},
               {'name': 'Системный аналитик',
                'description': '...решении задач по ИИ (ML/DL): либо в качестве участника, '
                               'либо в качестве организатора. - Базовые знания <highlighttext>Python</highlighttext>,'
                               ' PHP, SQL, JS.', 'url': 'https://api.hh.ru/vacancies/111424862?host=hh.ru',
                'pay': 130000},
               {'name': 'DevOps-инженер',
                'description': 'Понимание принципов работы Kubernetes, Docker. '
                               'Английский язык (чтение технической документации). '
                               'Навыки программирования на скриптовых языках '
                               '(Bash / <highlighttext>Python</highlighttext> – хотя бы один...',
                'url': 'https://api.hh.ru/vacancies/107769333?host=hh.ru', 'pay': 174000},
               {'name': 'Системный администратор Linux',
                'description': 'Знание операционных систем Linux, CentOS на уровне администратора. '
                               'Знание сервисов AD, DNS, DHCP. Знание принципов администрирования почтовых серверов. ',
                'url': 'https://api.hh.ru/vacancies/110803498?host=hh.ru', 'pay': 90000},
               {'name': 'Системный аналитик',
                'description': 'Работа с реляционными СУБД, знание SQL для работы с данными; '
                               'умение читать код (языки C, Bash, Perl, <highlighttext>Python</highlighttext>). ',
                'url': 'https://api.hh.ru/vacancies/108400557?host=hh.ru', 'pay': 150000},
               {'name': 'Python разработчик',
                'description': 'Уверенное программирование на <highlighttext>Python</highlighttext> '
                               'или других скриптовых языках с желанием мигрировать на '
                               '<highlighttext>Python</highlighttext>. Навык написания чистых SQL-запросов '
                               '(без использования...', 'url': 'https://api.hh.ru/vacancies/110130589?host=hh.ru',
                'pay': 100000},
               {'name': 'Разработчик Unreal Engine Middle',
                'description': 'Разработка продвинутых AI систем. Необходим опыт:',
                'url': 'https://api.hh.ru/vacancies/110418735?host=hh.ru', 'pay': 100000},
               {'name': 'Главный дизайнер',
                'description': 'Cinema4D (Redshift), Blender – уверенно. '
                               'Twinmotion, Unreal Engine – большой плюс. Figma – уверенно. '
                               'Автоматизация (<highlighttext>Python</highlighttext>, JavaScript) – большой плюс.',
                'url': 'https://api.hh.ru/vacancies/110622355?host=hh.ru', 'pay': 200000},
               {'name': 'Разработчик Python (Django)',
                'description': 'Опыт работы с jQuery, Celery и RabbitMQ. -Основные технические навыки: '
                               '1. Django: - Отличное знание фреймворка Django и его компонентов. - ',
                'url': 'https://api.hh.ru/vacancies/111488923?host=hh.ru', 'pay': 180000},
               {'name': 'Младший системный администратор (Windows)',
                'description': 'Автоматизация работы путём написания скриптов: PowerShell, shell, '
                               '<highlighttext>python</highlighttext>. Опыт работы с ПО по резервному копированию '
                               '(Acronis, Veritas). Знание принципов работы...',
                'url': 'https://api.hh.ru/vacancies/110416530?host=hh.ru', 'pay': 80000},
               {'name': 'Инженер технической поддержки (2 линия)',
                'description': 'Работать в консоли Linux, для этого будет достаточно базовых знаний '
                               '(что это и для чего, ориентироваться на сервере через консоль). ',
                'url': 'https://api.hh.ru/vacancies/110425843?host=hh.ru', 'pay': 75000},
               {'name': 'Prompt-инженер',
                'description': 'Есть опыт работы с крупными языковыми моделями (LLM) от 1 года, '
                               'предпочтительно с ChatGPT и другими коммерческими моделями. ',
                'url': 'https://api.hh.ru/vacancies/110844686?host=hh.ru', 'pay': 200000},
               {'name': 'Системный администратор Linux',
                'description': 'Хорошее знание основ работы с Linux, OSI, TCP/IP. '
                               'Опыт написания Bash shell, <highlighttext>python</highlighttext> scripts - обязательно. '
                               'Опыт работы с GIT...',
                'url': 'https://api.hh.ru/vacancies/112189481?host=hh.ru', 'pay': 200000},
               {'name': 'Data Science NLP',
                'description': 'ФГАНУ НИИ «Спецвузавтоматика» относится к Министерству науки и образовании. '
                               'Осуществляем деятельность в области информационных технологий и безопасности.',
                'url': 'https://api.hh.ru/vacancies/111069878?host=hh.ru', 'pay': 100000},
               {'name': 'Системный администратор',
                'description': 'Будет преимуществом: - Знание скриптовых языков (<highlighttext>Python</highlighttext>, '
                               'Shell, Bash) на базовом уровне. - Опыт внедрения/настройки программных и '
                               'аппаратных ИТ-решений. - ', 'url': 'https://api.hh.ru/vacancies/111527398?host=hh.ru',
                'pay': 84000},
               {'name': 'Developer в AI студию разработки США (stack: LLM, fullstack, python, javascript, JS, n8n)',
                'description': 'Фокус 2: наши внутренние AI продукты: Идеально - опыт в хакатонах/олимпиадах.',
                'url': 'https://api.hh.ru/vacancies/111614950?host=hh.ru', 'pay': 552},
               {'name': 'Разработчик С/С++',
                'description': 'Oпыт оптимизации кода (как платформонезависимой, '
                               'так и ориентированной на конкретное "железо"). '
                               'Знание скриптовых языков (<highlighttext>Python</highlighttext>, Shell, Perl, etc.). ',
                'url': 'https://api.hh.ru/vacancies/110798257?host=hh.ru', 'pay': 250000},
               {'name': 'Сетевой инженер',
                'description': 'Будет преимуществом: Знание языков программирования Perl/'
                               '<highlighttext>Python</highlighttext>/Go, умение автоматизировать процессы. '
                               'Разговорный английский язык. Опыт работы с оборудованием сетей связи. ',
                'url': 'https://api.hh.ru/vacancies/110890087?host=hh.ru', 'pay': 180000},
               {'name': 'Программист-разработчик',
                'description': 'Практическое знание двух и более языков. '
                               'Опыт программирования на C/C++/<highlighttext>Python</highlighttext>. '
                               'Желательно знание SQL. Хорошее знание схемотехники. ',
                'url': 'https://api.hh.ru/vacancies/111746629?host=hh.ru', 'pay': 150000},
               {'name': 'Middle/Middle+ Data Engineer',
                'description': '...C++ и интеграции с <highlighttext>Python</highlighttext> для повышения '
                               'производительности. Знание pybind11 или других инструментов для вызова C++ кода '
                               'из <highlighttext>Python</highlighttext>.',
                'url': 'https://api.hh.ru/vacancies/111875669?host=hh.ru', 'pay': 300000},
               {'name': 'Сетевой инженер',
                'description': 'Навыки автоматизации сетевых процессов (скрипты, Ansible, '
                               '<highlighttext>Python</highlighttext>). Опыт работы с системами резервного '
                               'копирования и восстановления данных (Acronis). Готовность к обучению...',
                'url': 'https://api.hh.ru/vacancies/112433157?host=hh.ru', 'pay': 120000},
               {'name': 'Go-разработчик (Middle)',
                'description': 'Понимание принципов асинхронного программирования и опыт работы с очередями сообщений '
                               '(например, Kafka, RabbitMQ). Знание других языков программирования, таких как '
                               '<highlighttext>Python</highlighttext>...',
                'url': 'https://api.hh.ru/vacancies/110594444?host=hh.ru', 'pay': 400000},
               {'name': 'Python-разработчик/ Python Developer',
                'description': 'Отличное знание <highlighttext>Python</highlighttext> 3, '
                               'опыт использования от трех лет. Опыт разработки тест кейсов. '
                               'Опыт использования Docker. Опыт тестирования API и...',
                'url': 'https://api.hh.ru/vacancies/110958431?host=hh.ru', 'pay': 150000},
               {'name': 'Программист С++ GUI',
                'description': 'Английский язык (чтение технической документации). '
                               'Опыт разработки и отладки многопоточных приложений. '
                               'Опыт с <highlighttext>python</highlighttext>. Опыт с websocket. SQL.',
                'url': 'https://api.hh.ru/vacancies/111528957?host=hh.ru', 'pay': 80000},
               {'name': 'Аналитик',
                'description': 'Приветствуется наличие сертификатов по специализированным аналитическим инструментам '
                               '(SQL, <highlighttext>Python</highlighttext>, R, Power BI и др.). '
                               'Владение английским языком на уровне, достаточном...',
                'url': 'https://api.hh.ru/vacancies/112298470?host=hh.ru', 'pay': 45000},
               {'name': 'Аналитик маркетплейсов',
                'description': 'Опыт работы с инструментами аналитики данных, такими как '
                               '<highlighttext>Python</highlighttext>, SQL, Excel (макросы)l и другими. '
                               'Опыт контроля за оборачиваемостью товара...',
                'url': 'https://api.hh.ru/vacancies/112704459?host=hh.ru', 'pay': 150000},
               {'name': 'Data Scientist (Python, ML) / Дата-сайентист',
                'description': 'Хорошее знание стека технологий и библиотек, которые мы используем: '
                               '<highlighttext>python</highlighttext>, pandas, pyspark, lightgbm, scikit-learn. '
                               'Высокий уровень знаний по классическим...',
                'url': 'https://api.hh.ru/vacancies/108723293?host=hh.ru', 'pay': 250000},
               {'name': 'Data Architect',
                'description': 'Степень бакалавра в области компьютерных наук, инженерии, бизнеса или смежной области. '
                               'Не менее 10 лет практического опыта проектирования, разработки и...',
                'url': 'https://api.hh.ru/vacancies/110627398?host=hh.ru', 'pay': 588000},
               {'name': 'Программист',
                'description': 'Знание языков программирования (например, Java, C#, '
                               '<highlighttext>Python</highlighttext>, JavaScript и др.). '
                               'Опыт работы с системами контроля версий (например, Git). ',
                'url': 'https://api.hh.ru/vacancies/111207966?host=hh.ru', 'pay': 40000},
               {'name': 'Начальник аналитического отдела',
                'description': 'Опыт в проектировании баз данных. Опыт программирования на языке '
                               '<highlighttext>Python</highlighttext>. Опыт руководства коллективом. '
                               'Знание компьютерных программ на экспертном уровне. ',
                'url': 'https://api.hh.ru/vacancies/99569863?host=hh.ru', 'pay': 75000},
               {'name': 'Дежурный инженер технической поддержки',
                'description': 'Знаете принципы работы сети Internet. Умеете работать с почтовыми клиентами, '
                               'клиентами FTP и SSH, и знаете, как их настраивать. ',
                'url': 'https://api.hh.ru/vacancies/106019230?host=hh.ru', 'pay': 45000}]
    vacancy_1 = ProcessingVacancies(lst_dct, 4, ['python'], '50000')
    gt = vacancy_1.__gt__(50000)
    sort = vacancy_1.sort_for_top_n_vacancies(gt)
    # j = ReadJson(lst_dct)
    json = ReadJson('tests.json', sort)
    json_in_file = json.dict_to_json(sort, 'test.json')
    read = json.read_file('tests.json')
    j = ReadJson('test.json', lst_dct)
    print(j)



