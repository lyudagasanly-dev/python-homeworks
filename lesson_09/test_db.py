from sqlalchemy import create_engine, text

# Стандартное подключение к базе QA1
db_url = "postgresql://postgres:lvs@localhost:5432/QA1"
engine = create_engine(db_url)


def test_insert_teacher():
    """1. Тест на добавление учителя в базу данных."""
    test_email = "autotest_insert_teacher@skypro.ru"

    # engine.begin() принудительно сохраняет изменения на диск
    with engine.begin() as connection:
        # Добавляем строчку только с email
        query = text("INSERT INTO teacher (email) VALUES (:email);")
        connection.execute(query, {"email": test_email})

        # ПРОВЕРКА ПО EMAIL
        select_query = text(
            "SELECT COUNT(*) FROM teacher WHERE email = :email;"
        )
        result = connection.execute(select_query, {"email": test_email})
        count = result.scalar()

        assert count == 1, f"Учитель с почтой {test_email} не добавился в БД"

        # УБОРКА ПО EMAIL: удаляем созданный тестовый емейл
        delete_query = text("DELETE FROM teacher WHERE email = :email;")
        connection.execute(delete_query, {"email": test_email})


def test_update_teacher():
    """2. Тест на изменение данных учителя."""
    old_email = "old_teacher_email@skypro.ru"
    new_email = "new_changed_teacher_email@skypro.ru"

    with engine.begin() as connection:
        # 1. Создаем учителя со стартовой почтой
        insert_query = text("INSERT INTO teacher (email) VALUES (:email);")
        connection.execute(insert_query, {"email": old_email})

        # 2. Обновляем (UPDATE) старую почту на новую
        update_query = text(
            "UPDATE teacher SET email = :new_email WHERE email = :old_email;"
        )
        connection.execute(
            update_query, {"new_email": new_email, "old_email": old_email}
        )

        # 3. Проверяем, что новая почта есть, а старой больше нет
        select_new = text("SELECT COUNT(*) FROM teacher WHERE email = :email;")
        count_new = connection.execute(
            select_new, {"email": new_email}
        ).scalar()
        assert count_new == 1, "Новый email не записался в базу данных"

        select_old = text("SELECT COUNT(*) FROM teacher WHERE email = :email;")
        count_old = connection.execute(
            select_old, {"email": old_email}
        ).scalar()
        assert count_old == 0, "Старый email всё ещё остался в базе данных"

        # УБОРКА ПО EMAIL
        delete_query = text("DELETE FROM teacher WHERE email = :email;")
        connection.execute(delete_query, {"email": new_email})


def test_delete_teacher():
    """3. Тест на удаление учителя из базы данных."""
    delete_email = "teacher_to_delete@skypro.ru"

    with engine.begin() as connection:
        # 1. Создаем учителя, которого будем удалять
        insert_query = text("INSERT INTO teacher (email) VALUES (:email);")
        connection.execute(insert_query, {"email": delete_email})

        # 2. Удаляем его (DELETE) напрямую по email
        delete_query = text("DELETE FROM teacher WHERE email = :email;")
        connection.execute(delete_query, {"email": delete_email})

        # 3. Проверяем, что строчка полностью исчезла (COUNT == 0)
        select_query = text(
            "SELECT COUNT(*) FROM teacher WHERE email = :email;"
        )
        count = connection.execute(
            select_query, {"email": delete_email}
        ).scalar()
        assert count == 0, "Учитель не удалился из базы данных по email"
