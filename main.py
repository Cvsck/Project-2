from src.api import HhRuAPI
from src.fileworker import JsonVacancyStorage
from src.utils import get_user_search_query, get_user_top_n, get_user_filter_keywords, get_user_salary, \
    filter_vacancies_by_keywords, filter_vacancies_by_salary, display_vacancies
from src.vacancy import Vacancy


def user_interaction():
    """
    Функция взаимодействия с пользователем.
    Объединяет запрос данных с hh.ru, фильтрацию вакансий и сохранение результатов.
    """
    print("Добро пожаловать в систему поиска вакансий!\n")

    # Создание объектов для работы с API и файлом
    storage = JsonVacancyStorage("Data/vacancies.json")
    hh_api = HhRuAPI()

    # Ввод данных от пользователя
    search_query = get_user_search_query()
    top_n = get_user_top_n()
    filter_keywords = get_user_filter_keywords()
    salary = get_user_salary()

    try:
        # Получение вакансий через API hh.ru
        print(f"\nЗапрос вакансий с ключевым словом '{search_query}'...")
        raw_vacancies = hh_api.get_vacancies(keyword=search_query, page=0, per_page=100)

        # Преобразование вакансий из JSON в объекты Vacancy
        vacancies = Vacancy.cast_to_object_list(raw_vacancies)
        print(f"Получено {len(vacancies)} вакансий от hh.ru.")

        # Фильтрация вакансий по ключевым словам
        filtered_by_keywords = filter_vacancies_by_keywords(
            [{"title": v.title, "salary": v.salary, "description": v.description, "link": v.link} for v in vacancies],
            filter_keywords,
        )

        # Фильтрация вакансий по зарплате
        filtered_by_salary = filter_vacancies_by_salary(filtered_by_keywords, salary)

        # Сохранение подходящих вакансий в файл
        for vacancy in filtered_by_salary:
            storage.add_vacancy(vacancy)

        # Вывод подходящих вакансий
        print("\nРезультаты:")
        display_vacancies(filtered_by_salary, top_n)

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    user_interaction()
