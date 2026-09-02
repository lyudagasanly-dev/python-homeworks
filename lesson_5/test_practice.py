from selenium import webdriver
from selenium.webdriver.common.by import By


def test_page_title():
    # 1. Запускаем браузер
    driver = webdriver.Chrome()

    # 2. Открываем тестовый сайт
    driver.get("https://qa-territory.online")

    # 3. Находим элемент h1 по его тегу (TAG_NAME)
    title_element = driver.find_element(By.TAG_NAME, "h1")

    # 4. Получаем текст этого заголовка
    title_text = title_element.text

    # 5. Проверяем, что в тексте заголовка есть слово "httpbin"
    assert "httpbin" in title_text

    # 6. Обязательно закрываем браузер
    driver.quit()


def test_form_interaction():

    # Настройки против ошибки безопасности
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(options=options)
    driver.get("https://qa-territory.online")

    # 1. Находим поле по атрибуту name и вводим текст
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Иван Иванов")

    # 2. Находим кнопку Submit по тегу button и кликаем
    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()

    driver.quit()


def test_element_state():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com")

    # Находим радиокнопку Yes по её ID
    radio_yes = driver.find_element(By.ID, "yesRadio")

    # 1. Проверяем, что она отображается
    assert radio_yes.is_displayed()

    # 2. Проверяем, что она доступна для взаимодействия
    assert radio_yes.is_enabled()

    driver.quit()
