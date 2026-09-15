from selenium import webdriver
from ShopPage import LoginPage, CatalogPage, CheckoutPage


def test_shop_checkout():
    # Запускаем браузер Firefox по условию задания
    driver = webdriver.Firefox()

    # 1. Открываем сайт магазина
    driver.get("https://saucedemo.com")

    # 2. Авторизуемся через LoginPage
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавляем товары и переходим в корзину через CatalogPage
    catalog_page = CatalogPage(driver)
    catalog_page.add_items_to_cart()
    catalog_page.go_to_cart()

    # 4. Оформляем заказ и проверяем итоговую цену через CheckoutPage
    checkout_page = CheckoutPage(driver)
    checkout_page.start_checkout()
    checkout_page.fill_customer_info("Иван", "Петров", "123456")

    total_price_text = checkout_page.get_total_price()

    # Закрываем браузер в коде теста
    driver.quit()

    # Проверяем итоговую сумму
    assert total_price_text == "Total: $58.29", (
        f"Ожидали Total: $58.29, но получили '{total_price_text}'"
    )
