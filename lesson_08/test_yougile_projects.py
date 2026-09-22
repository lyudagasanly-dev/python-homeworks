from YougileAPI import YougileAPI


def test_create_project_positive():
    """1. Позитивный тест: создание проекта."""
    api = YougileAPI()
    response = api.create_project("Авто-проект QA")
    assert response.status_code == 201, (
        f"Ожидали 201, получили {response.status_code}"
    )
    res_json = response.json()
    assert "id" in res_json, "В ответе сервера нет id!"


def test_create_project_negative_empty():
    """2. Негативный тест: создание проекта с пустым телом."""
    api = YougileAPI()
    response = api.create_project_negative({})
    assert response.status_code == 400, (
        f"Ожидали 400, получили {response.status_code}"
    )


def test_update_project_positive():
    """3. Позитивный тест: изменение названия проекта."""
    api = YougileAPI()

    # Сначала создаем проект, чтобы узнать его ID
    create_res = api.create_project("Проект для изменения")
    project_id = create_res.json()["id"]

    # Меняем название
    update_res = api.update_project(project_id, "Измененное название QA")
    assert update_res.status_code == 200, (
        f"Ожидали 200, получили {update_res.status_code}"
    )


def test_update_project_negative_fake_id():
    """4. Негативный тест: изменение несуществующего проекта."""
    api = YougileAPI()
    fake_id = "11111111-1111-1111-1111-111111111111"
    response = api.update_project(fake_id, "Новое имя")
    assert response.status_code == 404, (
        f"Ожидали 404, получили {response.status_code}"
    )


def test_get_project_positive():
    """5. Позитивный тест: получение проекта по ID."""
    api = YougileAPI()

    # Создаем проект для теста
    create_res = api.create_project("Проект для поиска")
    project_id = create_res.json()["id"]

    # Запрашиваем информацию
    get_res = api.get_project_by_id(project_id)
    assert get_res.status_code == 200, (
        f"Ожидали 200, получили {get_res.status_code}"
    )
    assert get_res.json()["title"] == "Проект для поиска"


def test_get_project_negative_fake_id():
    """6. Негативный тест: получение несуществующего проекта."""
    api = YougileAPI()
    fake_id = "11111111-1111-1111-1111-111111111111"
    response = api.get_project_by_id(fake_id)
    assert response.status_code == 404, (
        f"Ожидали 404, получили {response.status_code}"
    )
