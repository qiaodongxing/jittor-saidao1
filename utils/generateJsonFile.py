from myUtil import *

if __name__ == '__main__':
    path1 = '../../data/train_resized/imgs'
    path2 = '../../data/train_resized/labels'
    files1 = get_all_paths(path1, ext='*')
    files2 = get_all_paths(path2, ext='*')
    files1 = list(map(lambda x: x.split('/')[-1].split('.')[0], files1))
    files2 = list(map(lambda x: x.split('/')[-1].split('.')[0], files2))
    file_dict = {}
    for i,fileName in enumerate(files1):
        if fileName==files2[i]:
            file_dict[fileName+'.png']=fileName+'.jpg'

    save_json('./label_to_img.json',file_dict)
    print(file_dict.popitem())
    a=load_json('./label_to_img.json')
    print(a.popitem())







