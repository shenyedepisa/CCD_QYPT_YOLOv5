import cv2
import numpy as np
from skimage.filters import threshold_local
from scipy.ndimage.filters import gaussian_filter

img = cv2.imread('images/image_000000.jpg')
import matplotlib.pyplot as plt  # plt 用于显示图片

# 转换大小 保存副本
orig = img.copy()
# ratio = img.shape[0] / 500.0
# img = imutils.resize(img,height = 500)

# 预处理 转灰度图->滤波->边缘检测
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (1,1), 0)
edge = cv2.Canny(gray, 5, 500)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
src1 = img.astype(np.float32)
gauss = gaussian_filter(img, sigma=1)
gauss1 = gauss.astype(np.float32)
dst1 = (src1 / gauss1)
cv2.imshow('1', dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# T = threshold_local(dst1, 25, method='gaussian', offset=13)
# transformed = (dst1 > T).astype('uint8') * 255
# cv2.imshow('origin', orig)
# cv2.imshow('scanned', transformed)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
