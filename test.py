def clean_code(raw_code):
    """
    Преобразует строку с escape-последовательностями в читаемый код.
    Заменяет \r\n и \n на символы новой строки.
    """
    # Заменяем \r\n на \n (унифицируем символы новой строки)
    cleaned_code = raw_code.replace('\r\n', '\n')
    return cleaned_code

# Пример использования
raw_code = (
    "import unittest\r\n\r\n# Функция, которую мы будем тестировать\r\ndef add(a, b):\r\n    return a + b\r\n\r\n"
    "# Класс для тестирования\r\nclass TestAddition(unittest.TestCase):\r\n    def test_add_positive_numbers(self):\r\n"
    "        # Проверяем, что 2 + 3 = 5\r\n        self.assertEqual(add(2, 3), 5)\r\n\r\n    def test_add_negative_numbers(self):\r\n"
    "        # Проверяем, что (-1) + (-1) = -2\r\n        self.assertEqual(add(-1, -1), -2)\r\n\r\n    def test_add_zero(self):\r\n"
    "        # Проверяем, что 0 + 0 = 0\r\n        self.assertEqual(add(0, 0), 0)\r\n\r\n# Запуск тестов\r\n"
    "if __name__ == '__main__':\r\n    unittest.main()"
)

cleaned_code = clean_code(raw_code)
print(cleaned_code)