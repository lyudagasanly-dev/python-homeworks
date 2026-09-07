import time
from selenium import webdriver

# Запускаем браузер Chrome через автоматический менеджер
driver = webdriver.Chrome()

# Открываем сайт Google
driver.get("https://google.com")

# Устанавливаем 5 секунд, чтобы успеть посмотреть глазами
time.sleep(5)

# Закрываем браузер после теста
driver.quit()
