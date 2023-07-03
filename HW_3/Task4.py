#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
#Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
#Достаточно вернуть один допустимый вариант.

hike = {'палатка': 5, 'котелок': 2, 'веревка': 4, 'еда': 3, 'одежда': 2, 'спальник': 3}

MAX_WEIGHT = 10
summ = MAX_WEIGHT
new_backpack = {}

for key, value in hike.items():
    if value <= summ:
        summ -= value
        new_backpack[key] = value

print(f"Вместится в рюкзак не больше {MAX_WEIGHT} кг - например: {new_backpack}")