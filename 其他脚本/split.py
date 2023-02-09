import argparse
import random
import os
from shutil import copyfile
import shutil


def copy(src, dst, name):
    src_path = src + '/images/' + name
    dst_path = dst + '/images'
    src_path_jpg = src_path + '.jpg'
    shutil.copy(src_path_jpg, dst_path)
    src_path = src + '/labels/' + name
    dst_path = dst + '/labels'
    src_path_txt = src_path + '.txt'
    shutil.copy(src_path_txt, dst_path)
    with open(os.path.join(dst, 'list.txt'), 'a') as f:
        f.write(name + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='split the dataset')
    parser.add_argument('-s', '--src', type=str, default='../dataset/origin', help='source path')
    args = parser.parse_args()

    src = args.src
    train = os.path.join(src, '../train')
    if not os.path.exists(train):
        os.mkdir(train)
        os.mkdir(train + '/images')
        os.mkdir(train + '/labels')
    test = os.path.join(src, '../test')
    if not os.path.exists(test):
        os.mkdir(test)
        os.mkdir(test + '/images')
        os.mkdir(test + '/labels')
    val = os.path.join(src, '../val')
    if not os.path.exists(val):
        os.mkdir(val)
        os.mkdir(val + '/images')
        os.mkdir(val + '/labels')

    images = os.listdir(os.path.join(src, 'images'))
    n = len(images)
    n_test = n // 50
    n_val = n // 50
    # n_train = n - n_test - n_val
    n_train = n // 15

    for i in range(n):
        index = random.randint(0, len(images) - 1)
        name = images[index].replace('.jpg', '')
        if n_test > 0:
            copy(src, test, name)
            n_test -= 1
        elif n_train > 0:
            copy(src, train, name)
            n_train -= 1
        elif n_val > 0:
            copy(src, val, name)
            n_val -= 1
        images.pop(index)
