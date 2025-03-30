import unittest
import os
import json
from src.fileworker import JsonVacancyStorage

class TestJsonVacancyStorage(unittest.TestCase):
    def setUp(self):
        """Создаём временный файл перед тестами."""
        self.test_file = "test_vacancies.json"
        self.storage = JsonVacancyStorage(self.test_file)

    def tearDown(self):
        """Удаляем временный файл после тестов."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_vacancy(self):
        """Тест добавления вакансии."""
        vacancy = {
            "title": "Python Developer",
            "link": "https://example.com",
            "salary": "100000 - 150000 RUR",
            "description": "Опыт работы с Python 3+ лет."
        }

        # Добавляем вакансию
        self.storage.add_vacancy(vacancy)

        # Проверяем, что вакансия добавлена
        with open(self.test_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["Вакансия"], "Python Developer")

if __name__ == "__main__":
    unittest.main()
