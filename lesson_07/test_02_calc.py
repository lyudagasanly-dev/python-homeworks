from selenium import webdriver
from CalcPage import CalcPage


def test_slow_calculator():
    # Открываем Chrome по условию задания
    driver = webdriver.Chrome()

    # Создаем объект нашей страницы калькулятора
    calc_page = CalcPage(driver)

    # Выполняем шаги сценария по заданию
    calc_page.open_page()
    calc_page.set_delay("45")
    calc_page.click_button_by_text("7")
    calc_page.click_button_by_text("+")
    calc_page.click_button_by_text("8")
    calc_page.click_button_by_text("=")

    # Ждем появления результата и проверяем его через assert
    calc_page.wait_for_result("15")
    assert calc_page.get_result_text() == "15", (
        f"Ожидали 15, но получили {calc_page.get_result_text()}"
    )

    # Закрываем драйвер в тесте
    driver.quit()
