from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 15)

    url = (
        "https://bonigarcia.dev"
        "data-types.html"
    )
    driver.get(url)

    first_name = wait.until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    )

    first_name.send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")

    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_btn = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )
    submit_btn.click()

    wait.until(
        EC.text_to_be_present_in_element_attribute(
            (By.ID, "zip-code"), "class", "alert-danger"
        )
    )

    zip_code = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code.get_attribute("class"), (
        "Поле Zip code не подсвечено красным!"
    )

    green_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class"), (
            f"Поле {field_id} не подсвечено зеленым!"
        )

    driver.quit()
