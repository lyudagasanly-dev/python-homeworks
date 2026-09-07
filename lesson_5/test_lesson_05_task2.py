from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    # Настройки против блокировки сайта браузером
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    # 1. Открываем сразу страницу с анкетой
    start_url = "https://httpbin.qa-territory.online/forms/post"
    driver.get(start_url)

    # 2. Находим поле по атрибуту name и вводим имя
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Люда")

    # 3. Находим кнопку по тегу и кликаем
    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()

    # 4. Проверяем, что URL изменился после нажатия кнопки
    assert driver.current_url != start_url

    driver.quit()
