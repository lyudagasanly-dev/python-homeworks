def fizz_buzz(n, chislo=1):
    # Если наше число стало больше чем n, останавливаемся
    if chislo > n:
        return

    # Проверяем текущее число
    if chislo % 3 == 0 and chislo % 5 == 0:
        print("FizzBuzz")
    elif chislo % 3 == 0:
        print("Fizz")
    elif chislo % 5 == 0:
        print("Buzz")
    else:
        print(chislo)

    fizz_buzz(n, chislo + 1)


fizz_buzz(17)
