import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from even_odd import check_even_odd

def test_even_odd():
    """Тестирование функции проверки четности/нечетности числа."""
    assert check_even_odd(2) == "Четное число"
    assert check_even_odd(3) == "Нечетное число"
    assert check_even_odd(0) == "Четное число"
    assert check_even_odd(-1) == "Нечетное число"

def test_odd_number():
    assert check_even_odd(12) == "Четное число"

if __name__ == "__main__":
    test_even_odd()
    print("Все тесты пройдены успешно!")
