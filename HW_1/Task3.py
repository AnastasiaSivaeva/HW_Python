#   #Напишите код, который запрашивает число и сообщает является ли оно простым или составным.

NUM = int(input('Введите число от 1 до 100 000: '))
LOWER_LIMIT = 1
UPPER_LIMIT = 100000

if LOWER_LIMIT < NUM < UPPER_LIMIT:
    for i in range(2, int(NUM ** 0.5) + 1):
        if (NUM % i) == 0:
            print('Число составное')
            break
    else:
        print('Число простое')
else:
    print('Вы ввели число выходящее за рамки диапазона')
