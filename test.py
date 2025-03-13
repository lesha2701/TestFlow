import unittest

# Функция, которую мы будем тестировать
def add(a, b):
    return a + b

# Класс для тестирования
class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        # Проверяем, что 2 + 3 = 5
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        # Проверяем, что (-1) + (-1) = -2
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        # Проверяем, что 0 + 0 = 0
        self.assertEqual(add(0, 0), 0)

# Запуск тестов
if __name__ == '__main__':
    unittest.main()