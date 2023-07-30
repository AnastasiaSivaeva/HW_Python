#Создайте класс Матрица. Добавьте методы для: вывода на печать, сравнения, сложения

class Matrix:

    def __init__(self, element):
        self.element = element

    def get_matrix(self):
        return self.element

    def __add__(self, other):
        if len(self.element) != len(other.element) or len(self.element[0]) != len(other.element[0]):
            return f'Ошибка: матрицы разных размеров'
        else:
            return Matrix([[self.element[i][j] + other.element[i][j] for j in range(len(self.element[0]))] \
                           for i in range(len(self.element))])
    def __eq__(self, other):
        if len(self.element) != len(other.element) or len(self.element[0]) != len(other.element[0]):
            return f'Ошибка: матрицы разных размеров'
        else:
            for i in range(len(self.element)):
                for j in range(len(self.element[0])):
                    if self.element[i][j] != other.element[i][j]:
                        return False
            return True

    def __str__(self):
        s = ''
        for i in range(len(self.element)):
            s += str(self.element[i]) + '\n'
        return s
    
matrix_1 = [[1, 2, 4],
            [5, 6, 8],
            [2, 5, -2],
            [10, 5, 0]]

matrix_2 = [[1, 2, 4],
            [5, 6, 8],
            [2, 5, -2],
            [0, 5, 0]]

matrix_3 = [[1, 2, 4, 5],
            [5, 6, 8, 0],
            [5, 0, -7, 1]]

matrix_4 = [[1, 2, 4, 5, 0],
            [5, 6, 8, 0, 0],
            [5, 0, -7, 1, 0]]

matrix_1 = Matrix(matrix_1)
matrix_2 = Matrix(matrix_2)
matrix_3 = Matrix(matrix_3)
matrix_4 = Matrix(matrix_4)

print("Cложение матриц:")
matrix_sum = matrix_1 + matrix_2
print(matrix_sum)


print("Cравнение матриц:")
print(matrix_1 == matrix_2)