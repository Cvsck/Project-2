from typing import Dict, List, Optional


def get_user_search_query() -> str:
    """
    Запрашивает у пользователя поисковый запрос для поиска вакансий.
    :return: Строка с ключевым словом или поисковым запросом.
    """
    query = input("Введите поисковый запрос для поиска вакансий (например, 'Python'): ").strip()
    if not query:
        print("Поисковый запрос не может быть пустым.")
        return get_user_search_query()  # Рекурсивный вызов для повторного ввода
    return query


def get_user_top_n() -> int:
    """
    Запрашивает у пользователя количество вакансий для вывода в топ N.
    :return: Целое число N (количество вакансий для вывода).
    """
    try:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        if top_n <= 0:
            raise ValueError("Число вакансий должно быть положительным.")
        return top_n
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return get_user_top_n()  # Рекурсивный вызов для повторного ввода


def get_user_filter_keywords() -> List[str]:
    """
    Запрашивает у пользователя ключевые слова для фильтрации вакансий.
    :return: Список ключевых слов.
    """
    keywords = input("Введите ключевые слова для фильтрации вакансий (например, 'опыт, Django'): ").strip()
    return [keyword.strip().lower() for keyword in keywords.split(",") if keyword]


def get_user_salary() -> Optional[int]:
    """
    Запрашивает у пользователя сумму зарплаты для фильтрации вакансий.
    :return: Целое число или None (если пользователь ничего не ввел).
    """
    salary_input = input("Введите сумму зарплаты (например, 100000): ").strip()
    if not salary_input:
        return None
    try:
        salary = int(salary_input)
        if salary < 0:
            raise ValueError("Сумма зарплаты должна быть положительным числом.")
        return salary
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return get_user_salary()  # Рекурсивный вызов для повторного ввода


def filter_vacancies_by_keywords(vacancies: List[Dict], keywords: List[str]) -> List[Dict]:
    """
    Фильтрует вакансии по ключевым словам в описании.
    :param vacancies: Список вакансий.
    :param keywords: Список ключевых слов для фильтрации.
    :return: Список вакансий, удовлетворяющих условиям.
    """
    if not isinstance(keywords, list):  # Проверка типа
        raise TypeError("filter_keywords должен быть списком строк.")

    return [
        vacancy
        for vacancy in vacancies
        if any(keyword in (vacancy.get("description", "").lower()) for keyword in keywords)
    ]


def filter_vacancies_by_salary(vacancies: List[Dict], salary: Optional[int]) -> List[Dict]:
    """
    Фильтрует вакансии по указанной зарплате.
    :param vacancies: Список вакансий.
    :param salary: Сумма зарплаты для фильтрации.
    :return: Список вакансий, удовлетворяющих условиям.
    """
    if salary is None:
        return vacancies

    filtered_vacancies = []
    for vacancy in vacancies:
        salary_data = vacancy.get("salary")
        if not salary_data or not isinstance(salary_data, str):  # Проверяем, что salary — строка
            print(f"Некорректное поле salary: {salary_data}")  # Отладочный вывод
            continue

        try:
            salary_parts = salary_data.replace(" ", "").split("-")  # Удаляем пробелы и разделяем диапазон
            salary_min = int(salary_parts[0]) if salary_parts[0].isdigit() else 0
            if salary_min >= salary:
                filtered_vacancies.append(vacancy)
        except (ValueError, IndexError):
            print(f"Ошибка обработки salary: {salary_data}")  # Отладочный вывод
            continue

    return filtered_vacancies


def display_vacancies(vacancies: List[Dict], top_n: Optional[int] = None) -> None:
    """
    Выводит список вакансий в консоль.
    :param vacancies: Список вакансий в формате словарей.
    :param top_n: Количество вакансий для отображения (если None, отображаются все).
    """
    if not vacancies:
        print("\nНет подходящих вакансий!")
        return

    print("\nТоп вакансий:")
    for i, vacancy in enumerate(vacancies[:top_n], start=1):
        print(
            f"\n{i}. Вакансия: {vacancy.get('title')}\n"
            f"   Ссылка: {vacancy.get('link')}\n"
            f"   Зарплата: {vacancy.get('salary')}\n"
            f"   Описание: {vacancy.get('description')}"
        )
