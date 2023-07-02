#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное 
#строковое представление.Функцию hex используйте для проверки своего результата.

NUM = int(input('Введите целое число: '))

def transl(a: int, d: int) -> str:
    l = []
    while a > 0:
        a, f = divmod(a, d)
        l.append(str(f))
    return ''.join(l[::-1])

print(transl(NUM, 16))

h = hex(NUM)
print(h)
