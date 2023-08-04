#На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
#Напишите 3-7 тестов pytest для данного проекта.
#Используйте фикстуры.

import json
import pytest
from STask4 import Project
from STask3 import User
from Exceptions import NotAllowedError, AdminNotFoundError, LevelError

@pytest.fixture
def get_file(tmp_path):
    f_name = tmp_path / 'test_file.json'
    with open(f_name, 'w', encoding='utf-8') as f:
        data = {
            "1": {"21": "Петрова", },
            "2": {"334": "Сидорова", },
            "3": {"732": "Данченко", },
            "5": {"999": "Григорьев", }}

        json.dump(data, f, ensure_ascii=True)
    return f_name


@pytest.fixture
def fill_users(get_file):
    proj = Project().fill_project_users(get_file)
    return proj

def test_fill_users(get_file, fill_users):
    p = Project().fill_project_users(get_file)
    assert fill_users == p


@pytest.mark.parametrize("name, u_id, result", [("Данченко", 732, User("Данченко", 732)),
                        ("Иванова", 456, "Доступ закрыт!\nПользователь Иванов/777 не найден."),
                        ("Петрова", 21, User("Петрова", 21)), ])
def test_enter(name, u_id, result, fill_users):
    if isinstance(result, User):
        fill_users.enter(name, u_id)
        assert fill_users.admin == result
    else:
        with pytest.raises(NotAllowedError) as exc_info:
            fill_users.enter(name, u_id)
        assert str(exc_info.value) == result

@pytest.mark.parametrize("name, u_id, level, result, exc",[("Иванов", 34, 6, User("Иванов", 34, 6), None),
                        ("Иванов", 34, 6, "Доступ закрыт!\nАдминистратор не найден!", AdminNotFoundError),
                        ("Иванов", 34, 2, "Доступ закрыт!\nВаш уровень доступа(2) должен быть ниже уровеня доступа администратора(5)",
                        LevelError), ])
def test_add_user(name, u_id, level, result, exc, fill_users):
    if exc is None:
        fill_users.enter("Григорьев", 999)
        fill_users.add_user(name, u_id, level)
        assert result in fill_users.project_users
    elif exc == AdminNotFoundError:
        with pytest.raises(AdminNotFoundError) as exc_info:
            fill_users.add_user(name, u_id, level)
        assert str(exc_info.value) == result
    elif exc == LevelError:
        with pytest.raises(LevelError) as exc_info:
            fill_users.enter("Григорьев", 999)
            fill_users.add_user(name, u_id, level)
        assert str(exc_info.value) == result

@pytest.mark.parametrize("first_user, second_user, exp", [(User("Иванов", 34), User("Иванов", 34), True),
                                                          (User("Суворов", 278), User("Иванов", 34), False), ])
def test_users(first_user, second_user, exp):
    assert (first_user == second_user) == exp


if __name__ == "__main__":
    pytest.main(["-v"])