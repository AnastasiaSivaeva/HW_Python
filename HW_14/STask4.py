# Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта. 
#Класс имеет следующие методы:
# Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
# Метод входа в систему – требует указать имя и id пользователя.
# Далее метод создает пользователя и проверяет есть ли он в списке пользователей проекта.
# Если в списке его нет, то вызывается исключение доступа.
# Если пользователь присутствует в списке пользователей проекта, то пользователь,
# который входит получает его уровень доступа и становится администратором.
# Метод добавление пользователя в список пользователей.
# Если уровень пользователя меньше, чем уровень админа, вызывайте исключение уровня доступа.

import json
from Exceptions import NotAllowedError, AdminNotFoundError, LevelError
from STask3 import User

class Project:

    def __init__(self, project_users=None):
        self.project_users = project_users or []
        self.admin = None

    @classmethod
    def fill_project_users(cls):
        """Метод, заполняющий список из json файла"""
        with open("users.json", "r", encoding="utf-8") as j:
            file = json.load(j)
            temp = []
            for key in file:
                for user in file[key].items():
                    temp.append(User(user[1], int(user[0]), int(key)))
            return cls(temp)
        
    def enter(self, name, u_id):
        """
        Метод входа в систему.
        """
        user = User(name, u_id)
        for proj_user in self.project_users:
            if user == proj_user:
                print(f'Добро пожаловать администратор: {name}!')
                self.admin = proj_user
                break
        else:
            raise NotAllowedError(name, u_id)

    def add_user(self, name, u_id, level):
        """
        Метод добавления нового пользователя.
        """
        if self.admin is None:
            raise AdminNotFoundError
        if level > self.admin.level:
            raise LevelError(level, self.admin.level)
        print(f'Пользователь: {name}, с id {u_id} был добавлен в систему!')
        self.project_users.append(User(name, u_id, level))

    def enter(self, name, u_id):
        """
        Метод входа в систему.
        """
        user = User(name, u_id)
        for proj_user in self.project_users:
            if user == proj_user:
                print(f'Добро пожаловать администратор: {name}!')
                self.admin = proj_user
                break
        else:
            raise NotAllowedError(name, u_id)

    def add_user(self, name, u_id, level):
        """
        Метод добавления нового пользователя.
        """
        if self.admin is None:
            raise AdminNotFoundError
        if level > self.admin.level:
            raise LevelError(level, self.admin.level)
        print(f'Пользователь: {name}, с id {u_id} был добавлен в систему!')
        self.project_users.append(User(name, u_id, level))

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Метод выхода из контекстного менеджера
        Новый список пользователей сохраняется в new_users.json.
        """
        self.file = open(f'new_users.json', 'w', encoding='utf-8')
        temp = {k: {} for k in range(1, 8)}
        for user in self.project_users:
            temp[user.level].update({user.u_id: user.name})
        json.dump(temp, self.file, ensure_ascii=False)
        self.file.close()


with Project().fill_project_users() as p:
    print(p.project_users)
    p.enter("Иванов", 34)
    print(p.admin)
    p.add_user("111111", 34, 1)
    p.del_user("111111", 34, 1)