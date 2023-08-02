#Доработайте прошлую задачу 3 .Добавьте сравнение прямоугольников по площади. Должны работать 
#все шесть операций сравнения


class Rectangle:
    """ 
    Класс прямоугольник. Принимает длину и ширину при создании экземпляра
    """

    def __init__(self, side_a: int = 1, side_b: int | None = None):
        """
        init
        :param side_a:
        :param side_b:
        """
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    def get_perimeter(self):
        """
        Method for getting the perimeter of a rectangle
        :return:
        """
        return 2 * (self._side_a + self._side_b)


    def get_square(self):
        """
        Method for getting the square of a rectangle
        :return:
        """
        return self._side_a * self._side_b

    def __add__(self, other):
        return Rectangle(self._side_a + other._side_a, self._side_b + other._side_b)

    def __sub__(self, other):
        return Rectangle(abs(self._side_a - other._side_a), abs(self._side_b - other._side_b))
    
    def __lt__(self, other):  
        """
        Less comparison method
        :return:
        """                           
        return self.get_square() < other.get_square()

    def __eq__(self, other):        
        """
        comparison method equals
        :return:
        """                     
        return self.get_square() == other.get_square()

    def __le__(self, other):      
        """
        Comparison method less or equal
        :return:
        """                       
        return self.get_square() <= other.get_square()

    def __str__(self):
        """
        Human-readable representation
        :return:
        """ 
        return f"прямоугольник со сторонами: {self._side_a} {self._side_b} и периметром: {self.get_perimeter()}"


    def __repr__(self):
        return f"Rectangle(прямоугольник со сторонами: {self._side_a} {self._side_b} и периметром: {self.get_perimeter()})"
    
if __name__ == '__main__':
    rect1 = Rectangle(2, 3)
    rect2 = Rectangle(2, 3)
    rect3 = rect1 + rect2
    print(rect3)

    rect5 = Rectangle(2, 2)
    rect6 = Rectangle(3, 3)
    print(rect1 < rect2)
    print(rect1 > rect2)
    print(rect1 <= rect2)
    print(rect1 >= rect2)
    print(rect1 == rect2)
    print(rect1 != rect2)
    print(repr(rect3))