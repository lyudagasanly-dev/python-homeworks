from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(options=options)

    # Говорим браузеру подождать до 10 секунд
    driver.implicitly_wait(10)

    base_url = "https://httpbin.qa-territory.online"
    driver.get(base_url)

    # Находим ссылку и кликаем
    link = driver.find_element(By.LINK_TEXT, "HTML Form")
    link.click()

    # Проверяем, что URL изменился
    assert driver.current_url == f"{base_url}/forms/post"

    # Возвращаемся назад
    driver.back()

    # Проверяем, что вернулись на исходный URL
    assert driver.current_url == f"{base_url}/"

    driver.quit()
