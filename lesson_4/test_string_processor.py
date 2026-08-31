import pytest
from string_processor import StringProcessor


# Позитивные тесты: проверяем заглавные буквы и точки
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Hello", "Hello."),        # Обычное слово, добавится точка
        ("Hello.", "Hello."),       # Точка уже есть, она не продублируется
        ("hello world", "Hello world.")  # Сделает первую букву заглавной
    ]
)
def test_process_positive(input_text, expected_output):
    assert StringProcessor.process(input_text) == expected_output


# Негативные тесты: проверяем пустую строку и пробелы
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", "."),                  # Пустая строка должна вернуть просто точку
        ("   ", "   .")             # Пробелы должны остаться, а в конце точка
    ]
)
def test_process_negative(input_text, expected_output):
    assert StringProcessor.process(input_text) == expected_output
