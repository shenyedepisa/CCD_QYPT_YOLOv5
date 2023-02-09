from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import argparse


def zrtt(image,angle,xy,fill,ft):

 

    width,height=image.size
    maxdim=max(width,height)

    masksize=(maxdim*2,maxdim*2)
    mask=Image.new('L',masksize,0)
    
    draw=ImageDraw.Draw(mask)
    draw.text((maxdim,maxdim),u'密',255,font=ft)

    if angle%90==0:
        rotatedmask=mask.rotate(angle)
    else:
        biggermask=mask.resize((maxdim*8,maxdim*8),resample=Image.BICUBIC)
        rotatedmask=biggermask.rotate(angle).resize(masksize,resample=Image.LANCZOS)


    maskxy=(maxdim-xy[0],maxdim-xy[1])
    bbox=maskxy+(maskxy[0]+width,maskxy[1]+height)
    mask=rotatedmask.crop(bbox)

    
    colorimage=Image.new('RGBA',image.size,fill)
    mask=mask.resize(image.size)
    colorimage=colorimage.resize(image.size)

    print('zhdebug width,height:', width,height)
    print('zhdebug xy:', xy)
    print('zhdebug maxdim:',maxdim)
    print('zhdebug  maskxy:',maskxy)
    print('zhdebug','bbox:',bbox)
    print('zhdebug','colorimage:',colorimage,' mask:',mask)
    
    image.paste(colorimage,mask)



if __name__=='__main__':

    # 以下代码仅仅是 测试功能是否正常
    # 经测试 效果还可以 ， 达到了预期目标 ，   30 代表逆时针旋转 30度

    im=Image.open('./../finalnotmi/images/image_000001.jpg').convert('RGB')

    im2=Image.open('./../finalnotmi/images/image_000001.jpg').convert('RGB')

    fnt1=ImageFont.truetype(r'./fonts/chinese.stxingka.ttf',80)

    # zrtt  参数讲解， 图片，密字xy坐标,颜色，字体
    zrtt(im2,45,(0.1*im2.size[0],0.1*im2.size[1]),'blue',fnt1)

    im2.save('./zhrotate.jpg')
        


