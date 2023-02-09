from PIL import Image
from PIL import ImageStat
from PIL import ImageEnhance
import os


def get_image_light_mean(dst_src):
    im = dst_src.convert('L')
    stat = ImageStat.Stat(im)
    return stat.mean[0]


if __name__ == '__main__':
    imageDir = os.listdir('origin')
    maxNum = 0
    for image in imageDir:
        img = Image.open('origin/' + image)
        # print(get_image_light_mean(img))
        num = get_image_light_mean(img)
        if num > maxNum:
            maxNum = num
    print(maxNum)

