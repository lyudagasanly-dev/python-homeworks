from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 65)

    url = (
        "https://bonigarcia.dev"
        "slow-calculator.html"
    )
    driver.get(url)

    delay_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
    )

    delay_input.clear()
    delay_input.send_keys("45")

    btn_7 = "//span[contains(@class, 'btn') and text()='7']"
    btn_plus = "//span[contains(@class, 'btn') and text()='+']"
    btn_8 = "//span[contains(@class, 'btn') and text()='8']"
    btn_equal = "//span[contains(@class, 'btn') and text()='=']"

    driver.find_element(By.Xpath, btn_7).click()
    driver.find_element(By.Xpath, btn_plus).click()
    driver.find_element(By.Xpath, btn_8).click()
    driver.find_element(By.Xpath, btn_equal).click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), "15"
        )
    )

    result_screen = driver.find_element(By.CLASS_NAME, "screen")
    assert result_screen.text == "15", (
        f"Ожидали 15, но получили {result_screen.text}"
    )

    driver.quit()
