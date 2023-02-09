from PIL import Image
from PIL import ImageStat
from PIL import ImageEnhance
import os


def get_image_light_mean(dst_src):
    im = dst_src.convert('L')
    stat = ImageStat.Stat(im)
    return stat.mean[0]


# # 色度增强
def color(img):
    img = ImageEnhance.Color(img)
    colors = 1.5
    img = img.enhance(colors)
    # print('对比度', get_image_light_mean(img))
    return img


# 增强对比度
def contrast(img):
    img = ImageEnhance.Contrast(img)
    contrasts = 1.5
    img = img.enhance(contrasts)
    # print('对比度', get_image_light_mean(img))
    return img


# 亮度
def bright(img):
    brightness = 1 + ((255 - get_image_light_mean(img)) / 318)  # 1 - 1.5
    img = ImageEnhance.Brightness(img)
    img = img.enhance(brightness)
    # print('亮度', get_image_light_mean(img))
    return img


# 锐化
def sharp(img):
    sharpness = 1.5
    img = ImageEnhance.Sharpness(img)
    img = img.enhance(sharpness)
    # print('锐化', get_image_light_mean(img))
    return img


if __name__ == '__main__':
    imageDir = os.listdir('images')
    for img in imageDir:
        image = Image.open('images/' + img)
        # image.show()
        # print(get_image_light_mean(image))
        image = color(image)
        image = contrast(image)

        # image = bright(image)
        # image = sharp(image)

        # image = contrast(image)
        # image = color(image)
        # image = image.convert('L')
        # image.show()
        image.save('new/' + img)
