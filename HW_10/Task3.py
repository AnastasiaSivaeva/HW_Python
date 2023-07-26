#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
#В результирующем списке не должно быть дубликатов.

class Elements:
    def __int__(self):
        self.list = list

    def element(self):
        result = set()
        for i in list:
            spam = list.count(i)
            if spam > 1:
                result.add(i)
        return result

list = [1, 1, 2, 2, 2, 3, 3, 3, 4, 6, 6, 7]
print(Elements.element(list))