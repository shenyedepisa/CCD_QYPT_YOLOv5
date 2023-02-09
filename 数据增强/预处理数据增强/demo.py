import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/image_000044.jpg')
edges = cv2.Canny(img,100,200,L2gradient=False)
edges2 = cv2.Canny(img,100,200,L2gradient=True)
plt.subplot(131),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image1'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(edges2,cmap = 'gray')
plt.title('Edge Image2'), plt.xticks([]), plt.yticks([])
plt.show()
