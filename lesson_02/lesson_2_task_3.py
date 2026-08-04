import math


def square(storona):
    # Вычисляем площадь квадрата
    area = storona * storona

    # Округляем результат вверх и возвращаем его
    return math.ceil(area)


# Пример проверки работы функции:
print(square(5))
print(square(4.1))
