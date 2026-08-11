def is_year_leap(year):

    if year % 4 == 0:
        return True
    else:
        return False


year = 2024
otvet = is_year_leap(year)

print("год", year, ":", otvet)
year = 2025
otvet = is_year_leap(year)

print("год", year, ":", otvet)
