#Напишите функцию группового переименования файлов. Она должна:
#* принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
#* принимать параметр количество цифр в порядковом номере.
#* принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
#* принимать параметр расширение конечного файла.


import os
from pathlib import Path


def group_rename(count_len: int, extension: str, new_extension: str, interval: list[int], new_name=''):
    count = 0
    for file in os.listdir():
        if file.endswith(extension):
            count += 1
            Path(file).rename(f"{file.split('.')[0][interval[0]:interval[1]]}{new_name}{count:0>{count_len}}.\
{new_extension}")


group_rename(3, 'zip', 'avi', [0, 2], "PICK")