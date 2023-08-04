class OwnException(Exception):
    pass



class LevelError(OwnException):
    def __init__(self, user_level, admin_level):
        self.user_level = user_level
        self.admin_level = admin_level

    def __str__(self):
        return f"""Отказано в доступе!
Ваш уровень доступа({self.user_level}) должен быть ниже уровня доступа администратора({self.admin_level})"""
    
class NotAllowedError(OwnException):
    def __init__(self, name, id_):
        self.name = name
        self.id_ = id_

    def __str__(self):
        return f"""Отказано в доступе!
Пользователь {self.name}/{self.id_} не найден."""

class AdminNotFoundError(OwnException):
    def __str__(self):
        return """Отказано в доступе!
Администратор не найден!"""