#Выведите в консоль таблицу умножения

NUM_X1 = 2
NUM_X2 = 11
NUM_Y1 = 2
NUM_Y2 = 6
NUM_Y3 = 10

for i in range(NUM_X1, NUM_X2):
    for k in range(NUM_Y1, NUM_Y2):
        print(f'{k} * {i} = {k * i}\t', end='       ')
    print('   ')
print(' ')

for i in range(NUM_X1, NUM_X2):
    for k in range(NUM_Y2, NUM_Y3):
        print(f'{k} * {i} = {k * i}\t', end='       ')
    print('   ')
print(' ')