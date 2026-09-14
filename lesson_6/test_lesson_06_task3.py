from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_ajax_content():
    # Запускаем браузер Google Chrome
    driver = webdriver.Chrome()
    
    # Создаем таймер явного ожидания (в эталоне просят 15 секунд, так как AJAX может грузиться дольше)
    wait = WebDriverWait(driver, 15)
    
    # 1. Открываем правильную страницу тренажера
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Нажимаем кнопку Start
    start_btn = driver.find_element(By.XPATH, "//button[text()='Start']")
    start_btn.click()
    
    # 3. Ждем появления элемента с текстом "Hello World!" на экране
    hello_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
    )
    
    # Проверяем, что элемент виден и текст совпадает через обычный Selenium
    assert hello_element.is_displayed(), "Элемент с текстом 'Hello World!' не отобразился"
    assert hello_element.text == "Hello World!", f"Текст элемента не 'Hello World!', а '{hello_element.text}'"
    
    # 4. Используем JavaScript для получения текста элемента напрямую из браузера
    text_via_js = driver.execute_script("return arguments[0].textContent;", hello_element)
    
    # 5. Проверяем, что текст, полученный через JS, равен "Hello World!"
    assert text_via_js == "Hello World!", f"Текст через JavaScript не 'Hello World!', а '{text_via_js}'"
    
    # 6. Дополнительная проверка — элемент находится в DOM и виден
    assert hello_element.is_displayed(), "Элемент не видим на странице"
    
    # Закрываем браузер после успешного теста
    driver.quit()
