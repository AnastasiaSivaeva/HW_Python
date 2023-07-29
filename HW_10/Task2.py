# Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали.
# Превратите функции в методы класса. Задачи должны решаться через вызов методов экземпляра.

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

class Elements:
    def __init__(self, elements):
        self.elements = elements

    def elements(**kwargs):
        result = {}
        for key, value in kwargs.items():
            result[str(value)] = key
        return result


print(Elements.elements(one='6', two=6.15, three='Hello', four=35))