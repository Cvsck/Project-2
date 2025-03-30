import unittest
from unittest.mock import Mock, patch

from src.api import HhRuAPI


class TestHhRuAPI(unittest.TestCase):
    @patch("src.api.requests.get")
    def test_connect(self, mock_get):
        """Тест успешного подключения."""
        mock_get.return_value = Mock(status_code=200)
        api = HhRuAPI()
        api._connect()

    @patch("src.api.requests.get")
    def test_get_vacancies(self, mock_get):
        """Тест получения вакансий."""
        mock_get.return_value = Mock(status_code=200, json=lambda: {"items": [{"name": "Python Developer"}]})
        api = HhRuAPI()
        vacancies = api.get_vacancies("Python")
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]["name"], "Python Developer")


if __name__ == "__main__":
    unittest.main()
