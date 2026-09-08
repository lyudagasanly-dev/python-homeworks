from selenium import webdriver


def test_session_storage_auth():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)

    driver.get("https://gitflic.ru")

    cookie_1 = {
        "name": "SESSION",
        "value": "11111111-1111-1111-1111-111111111111",
        "domain": "gitflic.ru"
    }
    driver.add_cookie(cookie_1)
    driver.refresh()

    driver.get("https://gitflic.ruprofile?user=1")
    user1_url = driver.current_url

    driver.delete_all_cookies()

    driver.get("https://gitflic.ru")

    cookie_2 = {
        "name": "SESSION",
        "value": "22222222-2222-2222-2222-222222222222",
        "domain": "gitflic.ru"
    }
    driver.add_cookie(cookie_2)
    driver.refresh()

    driver.get("https://gitflic.ruprofile?user=2")
    user2_url = driver.current_url

    assert user1_url != user2_url, f"Ошибка: URL совпадает ({user1_url})"

    driver.quit()
