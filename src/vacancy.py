class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ('__title', '__link', '__salary', '__description')

    def __init__(self, title, link, salary, description):
        self.__title = title
        self.__link = link
        self.__salary = salary
        self.__description = description

    # Геттеры
    @property
    def title(self):
        return self.__title

    @property
    def link(self):
        return self.__link

    @property
    def salary(self):
        return self.__salary

    @property
    def description(self):
        return self.__description

    # Преобразование JSON в список объектов Vacancy
    @staticmethod
    def cast_to_object_list(vacancies_json):
        """Преобразует JSON в список объектов Vacancy."""
        vacancies = []
        for item in vacancies_json:
            title = item.get("name", "Не указано")
            link = item.get("alternate_url", "Не указано")
            salary = Vacancy.__parse_salary(item.get("salary"))
            requirement = item.get("snippet", {}).get("requirement") or ""  # Заменяем None на пустую строку
            responsibility = item.get("snippet", {}).get("responsibility") or ""  # Заменяем None на пустую строку
            description = (requirement + " " + responsibility).strip() or "Описание отсутствует"
            vacancies.append(Vacancy(title, link, salary, description))
        return vacancies

    # Метод для форматирования зарплаты
    @staticmethod
    def __parse_salary(salary):
        if salary is None:
            return "Зарплата не указана"
        salary_from = salary.get("from", "Не указано")
        salary_to = salary.get("to", "Не указано")
        currency = salary.get("currency", "")
        return f"{salary_from} - {salary_to} {currency}"

    # Удобный вывод объекта Vacancy
    def __str__(self):
        return (
            f"Вакансия: {self.title}\n"
            f"Ссылка: {self.link}\n"
            f"Зарплата: {self.salary}\n"
            f"Описание: {self.description}"
        )
