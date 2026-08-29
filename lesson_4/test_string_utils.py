import pytest
from string_utils import StringUtils

utils = StringUtils()


# ==========================================
# 1. ТЕСТЫ ДЛЯ МЕТОДА capitalize (Заглавная буква)
# ==========================================
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("04 апреля 2023", "04 апреля 2023"),
        ("Тест", "Тест"),
        ("", ""),
        (" ", " ")
    ]
)
def test_capitalize(input_str, expected):
    assert utils.capitalize(input_str) == expected


# ==========================================
# 2. ТЕСТЫ ДЛЯ МЕТОДА trim (Удаление пробелов в начале)
# ==========================================
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        ("skypro", "skypro"),
        ("  04 апреля", "04 апреля"),
        ("", ""),
        ("   ", "")
    ]
)
def test_trim(input_str, expected):
    assert utils.trim(input_str) == expected


# ==========================================
# 3. ТЕСТЫ ДЛЯ МЕТОДА contains (Содержит ли символ)
# ==========================================

@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "P", True),
        ("SkyPro", "U", False),
        ("123", "2", True),
        ("", "A", False),
        ("SkyPro", "", False)
    ]
)
def test_contains(input_str, symbol, expected):
    assert utils.contains(input_str, symbol) == expected


# ==========================================
# 4. ТЕСТЫ ДЛЯ МЕТОДА delete_symbol (Удаление символа)
# ==========================================
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("04 апреля 2023", " ", "04апреля2023"),
        ("123", "2", "13"),
        ("", "A", ""),
        ("SkyPro", "Z", "SkyPro")
    ]
)
def test_delete_symbol(input_str, symbol, expected):
    assert utils.delete_symbol(input_str, symbol) == expected
