import os
import re
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='add noisy for images')
    parser.add_argument('-s', '--src', type=str, default='../dataset/a', help='source path')
    parser.add_argument('-d', '--dst', type=str, default='../dataset/a_noise', help='destination path')
    args = parser.parse_args()
    print(args.src)
    print(args.dst)

    if not os.path.exists(args.src):
        print('source path not exists')
        exit(0)
    if not os.path.exists(args.dst):
        os.mkdir(args.dst)

    fileList = os.listdir('d')
    #切换到当前工作目录
    os.chdir("d")
    num = 0
    print("start change name")
    #如果想保持原有文件顺序，可以尝试先读取fileName然后据此修改
    for fileName in fileList:
        os.rename(fileName,"d_"+str(num).zfill(4)+".jpg")
        num = num + 1
    print("complete")
