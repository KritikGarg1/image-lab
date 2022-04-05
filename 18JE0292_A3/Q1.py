# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('pout.png', 0)

cv2.imshow("Original", img)
cv2.waitKey(0)
hist=cv2.calcHist([img],[0], None, [256],[0,255])
plt.plot(hist)
plt.show()

cnt1 = np.zeros((256,),dtype=np.float16)
cnt2 = np.zeros((256,),dtype=np.float16)
h,w = img.shape
for i in range(h):
  for j in range(w):
    x = img[i,j]
    cnt1[x] = cnt1[x] + 1

tmp = 1.0/(h*w)
for i in range(256):
  for j in range(i+1):
    cnt2[i]+=cnt1[j]*tmp
  cnt2[i] = round(cnt2[i]*255)

cnt2=cnt2.astype(np.uint8)
for i in range(h):
  for j in range(w):
    x = img[i,j]
    img[i,j] = cnt2[x]
cv2.imshow("Modified",img)
cv2.waitKey(0)

plt.figure()
hist2 = cv2.calcHist([img],[0],None,[256],[0,255])
plt.plot(hist2)
plt.show()
cv2.destroyAllWindows()
