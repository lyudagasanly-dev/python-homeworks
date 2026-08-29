import pytest
from calc import Calc


def test_calc_operations():
    calculator = Calc()

    # Проверяем сложение, вычитание, умножение и деление
    assert calculator.sum(4, 5) == 9
    assert calculator.sub(10, 4) == 6
    assert calculator.mul(3, 4) == 12
    assert calculator.div(10, 2) == 5

    # Проверяем степень и среднее значение
    assert calculator.pow(2, 3) == 8
    assert calculator.avg([1, 2, 3, 4, 5]) == 3

    # Проверяем, что при делении на ноль правильно вызывается ошибка
    with pytest.raises(ArithmeticError):
        calculator.div(5, 0)
