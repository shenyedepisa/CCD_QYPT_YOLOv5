import numpy as np
import random
import cv2
import os
import argparse

def sp_noise(image,prob):
  '''
  添加椒盐噪声
  prob:噪声比例 
  '''
  output = np.zeros(image.shape,np.uint8)
  thres = 1 - prob 
  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
      rdn = random.random()
      if rdn < prob:
        output[i][j] = 0
      elif rdn > thres:
        output[i][j] = 255
      else:
        output[i][j] = image[i][j]
  return output

def gasuss_noise(image, mean=0, var=0.001):
  ''' 
    添加高斯噪声
    mean : 均值 
    var : 方差
  '''
  image = np.array(image/255, dtype=float)
  noise = np.random.normal(mean, var ** 0.5, image.shape)
  out = image + noise
  if out.min() < 0:
    low_clip = -1.
  else:
    low_clip = 0.
  out = np.clip(out, low_clip, 1.0)
  out = np.uint8(out*255)
  return out


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

  fileList = os.listdir(args.src)
  for fileName in fileList:
      img_name = os.path.join(args.src, fileName)
      img = cv2.imread(img_name)
      ret,binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
      img_sp = sp_noise(binary,0.1)
      # img_gas = gasuss_noise(binary)
      img_dst = img_name.replace(args.src, args.dst)
      print(img_dst, end=" ")
      if cv2.imwrite(img_dst, img_sp):
        print('done')
      else:
        print('fail')
