#Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. 
#Для тестированию возьмите pickle версию файла из предыдущей задачи. Функция должна извлекать ключи словаря 
#для заголовков столбца из переданного файла.

import pickle
import pandas

with open("Task5.pickle", "rb") as f:
    object1 = pickle.load(f)
df = pandas.DataFrame(object1)
df.to_csv(r'file.csv')