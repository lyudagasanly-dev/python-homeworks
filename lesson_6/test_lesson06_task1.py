from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    driver.get("https://herokuapp.com")

    start_btn = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_btn.click()

    hello_text_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    driver.save_screenshot("step4_page_screenshot.png")

    assert hello_text_element.text == "Hello World!", (
        f"Ожидали 'Hello World!', но получили '{hello_text_element.text}'"
    )

    driver.quit()
