from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_page(self):
        """Открывает страницу тренажера с формой."""
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java"
            "data-types.html"
        )
        self.driver.get(url)

    def fill_form(self):
        """Заполняет все поля формы, кроме Zip code."""
        # Ожидаем загрузки первого поля
        first_name = self.wait.until(
            EC.presence_of_element_located((By.NAME, "first-name"))
        )
        first_name.send_keys("Иван")
        # Заполняем остальные поля напрямую
        self.driver.find_element(By.NAME, "last-name").send_keys("Петров")
        self.driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        self.driver.find_element
        (By.NAME, "e-mail").send_keys("test@skypro.com")
        self.driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        self.driver.find_element(By.NAME, "city").send_keys("Москва")
        self.driver.find_element(By.NAME, "country").send_keys("Россия")
        self.driver.find_element(By.NAME, "job-position").send_keys("QA")
        self.driver.find_element(By.NAME, "company").send_keys("SkyPro")

    def click_submit(self):
        """Нажимает кнопку отправки формы."""
        submit_btn = self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        submit_btn.click()

    def get_zip_code_class(self):
        """Ждет покраснения поля Zip code и возвращает его HTML-класс."""
        self.wait.until(
            EC.text_to_be_present_in_element_attribute(
                (By.ID, "zip-code"), "class", "alert-danger"
            )
        )
        zip_code_element = self.driver.find_element(By.ID, "zip-code")
        return zip_code_element.get_attribute("class")

    def get_field_class_by_id(self, field_id):
        """Возвращает HTML-класс любого поля по его ID."""
        field = self.driver.find_element(By.ID, field_id)
        return field.get_attribute("class")
