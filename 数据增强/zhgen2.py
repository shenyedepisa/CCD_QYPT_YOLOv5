from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw, ImageFont
import random
import os
import argparse
import zhrotate
from zhrotate import zrtt
import math

'''
zhgen2   尝试加入旋转功能！！！
'''
'''
张涵尝试修复 label框 偏移的问题  但是 当旋转角度 不同时可能要分情况讨论
为了简单起见，我们限制所需要讨论的情况，就是限制旋转的角度
'''

'''
张涵自己的密字生成，我们主要达到以下几个要点， 
1，当前的生成位置是固定的，我需要 随机的
解决 方案 ，设计一个随机算法， 产生一个长度为10的列表，其中是我们需要的坐标
2，当前的 lebal微调有什么用处？？ 我不要微调,经过测试
微调是必要的，十分诡异现象， 猜测可能是由于 字体导致的。

3. 能不能加入旋转，加入旋转之后，出现了 label框 巨大的偏移
4，字体颜色 能不能随机， 12种随机， 但是还是想 黑色的可能性大一些
'''

zhxx = []
zhyy = []
zhrr = []


def zhrandomrr():
    # 调用本方法，将会按某一规则 去填充 zhrr列表，随机产生旋转的度数
    for i in range(0, 10):
        zhrr.append(zhgetan(i))


def zhrandomxy():
    # 调用本方法 将会 随机产生  zhxx 和 zhyy  为这两个坐标
    # 列表产生随机的10个位置坐标
    for i in range(0, 10):
        x = 0.0
        y = 0
        z = 0
        y = random.randint(30, 70)
        z = random.randint(30, 70)
        x = y / 100
        zhxx.append(x)
        x = z / 100
        zhyy.append(x)


def zhrandomcolor():
    # 调用此方法 获得随机的颜色， 返回值是  字符串
    x = random.randint(1, 20)
    if x == 1:
        return 'red'
    if x == 2:
        return 'black'
    if x == 3:
        return 'blue'
    if x == 4:
        return 'green'
    if x == 5:
        return 'purple'
    if x == 6:
        return 'yellow'
    if x == 7:
        return 'gray'
    if x == 8:
        return 'orange'
    if x == 9:
        return 'pink'
    if x == 10:
        return 'cyan'
    if x == 11:
        return 'olive'
    if x == 12:
        return 'brown'
    if x == 13:
        return 'black'
    if x == 14:
        return 'black'
    if x == 15:
        return 'black'
    if x == 16:
        return 'black'
    if x == 17:
        return 'black'
    if x == 18:
        return 'black'
    if x == 19:
        return 'black'
    if x == 20:
        return 'black'


def zhgetan00():
    # 限制 逆时针旋转的角度 只能在 0~90度之间
    x = random.randint(1, 89)
    return x


def zhgetan01():
    # get angle
    x = random.randint(271, 359)
    return x


def zhgetan(i):
    if i <= 3:
        return 0
    if i > 3 and i <= 6:
        return zhgetan00()
    if i >= 7:
        return zhgetan01()


def zhgetsize(i):
    if i == 0:
        return 50
    if i == 1:
        return 60
    if i == 2:
        return 70
    if i == 3:
        return 80
    if i == 4:
        return 90
    if i == 5:
        return 50
    if i == 6:
        return 60
    if i == 7:
        return 70
    if i == 8:
        return 80
    if i == 9:
        return 90


if __name__ == '__main__':

    # python的 参数方法，  description 说明
    parser = argparse.ArgumentParser(description='add mi for images')
    parser.add_argument('-s', '--src', type=str, default='./data-non/images', help='source path')
    parser.add_argument('-d', '--dst', type=str, default='./data-non/images_gc1', help='destination path')
    args = parser.parse_args()
    print(args.src)
    print(args.dst)

    if not os.path.exists(args.src):
        print('source path not exists')
        exit(0)
    if not os.path.exists(args.dst):
        os.mkdir(args.dst)

    fileList = os.listdir(args.src)
    fileList.sort()
    for fileName in fileList:
        img_name = os.path.join(args.src, fileName)
        im = Image.open(img_name)
        print(img_name, im.size[0], im.size[1])
        im = im.convert('RGB')

        im1 = (Image.open(img_name)).convert('RGB')
        im2 = (Image.open(img_name)).convert('RGB')
        im3 = (Image.open(img_name)).convert('RGB')
        im4 = (Image.open(img_name)).convert('RGB')
        im5 = (Image.open(img_name)).convert('RGB')
        im6 = (Image.open(img_name)).convert('RGB')
        im7 = (Image.open(img_name)).convert('RGB')
        im8 = (Image.open(img_name)).convert('RGB')
        im9 = (Image.open(img_name)).convert('RGB')
        im10 = (Image.open(img_name)).convert('RGB')

        draw1 = ImageDraw.Draw(im1)
        draw2 = ImageDraw.Draw(im2)
        draw3 = ImageDraw.Draw(im3)
        draw4 = ImageDraw.Draw(im4)
        draw5 = ImageDraw.Draw(im5)
        draw6 = ImageDraw.Draw(im6)
        draw7 = ImageDraw.Draw(im7)
        draw8 = ImageDraw.Draw(im8)
        draw9 = ImageDraw.Draw(im9)
        draw10 = ImageDraw.Draw(im10)

        # 两种写法：密，宻
        # 字体任选10种
        # 字体大小50，60，70，80，90
        # 字体颜色红，黑
        # 字体位置(100,100)~(500,500)
        # 字体倾斜角度？

        fnt1 = ImageFont.truetype(r'./fonts/chinese.stxingka.ttf', 50)
        fnt2 = ImageFont.truetype(r'./fonts/simkai.ttf', 60)
        fnt3 = ImageFont.truetype(r'./fonts/chinese.sthupo.ttf', 70)
        fnt4 = ImageFont.truetype(r'./fonts/chinese.simli.ttf', 80)
        fnt5 = ImageFont.truetype(r'./fonts/chinese.fzstk.ttf', 90)
        fnt6 = ImageFont.truetype(r'./fonts/chinese.stxingka.ttf', 50)
        fnt7 = ImageFont.truetype(r'./fonts/chinese.stxihei.ttf', 60)
        fnt8 = ImageFont.truetype(r'./fonts/chinese.stcaiyun.ttf', 70)
        fnt9 = ImageFont.truetype(r'./fonts/chinese.fzytk.ttf', 80)
        fnt10 = ImageFont.truetype(r'./fonts/simkai.ttf', 90)

        # zh
        zhxx.clear()
        zhyy.clear()
        zhrr.clear()
        zhrandomxy()
        zhrandomrr()

        # draw1.text((zhxx[0]*im.size[0], zhyy[0]*im.size[1]), u'密',fill=zhrandomcolor(), font=fnt1)
        # draw2.text((zhxx[1]*im.size[0], zhyy[1]*im.size[1]), u'密',fill=zhrandomcolor(), font=fnt2)
        # draw3.text((zhxx[2]*im.size[0], zhyy[2]*im.size[1]), u'密',fill=zhrandomcolor(), font=fnt3)
        # draw4.text((zhxx[3]*im.size[0], zhyy[3]*im.size[1]), u'密',fill=zhrandomcolor(), font=fnt4)
        # draw5.text((zhxx[4]*im.size[0], zhyy[4]*im.size[1]), u'密',fill=zhrandomcolor(), font=fnt5)
        # draw6.text((zhxx[5]*im.size[0], zhyy[5]*im.size[1]), u'密',fill=zhrandomcolor(), font=fnt6)
        # draw7.text((zhxx[6]*im.size[0], zhyy[6]*im.size[1]), u'密',fill=zhrandomcolor(), font=fnt7)
        # draw8.text((zhxx[7]*im.size[0], zhyy[7]*im.size[1]), u'密',fill=zhrandomcolor(), font=fnt8)
        # draw9.text((zhxx[8]*im.size[0], zhyy[8]*im.size[1]), u'密',fill=zhrandomcolor(), font=fnt9)
        # draw10.text((zhxx[9]*im.size[0], zhyy[9]*im.size[1]), u'密',fill=zhrandomcolor(), font=fnt10)
        '''
        使用zrtt函数 来代替原来的 text函数，可以生成带有旋转效果的密字
        zrtt 参数解析， 第一个参数 底图（被贴上密字的底图）
        第二个参数是 控制旋转度数
        第3个参参数 是 控制 xy 左上角位置坐标
        第4个参数是 fill 控制填充颜色
        第5个参数是 font 控制字体
        '''
        zrtt(im1, zhrr[0], (zhxx[0] * im.size[0], zhyy[0] * im.size[1]), zhrandomcolor(), fnt1)
        zrtt(im2, zhrr[1], (zhxx[1] * im.size[0], zhyy[1] * im.size[1]), zhrandomcolor(), fnt2)
        zrtt(im3, zhrr[2], (zhxx[2] * im.size[0], zhyy[2] * im.size[1]), zhrandomcolor(), fnt3)
        zrtt(im4, zhrr[3], (zhxx[3] * im.size[0], zhyy[3] * im.size[1]), zhrandomcolor(), fnt4)
        zrtt(im5, zhrr[4], (zhxx[4] * im.size[0], zhyy[4] * im.size[1]), zhrandomcolor(), fnt5)
        zrtt(im6, zhrr[5], (zhxx[5] * im.size[0], zhyy[5] * im.size[1]), zhrandomcolor(), fnt6)
        zrtt(im7, zhrr[6], (zhxx[6] * im.size[0], zhyy[6] * im.size[1]), zhrandomcolor(), fnt7)
        zrtt(im8, zhrr[7], (zhxx[7] * im.size[0], zhyy[7] * im.size[1]), zhrandomcolor(), fnt8)
        zrtt(im9, zhrr[8], (zhxx[8] * im.size[0], zhyy[8] * im.size[1]), zhrandomcolor(), fnt9)
        zrtt(im10, zhrr[9], (zhxx[9] * im.size[0], zhyy[9] * im.size[1]), zhrandomcolor(), fnt10)

        # im1.show()
        print(img_name.replace(args.src, args.dst))
        im1.save(img_name.replace(args.src, args.dst).replace('.jpg', '_0.jpg'))
        im2.save(img_name.replace(args.src, args.dst).replace('.jpg', '_1.jpg'))
        im3.save(img_name.replace(args.src, args.dst).replace('.jpg', '_2.jpg'))
        im4.save(img_name.replace(args.src, args.dst).replace('.jpg', '_3.jpg'))
        im5.save(img_name.replace(args.src, args.dst).replace('.jpg', '_4.jpg'))
        im6.save(img_name.replace(args.src, args.dst).replace('.jpg', '_5.jpg'))
        im7.save(img_name.replace(args.src, args.dst).replace('.jpg', '_6.jpg'))
        im8.save(img_name.replace(args.src, args.dst).replace('.jpg', '_7.jpg'))
        im9.save(img_name.replace(args.src, args.dst).replace('.jpg', '_8.jpg'))
        im10.save(img_name.replace(args.src, args.dst).replace('.jpg', '_9.jpg'))

        label_path = (args.src).replace('images', 'labels_gc1')
        label = img_name.replace('images', 'labels_gc1')
        if not os.path.exists(label_path):
            os.mkdir(label_path)
        file1 = open(label.replace('.jpg', '_0.txt'), 'w')
        file2 = open(label.replace('.jpg', '_1.txt'), 'w')
        file3 = open(label.replace('.jpg', '_2.txt'), 'w')
        file4 = open(label.replace('.jpg', '_3.txt'), 'w')
        file5 = open(label.replace('.jpg', '_4.txt'), 'w')
        file6 = open(label.replace('.jpg', '_5.txt'), 'w')
        file7 = open(label.replace('.jpg', '_6.txt'), 'w')
        file8 = open(label.replace('.jpg', '_7.txt'), 'w')
        file9 = open(label.replace('.jpg', '_8.txt'), 'w')
        file10 = open(label.replace('.jpg', '_9.txt'), 'w')

        '''
        张涵尝试修复 加入旋转功能之后  GT框 偏差的问题，
        思路，只能在 zhgen中做修改，因为需要用到 字的边长
        '''
        for i in range(0, 10):

            if zhrr[i] >= 1 and zhrr[i] <= 89:
                zhyy[i] = (zhyy[i] * im.size[1] - zhgetsize(i) * math.sin(zhrr[i] / 180 * math.pi)) / im.size[1]
            if zhrr[i] >= 15 and zhrr[i] <= 75:
                zhxx[i] = (zhxx[i] * im.size[0] + zhgetsize(i) / 3.5) / im.size[0]
                zhyy[i] = (zhyy[i] * im.size[1] + zhgetsize(i) / 3.5) / im.size[1]
            if zhrr[i] >= 270 and zhrr[i] <= 360:
                zhxx[i] = (zhxx[i] * im.size[0] - zhgetsize(i) * math.cos((90 - (360 - zhrr[i])) / 180 * math.pi)) / \
                          im.size[0]
            if zhrr[i] >= 285 and zhrr[i] <= 355:
                zhxx[i] = (zhxx[i] * im.size[0] + zhgetsize(i) / 4.2) / im.size[0]
                zhyy[i] = (zhyy[i] * im.size[1] + zhgetsize(i) / 4.2) / im.size[1]
            if zhrr[i] >= 340 and zhrr[i] <= 359:
                zhxx[i] = (zhxx[i] * im.size[0] - zhgetsize(i) / 5) / im.size[0]
                zhyy[i] = (zhyy[i] * im.size[1] + zhgetsize(i) / 5) / im.size[1]

        centerx1 = (zhxx[0] * im.size[0] + 50 / 2) / im.size[0]
        centerx2 = (zhxx[1] * im.size[0] + 60 / 2) / im.size[0]
        centerx3 = (zhxx[2] * im.size[0] + 70 / 2) / im.size[0]
        centerx4 = (zhxx[3] * im.size[0] + 80 / 2) / im.size[0]
        centerx5 = (zhxx[4] * im.size[0] + 90 / 2) / im.size[0]
        centerx6 = (zhxx[5] * im.size[0] + 50 / 2) / im.size[0]
        centerx7 = (zhxx[6] * im.size[0] + 60 / 2) / im.size[0]
        centerx8 = (zhxx[7] * im.size[0] + 70 / 2) / im.size[0]
        centerx9 = (zhxx[8] * im.size[0] + 80 / 2) / im.size[0]
        centerx10 = (zhxx[9] * im.size[0] + 90 / 2) / im.size[0]

        centery1 = (zhyy[0] * im.size[1] + 50 / 2) / im.size[1]
        centery2 = (zhyy[1] * im.size[1] + 60 / 2) / im.size[1]
        centery3 = (zhyy[2] * im.size[1] + 70 / 2) / im.size[1]
        centery4 = (zhyy[3] * im.size[1] + 80 / 2) / im.size[1]
        centery5 = (zhyy[4] * im.size[1] + 90 / 2) / im.size[1]
        centery6 = (zhyy[5] * im.size[1] + 50 / 2) / im.size[1]
        centery7 = (zhyy[6] * im.size[1] + 90 / 2) / im.size[1]  # 有微调改动
        centery8 = (zhyy[7] * im.size[1] + 70 / 2) / im.size[1]
        centery9 = (zhyy[8] * im.size[1] + 100 / 2) / im.size[1]  # 有微调改动
        centery10 = (zhyy[9] * im.size[1] + 90 / 2) / im.size[1]

        width1 = 50 / im.size[0]
        width2 = 60 / im.size[0]
        width3 = 70 / im.size[0]
        width4 = 80 / im.size[0]
        width5 = (90 * math.cos((90 - zhrr[4]) / 180 * math.pi) + 90 * math.sin((90 - zhrr[4]) / 180 * math.pi)) / \
                 im.size[0]
        width6 = (50 * math.cos((90 - zhrr[5]) / 180 * math.pi) + 50 * math.sin((90 - zhrr[5]) / 180 * math.pi)) / \
                 im.size[0]
        width7 = (60 * math.cos((90 - zhrr[6]) / 180 * math.pi) + 60 * math.sin((90 - zhrr[6]) / 180 * math.pi)) / \
                 im.size[0]
        width8 = (70 * math.cos((360 - zhrr[7]) / 180 * math.pi) + 70 * math.sin((360 - zhrr[7]) / 180 * math.pi)) / \
                 im.size[0]
        width9 = (80 * math.cos((360 - zhrr[8]) / 180 * math.pi) + 80 * math.sin((360 - zhrr[8]) / 180 * math.pi)) / \
                 im.size[0]
        width10 = (90 * math.cos((360 - zhrr[9]) / 180 * math.pi) + 90 * math.sin((360 - zhrr[9]) / 180 * math.pi)) / \
                  im.size[0]

        height1 = 50 / im.size[1]
        height2 = 60 / im.size[1]
        height3 = 70 / im.size[1]
        height4 = 80 / im.size[1]
        height5 = (90 * math.cos((90 - zhrr[4]) / 180 * math.pi) + 90 * math.sin((90 - zhrr[4]) / 180 * math.pi)) / \
                  im.size[1]
        height6 = (50 * math.cos((90 - zhrr[5]) / 180 * math.pi) + 50 * math.sin((90 - zhrr[5]) / 180 * math.pi)) / \
                  im.size[1]
        height7 = (60 * math.cos((90 - zhrr[6]) / 180 * math.pi) + 60 * math.sin((90 - zhrr[6]) / 180 * math.pi)) / \
                  im.size[1]
        height8 = (70 * math.cos((360 - zhrr[7]) / 180 * math.pi) + 70 * math.sin((360 - zhrr[7]) / 180 * math.pi)) / \
                  im.size[1]
        height9 = (80 * math.cos((360 - zhrr[8]) / 180 * math.pi) + 80 * math.sin((360 - zhrr[8]) / 180 * math.pi)) / \
                  im.size[1]
        height10 = (90 * math.cos((360 - zhrr[9]) / 180 * math.pi) + 90 * math.sin((360 - zhrr[9]) / 180 * math.pi)) / \
                   im.size[1]

        file1.write('0 ' + str(centerx1) + ' ' + str(centery1) + ' ' + str(width1) + ' ' + str(height1) + '\n')
        file2.write('0 ' + str(centerx2) + ' ' + str(centery2) + ' ' + str(width2) + ' ' + str(height2) + '\n')
        file3.write('0 ' + str(centerx3) + ' ' + str(centery3) + ' ' + str(width3) + ' ' + str(height3) + '\n')
        file4.write('0 ' + str(centerx4) + ' ' + str(centery4) + ' ' + str(width4) + ' ' + str(height4) + '\n')
        file5.write('0 ' + str(centerx5) + ' ' + str(centery5) + ' ' + str(width5) + ' ' + str(height5) + '\n')
        file6.write('0 ' + str(centerx6) + ' ' + str(centery6) + ' ' + str(width6) + ' ' + str(height6) + '\n')
        file7.write('0 ' + str(centerx7) + ' ' + str(centery7) + ' ' + str(width7) + ' ' + str(height7) + '\n')
        file8.write('0 ' + str(centerx8) + ' ' + str(centery8) + ' ' + str(width8) + ' ' + str(height8) + '\n')
        file9.write('0 ' + str(centerx9) + ' ' + str(centery9) + ' ' + str(width9) + ' ' + str(height9) + '\n')
        file10.write('0 ' + str(centerx10) + ' ' + str(centery10) + ' ' + str(width10) + ' ' + str(height10) + '\n')

    print("complete")
