def month_to_season(month):
    # 1. Проверяем зимние месяцы
    if month == 12 or month == 1 or month == 2:
        return "Зима"

    # 2. Иначе если весенние месяцы
    elif month == 3 or month == 4 or month == 5:
        return "Весна"

    # 3. Иначе если летние месяцы
    elif month == 6 or month == 7 or month == 8:
        return "Лето"

    # 4. Иначе если осенние месяцы
    elif month == 9 or month == 10 or month == 11:
        return "Осень"

    # 5. Если ввели неправильный номер (например, 15 или 0)
    else:
        return "Неверный номер месяца"


print(month_to_season(2))
print(month_to_season(7))
print(month_to_season(11))
