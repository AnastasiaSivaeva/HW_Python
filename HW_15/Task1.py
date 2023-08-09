#Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
#Соберите информацию о содержимом в виде объектов namedtuple.
#Каждый объект хранит:
#* имя файла без расширения или название каталога,
#* расширение, если это файл,
#* флаг каталога,
#* название родительского каталога.
#В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
from collections import namedtuple
import os
from pathlib import Path
import logging

param = r"C:\Users\Acer\Desktop\HW_Python\HW_15"

logging.basicConfig(filename='file.log',
                    encoding='utf-8',
                    format='{asctime} {levelname} - {msg}',
                    level=logging.INFO,
                    style='{')

logger = logging.getLogger()

PathElements = namedtuple("PathElements", ['name', 'extension', 'directory', 'parent_dir'])

parser = argparse.ArgumentParser()
parser.add_argument('-param', type=str)
args = parser.parse_args()
path = Path(args.param)

path_elements_list = []
file_list = os.listdir(path)

for elem in file_list:
    temp_path = path / elem
    name = temp_path.stem
    expansion = temp_path.suffix or 'каталог не имеет расширения'
    directory = temp_path.is_dir()
    parent_dir = temp_path.parent.stem
    logger.info(f"Имя файла/каталога: {name}, расширение: {expansion}, директория: {directory}, имя директории: {parent_dir}")
    path_elements_list.append(PathElements(name, expansion, directory, parent_dir))

print(*path_elements_list, sep='\n')

