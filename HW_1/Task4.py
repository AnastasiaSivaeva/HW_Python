#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.

from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 10

while count != 0:
    NUMBER = int(input('Введите число от 1 до 1000: '))
    if NUMBER == num:
        print('Вы угадали число')
        break
    if NUMBER < num:
        print('Загаданное число больше ', NUMBER)
    else:
        print('Загаданное число меньше ', NUMBER)
    print(f'Осталось {count} попыток')
    count -= 1

