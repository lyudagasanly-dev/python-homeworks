from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_checkout():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 15)

    driver.get("https://saucedemo.com")

    user_field = (By.ID, "user-name")
    wait.until(EC.visibility_of_element_located(user_field)).send_keys(
        "standard_user"
    )
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    wait.until(EC.element_to_be_clickable(backpack)).click()

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
    ).click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    fn_field = (By.ID, "first-name")
    wait.until(EC.visibility_of_element_located(fn_field)).send_keys(
        "Иван"
    )
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    total_label = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        )
    )
    total_text = total_label.text

    driver.quit()

    assert total_text == "Total: $58.29", (
        f"Ожидали Total: $58.29, но получили '{total_text}'"
    )
