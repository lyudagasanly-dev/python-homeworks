from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    # Настройки против блокировки сайта браузером
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    # 1. Открываем правильную страницу со ссылками
    # 1. Открываем правильную страницу со ссылками
    start_url = "https://httpbin.qa-territory.online/links/10"
    driver.get(start_url)

    # 2. Находим ВСЕ ссылки на странице (тег a)
    links = driver.find_elements(By.TAG_NAME, "a")

    # 3. Проверяем, что количество ссылок равно 9
    assert len(links) == 9

    # 4. Проверяем, что все ссылки отображаются на странице
    for link in links:
        assert link.is_displayed()

    # 5. Проверяем, что текст первой ссылки содержит "1"
    assert "1" in links[0].text

    driver.quit()
