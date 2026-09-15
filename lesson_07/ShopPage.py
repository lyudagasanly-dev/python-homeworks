from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def login(self, username, password):
        """Выполняет авторизацию пользователя."""
        user_field = (By.ID, "user-name")
        self.wait.until(
            EC.visibility_of_element_located(user_field)
        ).send_keys(username)

        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_items_to_cart(self):
        """Добавляет три указанных товара в корзину."""
        backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.wait.until(EC.element_to_be_clickable(backpack)).click()

        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        self.driver.find_element
        (By.ID, "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self):
        """Переходит в корзину."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def start_checkout(self):
        """Нажимает кнопку Checkout в корзине."""
        checkout_btn = (By.ID, "checkout")
        self.wait.until(EC.element_to_be_clickable(checkout_btn)).click()

    def fill_customer_info(self, first_name, last_name, postal_code):
        """Заполняет форму оформления заказа."""
        fn_field = (By.ID, "first-name")
        self.wait.until(EC.visibility_of_element_located(fn_field)).send_keys(
            first_name
        )
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self):
        """Возвращает итоговую стоимость текстом со страницы подтверждения."""
        total_label = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total_label.text
