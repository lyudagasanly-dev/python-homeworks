from selenium import webdriver
from FormPage import FormPage


def test_form_validation():
    # Настраиваем драйвер в тесте по правилам задания
    driver = webdriver.Edge()

    # Создаем объект нашей страницы
    form_page = FormPage(driver)

    # Выполняем понятные шаги сценария
    form_page.open_page()
    form_page.fill_form()
    form_page.click_submit()

    # Проверяем, что поле Zip code подсвечено красным (alert-danger)
    assert "alert-danger" in form_page.get_zip_code_class(), (
        "Поле Zip code не подсвечено красным!"
    )

    # Проверяем остальные поля на зеленый цвет (alert-success)
    green_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in green_fields:
        field_class = form_page.get_field_class_by_id(field_id)
        assert "alert-success" in field_class, (
            f"Поле {field_id} не подсвечено зеленым!"
        )

    # Закрываем драйвер в самом тесте
    driver.quit()
