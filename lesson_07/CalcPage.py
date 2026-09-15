from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        # Ставим таймер ожидания с запасом, чтобы дождаться 45-сек. загрузки
        self.wait = WebDriverWait(driver, 65)

    def open_page(self):
        """Открывает точную страницу калькулятора."""
        url = (
           "https://bonigarcia.dev/selenium-webdriver-java/"
           "slow-calculator.html"
        )
        self.driver.get(url)

    def set_delay(self, delay_value):
        """Находит поле задержки, очищает его и вводит переданное значение."""
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(delay_value)

    def click_button_by_text(self, btn_text):
        """Нажимает на любую кнопку калькулятора по её тексту."""
        locator = f"//span[contains(@class, 'btn') and text()='{btn_text}']"
        self.driver.find_element(By.XPATH, locator).click()

    def wait_for_result(self, expected_result):
        """Ожидает появления конкретного текста на экране калькулятора."""
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected_result
            )
        )

    def get_result_text(self):
        """Возвращает текущий текст с экрана калькулятора."""
        return self.driver.find_element(By.CLASS_NAME, "screen").text
