#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и 
#знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки 
#своего кода используйте модуль fractions.

import fractions

a1, b1 = map(int, input('Введите первую дробь вида а/b: ').split('/'))
a2, b2 = map(int, input('Введите вторую дробь вида а/b: ').split('/'))

#Сумма

numerator = (b2 * a1) + (b1 * a2)
denominator = b1 * b2
print('Сумма равна {}/{}'.format(numerator , denominator))

f1 = fractions.Fraction(a1, b1)
f2 = fractions.Fraction(a2, b2)
print(f1 + f2)

#Произведение

numerator = a1 * a2
denominator = b1 * b2
print('Произведение равно {}/{}'.format(numerator, denominator))

f1 = fractions.Fraction(a1, b1)
f2 = fractions.Fraction(a2, b2)
print(f1 * f2)

