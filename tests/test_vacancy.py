import unittest

from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):
    def test_vacancy_creation(self):
        """Тест создания объекта Vacancy."""
        vacancy = Vacancy(
            "Python Developer", "https://example.com", "100000 - 150000 RUR", "Требуется опыт работы с Python."
        )

        self.assertEqual(vacancy.title, "Python Developer")
        self.assertEqual(vacancy.link, "https://example.com")
        self.assertEqual(vacancy.salary, "100000 - 150000 RUR")
        self.assertEqual(vacancy.description, "Требуется опыт работы с Python.")

    def test_vacancy_str(self):
        """Тест строкового представления объекта Vacancy."""
        vacancy = Vacancy(
            "Python Developer", "https://example.com", "100000 - 150000 RUR", "Требуется опыт работы с Python."
        )

        expected_output = (
            "Вакансия: Python Developer\n"
            "Ссылка: https://example.com\n"
            "Зарплата: 100000 - 150000 RUR\n"
            "Описание: Требуется опыт работы с Python."
        )
        self.assertEqual(str(vacancy), expected_output)

    def test_cast_to_object_list(self):
        """Тест преобразования JSON в список объектов Vacancy."""
        vacancies_json = [
            {
                "name": "Python Developer",
                "alternate_url": "https://example.com",
                "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
                "snippet": {
                    "requirement": "Опыт работы с Python 3+ лет.",
                    "responsibility": "Разработка веб-приложений.",
                },
            },
            {
                "name": "Data Scientist",
                "alternate_url": "https://example2.com",
                "salary": None,
                "snippet": {"requirement": None, "responsibility": None},
            },
        ]

        vacancies = Vacancy.cast_to_object_list(vacancies_json)

        self.assertEqual(len(vacancies), 2)

        self.assertEqual(vacancies[0].title, "Python Developer")
        self.assertEqual(vacancies[0].link, "https://example.com")
        self.assertEqual(vacancies[0].salary, "100000 - 150000 RUR")
        self.assertEqual(vacancies[0].description, "Опыт работы с Python 3+ лет. Разработка веб-приложений.")

        self.assertEqual(vacancies[1].title, "Data Scientist")
        self.assertEqual(vacancies[1].link, "https://example2.com")
        self.assertEqual(vacancies[1].salary, "Зарплата не указана")
        self.assertEqual(vacancies[1].description, "Описание отсутствует")


if __name__ == "__main__":
    unittest.main()
