#Задание №3
#Создайте класс с базовым исключением и дочерние классы исключения: ошибка уровня, ошибка доступа

from dataclasses import dataclass


@dataclass
class User:
    """
    Класс пользователя.
    """
    name: str
    u_id: int
    level: int = None

    def __eq__(self, other):
        """
        Сравнение пользователей
        """
        return self.u_id == other.u_id and self.name == other.name


if __name__ == "__main__":
    e1 = User('Иванов', 5, 6)
    e2 = User('Петров', 3, 6)
    print(e1.level > e2.level)