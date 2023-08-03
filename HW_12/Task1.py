#Создайте класс студента.
#* Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
#* Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре 
#недопустимы.
#* Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
#* Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе 
#взятых.

import csv
from functools import reduce
from pathlib import Path

class Exam:
    '''
    Проверка на наличие в ФИО только букв и первой заглавной 
    '''

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.isalpha():
            raise TypeError(f'Вводимое значение {value} должно содержать только буквы')
        if not value.istitle():
            raise TypeError(f'Вводимое значение {value} должно начинаться с заглавной буквы')
        
class Student:
    name = Exam()
    second_name = Exam()
    surname = Exam()
    _lessons = None

    def __init__(self, surname: str, name: str, second_name: str, lessons_file: Path):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.lessons = lessons_file

    @property
    def lessons(self):
        return self._lessons
    
    @lessons.setter
    def lessons(self, lessons_file: Path):
        '''
        Считывается список предметов из файла
        '''

        self._lessons = {"lessons": {}}
        with open(lessons_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._lessons["lessons"][row[0]] = {"assessments": [], "test_results": [], "average_test": None}
        self._lessons["middle_assessment"] = None
        self._lessons["middle_test"] = None

    def __call__(self, lesson: str, number: int, type_est: str = "lesson"):
        '''
        Метод для сохранения новой оценки по предмету и тесту
        '''

        if lesson not in self.lessons["lessons"].keys():
            raise AttributeError("Такого предмета нет")
        if type_est == "lesson":
            if number < 2 or number > 5:
                raise ValueError("Оценка должна быть в диапазоне от 2 до 5")
            self.lessons["lessons"][lesson]["assessments"].append(number)
            self.lessons["middle_assessment"] = self.calculate_middle_estimate(self.lessons)
        elif type_est == "test":
            if number < 0 or number > 100:
                raise ValueError("Балл должен быть в диапазоне от 0 до 100")
            self.lessons["lessons"][lesson]["test_results"].append(number)

            self.lessons["lessons"][lesson]["average_test"] \
                = reduce(lambda x, y: x + y, self.lessons["lessons"][lesson]["test_results"]) \
                / len(self.lessons["lessons"][lesson]["test_results"])
            self.lessons['middle_test'] = self.calculate_middle_test(self.lessons)
    
    @staticmethod
    def calculate_middle_estimate(lessons: dict) -> float:
        '''
        Подсчет средней оценки по всем предметам
        '''

        all_estimates = []
        [all_estimates.extend(lessons["lessons"][name]["assessments"]) for name in lessons["lessons"]]
        result = reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)
        return round(result, 2)

    @staticmethod
    def calculate_middle_test(lessons: dict) -> float:
        '''
        Подсчет среднего бала по тестам по всем предметам
        '''

        all_estimates = []
        [all_estimates.extend(lessons["lessons"][name]["test_results"]) for name in lessons["lessons"]]
        result = reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)
        return round(result, 2)
    
    def __repr__(self):
        result = f'Студент {self.surname} {self.name} {self.second_name} \nСредняя оценка по всем предметам = {self.lessons["middle_assessment"]}\nСредний бал по всем тестам = {self.lessons["middle_test"]}\n'
        result += "\nОценки по предметам:\n"

        for key, value in self.lessons["lessons"].items():
            result += f'{key} = {value["assessments"]}\n'
        result += "\nТесты по предметам:\n"
        for key, value in self.lessons["lessons"].items():
            result += f'{key} = {value["test_results"]}, ср.бал = {value["average_test"]}\n'

        return result
    
if __name__ == '__main__':
    student_1 = Student("Иванов", "Александр", "Викторович", Path('lessons.csv'))
    student_1("русский язык", 5)
    student_1("русский язык", 4)
    student_1("история", 3)
    student_1("физика", 5)
    student_1("математика", 5)
    student_1("информатика", 33, "test")
    student_1("математика", 50, "test")
    student_1("химия", 55, "test")
    student_1("химия", 4)
    student_1("информатика", 4)
    student_1("информатика", 40, "test")
    print(student_1)
    
    student_2 = Student("Петров", "Иван", "Иванович",  Path('lessons.csv'))
    student_2("русский язык", 4)
    student_2("история", 5)
    student_2("физика", 3)
    student_2("математика", 5)
    student_2("история", 40, "test")
    student_2("история", 80, "test")
    student_2("физика", 99, "test")
    student_2("физика", 4)
    student_2("информатика", 5)
    student_2("информатика", 40, "test")
    student_2("история", 75, "test")
    print(student_2)




