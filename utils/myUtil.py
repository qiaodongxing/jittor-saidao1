import pathlib
import numpy as np
import json
def shuffle_list(train_list):
    # train_list is a list
    file_count = len(train_list)
    rnd_index = np.arange(file_count)
    np.random.shuffle(rnd_index)
    train_list = np.array(train_list)[rnd_index]
    return train_list

def get_all_paths(root_dir, ext='png', shuffle=False):
    root_dir = pathlib.Path(root_dir)
    file_paths = list(map(str, root_dir.rglob('*.' + ext)))
    file_paths.sort()
    if shuffle:
        file_paths = shuffle_list(file_paths)

    return file_paths

def compare2Folder_FileName(path1,path2):
    files1 = get_all_paths(path1, ext='*')
    files2 = get_all_paths(path2, ext='*')
    files1 = set(map(lambda x: x.split('/')[-1].split('.')[0], files1))
    files2 = set(map(lambda x: x.split('/')[-1].split('.')[0], files2))
    assert len(files1)==len(files2) and len(files1)!=0
    return files1.issubset(files2) and files2.issubset(files1)

def save_json(save_path, data):
    assert save_path.split('.')[-1] == 'json'
    with open(save_path, 'w') as file:
        json.dump(data, file)

def load_json(file_path):
    assert file_path.split('.')[-1] == 'json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
