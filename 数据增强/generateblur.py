from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw , ImageFont
import random
import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='add mi and blur for images')
    parser.add_argument('-s', '--src', type=str, default='./data-non/images', help='source path')
    parser.add_argument('-d', '--dst', type=str, default='./data-non/images_gb', help='destination path')
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

        fnt1 = ImageFont.truetype(r'./fonts/chinese.stxingka.ttf',50)
        fnt2 = ImageFont.truetype(r'./fonts/simkai.ttf',60)
        fnt3 = ImageFont.truetype(r'./fonts/chinese.sthupo.ttf',70)
        fnt4 = ImageFont.truetype(r'./fonts/chinese.simli.ttf',80)
        fnt5 = ImageFont.truetype(r'./fonts/chinese.fzstk.ttf',90)
        fnt6 = ImageFont.truetype(r'./fonts/chinese.stxingka.ttf',50)
        fnt7 = ImageFont.truetype(r'./fonts/chinese.stxihei.ttf',60)
        fnt8 = ImageFont.truetype(r'./fonts/chinese.stcaiyun.ttf',70)
        fnt9 = ImageFont.truetype(r'./fonts/chinese.fzytk.ttf',80)
        fnt10 = ImageFont.truetype(r'./fonts/chinese.stcaiyun.ttf',90)

        draw1.text((0.1*im.size[0], 0.1*im.size[1]), u'密', fill='red', font=fnt1)
        draw2.text((0.2*im.size[0], 0.1*im.size[1]), u'密', fill='black', font=fnt2)
        draw3.text((0.3*im.size[0], 0.1*im.size[1]), u'密', fill='yellow', font=fnt3)
        draw4.text((0.4*im.size[0], 0.1*im.size[1]), u'密', fill='red', font=fnt4)
        draw5.text((0.5*im.size[0], 0.1*im.size[1]), u'密', fill='black', font=fnt5)
        draw6.text((0.1*im.size[0], 0.2*im.size[1]), u'密', fill='red', font=fnt6)
        draw7.text((0.1*im.size[0], 0.3*im.size[1]), u'密', fill='black', font=fnt7)
        draw8.text((0.1*im.size[0], 0.4*im.size[1]), u'密', fill='yellow', font=fnt8)
        draw9.text((0.1*im.size[0], 0.5*im.size[1]), u'密', fill='red', font=fnt9)
        draw10.text((0.1*im.size[0], 0.6*im.size[1]), u'密', fill='black', font=fnt10)

        # im1.show()
        print(img_name.replace(args.src,args.dst))
        im1.filter(ImageFilter.GaussianBlur).save(img_name.replace(args.src,args.dst).replace('.jpg','_0.jpg'))
        im2.filter(ImageFilter.GaussianBlur).save(img_name.replace(args.src,args.dst).replace('.jpg','_1.jpg'))
        im3.filter(ImageFilter.GaussianBlur).save(img_name.replace(args.src,args.dst).replace('.jpg','_2.jpg'))
        im4.filter(ImageFilter.GaussianBlur).save(img_name.replace(args.src,args.dst).replace('.jpg','_3.jpg'))
        im5.filter(ImageFilter.GaussianBlur).save(img_name.replace(args.src,args.dst).replace('.jpg','_4.jpg'))
        im6.filter(ImageFilter.GaussianBlur).save(img_name.replace(args.src,args.dst).replace('.jpg','_5.jpg'))
        im7.filter(ImageFilter.GaussianBlur).save(img_name.replace(args.src,args.dst).replace('.jpg','_6.jpg'))
        im8.filter(ImageFilter.GaussianBlur).save(img_name.replace(args.src,args.dst).replace('.jpg','_7.jpg'))
        im9.filter(ImageFilter.GaussianBlur).save(img_name.replace(args.src,args.dst).replace('.jpg','_8.jpg'))
        im10.filter(ImageFilter.GaussianBlur).save(img_name.replace(args.src,args.dst).replace('.jpg','_9.jpg'))

        label_path = (args.src).replace('images','labels_gb')
        label = img_name.replace('images','labels_gb')
        if not os.path.exists(label_path):
            os.mkdir(label_path)
        file1 = open(label.replace('.jpg','_0.txt'), 'w')
        file2 = open(label.replace('.jpg','_1.txt'), 'w')
        file3 = open(label.replace('.jpg','_2.txt'), 'w')
        file4 = open(label.replace('.jpg','_3.txt'), 'w')
        file5 = open(label.replace('.jpg','_4.txt'), 'w')
        file6 = open(label.replace('.jpg','_5.txt'), 'w')
        file7 = open(label.replace('.jpg','_6.txt'), 'w')
        file8 = open(label.replace('.jpg','_7.txt'), 'w')
        file9 = open(label.replace('.jpg','_8.txt'), 'w')
        file10 = open(label.replace('.jpg','_9.txt'), 'w')

        centerx1 = (0.1*im.size[0]+50/2)/im.size[0]
        centerx2 = (0.2*im.size[0]+60/2)/im.size[0]
        centerx3 = (0.3*im.size[0]+70/2)/im.size[0]
        centerx4 = (0.4*im.size[0]+80/2)/im.size[0]
        centerx5 = (0.5*im.size[0]+90/2)/im.size[0]
        centerx6 = (0.1*im.size[0]+50/2)/im.size[0]
        centerx7 = (0.1*im.size[0]+60/2)/im.size[0]
        centerx8 = (0.1*im.size[0]+70/2)/im.size[0]
        centerx9 = (0.1*im.size[0]+80/2)/im.size[0]
        centerx10 = (0.1*im.size[0]+90/2)/im.size[0]

        centery1 = (0.1*im.size[1]+50/2)/im.size[1]
        centery2 = (0.1*im.size[1]+60/2)/im.size[1]
        centery3 = (0.1*im.size[1]+70/2)/im.size[1]
        centery4 = (0.1*im.size[1]+80/2)/im.size[1]
        centery5 = (0.1*im.size[1]+90/2)/im.size[1]
        centery6 = (0.2*im.size[1]+50/2)/im.size[1]
        centery7 = (0.3*im.size[1]+90/2)/im.size[1] # 有微调改动
        centery8 = (0.4*im.size[1]+70/2)/im.size[1]
        centery9 = (0.5*im.size[1]+100/2)/im.size[1] # 有微调改动
        centery10 = (0.6*im.size[1]+90/2)/im.size[1]

        width1 = 50/im.size[0]
        width2 = 60/im.size[0]
        width3 = 70/im.size[0]
        width4 = 80/im.size[0]
        width5 = 90/im.size[0]

        height1 = 50/im.size[1]
        height2 = 60/im.size[1]
        height3 = 70/im.size[1]
        height4 = 80/im.size[1]
        height5 = 90/im.size[1]

        file1.write('0 ' + str(centerx1) + ' ' + str(centery1) + ' ' + str(width1) + ' ' + str(height1) + '\n')
        file2.write('0 ' + str(centerx2) + ' ' + str(centery2) + ' ' + str(width2) + ' ' + str(height2) + '\n')
        file3.write('0 ' + str(centerx3) + ' ' + str(centery3) + ' ' + str(width3) + ' ' + str(height3) + '\n')
        file4.write('0 ' + str(centerx4) + ' ' + str(centery4) + ' ' + str(width4) + ' ' + str(height4) + '\n')
        file5.write('0 ' + str(centerx5) + ' ' + str(centery5) + ' ' + str(width5) + ' ' + str(height5) + '\n')
        file6.write('0 ' + str(centerx6) + ' ' + str(centery6) + ' ' + str(width1) + ' ' + str(height1) + '\n')
        file7.write('0 ' + str(centerx7) + ' ' + str(centery7) + ' ' + str(width2) + ' ' + str(height2) + '\n')
        file8.write('0 ' + str(centerx8) + ' ' + str(centery8) + ' ' + str(width3) + ' ' + str(height3) + '\n')
        file9.write('0 ' + str(centerx9) + ' ' + str(centery9) + ' ' + str(width4) + ' ' + str(height4) + '\n')
        file10.write('0 ' + str(centerx10) + ' ' + str(centery10) + ' ' + str(width5) + ' ' + str(height5) + '\n')

    print("complete")
