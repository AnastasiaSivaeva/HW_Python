import json
import pickle
from pathlib import Path


def re_save_files(path, new_path):
    directory = Path(path)
    if not Path(directory / new_path).exists():
        Path(directory / new_path).mkdir()
    new = Path(directory / new_path)
    json_files = [i for i in directory.iterdir() if i.suffix == '.json']
    for file in json_files:
        with (
            open(file, 'r', encoding='utf-8') as j,
            open(new / f'{file.stem}.pickle', 'wb') as p
        ):
            json_file = json.load(j)
            pickle.dump(json_file, p)


re_save_files('./HW_8', 'pickles')