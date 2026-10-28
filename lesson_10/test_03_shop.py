import allure
from selenium import webdriver
from ShopPage import LoginPage, CatalogPage, CheckoutPage


@allure.epic("Интернет-магазин Saucedemo")
@allure.feature("Оформление заказа")
@allure.story("Покупка нескольких товаров")
@allure.title("Успешное оформление заказа с проверкой итоговой стоимости")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_checkout() -> None:
    """Тест проверяет полный цикл покупки"""

    with allure.step("Запуск браузера Firefox"):
        driver = webdriver.Firefox()

    try:
        with allure.step("Авторизация в магазине"):
            login_page = LoginPage(driver)
            login_page.open_page()
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
            catalog_page = CatalogPage(driver)
            catalog_page.add_items_to_cart()
            catalog_page.go_to_cart()

        with allure.step("Заполнение данных покупателя"):
            checkout_page = CheckoutPage(driver)
            checkout_page.start_checkout()
            checkout_page.fill_customer_info("Иван", "Петров", "123456")

        with allure.step("Получение итоговой стоимости заказа"):
            total_price_text = checkout_page.get_total_price()

        with allure.step("Проверка соответствия цены ожидаемой сумме"):
            assert total_price_text == "Total: $58.29", (
                f"Ожидали Total: $58.29, но получили '{total_price_text}'"
            )

    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
