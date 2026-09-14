from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_controls():
    # Запускаем браузер Google Chrome
    driver = webdriver.Chrome()
    
    # Создаем удобную переменную для явных ожиданий (максимум 10 секунд)
    wait = WebDriverWait(driver, 10)
    
    # Открываем страницу тренажера
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    # Нажимаем кнопку Remove и ждем сообщения
    remove_btn = driver.find_element(By.XPATH, "//button[text()='Remove']")
    remove_btn.click()
    
    # Ждем, пока в элементе с id="message" появится именно текст "It's gone!"
    wait.until(
        EC.text_to_be_present_in_element((By.ID, "message"), "It's gone!")
    )
    
    # Находим этот элемент с текстом и проверяем его содержимое
    message_element = driver.find_element(By.ID, "message")
    assert message_element.text == "It's gone!", "Сообщение 'It's gone!' не появилось"
    
    # Нажимаем кнопку Enable
    enable_btn = driver.find_element(By.XPATH, "//button[text()='Enable']")
    enable_btn.click()
    
    # Ждем, когда поле ввода (input с атрибутом type='text') станет активным и кликабельным
    input_field = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
    )
    
    # Проверяем, что поле ввода действительно стало активным
    assert input_field.is_enabled(), "Поле ввода не стало активным"
    
    # Дополнительная проверка — вводим текст и проверяем записанное значение
    input_field.send_keys("Hello World")
    assert input_field.get_attribute("value") == "Hello World", "Текст в поле ввода не совпадает"
    
    # Закрываем браузер
    driver.quit()

