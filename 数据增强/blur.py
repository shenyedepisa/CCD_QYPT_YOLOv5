from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw , ImageFont
import random
import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='add blur for images')
    parser.add_argument('-s', '--src', type=str, default='../dataset/a', help='source path')
    parser.add_argument('-d', '--dst', type=str, default='../dataset/a_blur', help='destination path')
    args = parser.parse_args()
    print(args.src)
    print(args.dst)
    
    if not os.path.exists(args.src):
        print('source path not exists')
        exit(0)
    if not os.path.exists(args.dst):
        os.mkdir(args.dst)
    
    fileList = os.listdir(args.src)
    for fileName in fileList:
        img_name = os.path.join(args.src, fileName)
        im = Image.open(img_name)
        im = im.convert('RGB')
        im.filter(ImageFilter.BLUR).save(img_name.replace(args.src,args.dst))
        print(img_name)
