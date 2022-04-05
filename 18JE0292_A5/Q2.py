#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 16:25:34 2022

@author: dhyeybm
"""
import numpy as np
import cv2

img = cv2.imread('img1.png',0)
img = img.astype('float')
img = img/255

cv2.imshow("Original",img)
cv2.waitKey(0)

row,col = img.shape
s_vs_p = 0.2
amount = 0.1
out = np.copy(img)
# Salt mode
num_salt = np.ceil(amount * img.size * s_vs_p)
coords = [np.random.randint(0, i - 1, int(num_salt))
        for i in img.shape]
out[coords] = 1

# Pepper mode
num_pepper = np.ceil(amount* img.size * (1. - s_vs_p))
coords = [np.random.randint(0, i - 1, int(num_pepper))
        for i in img.shape]
out[coords] = 0

cv2.imshow("S&P",out)
cv2.waitKey(0)

mean = 0.01
var = 0.01
sigma = var**0.5
gauss = np.random.normal(mean,sigma,(row,col))
gauss = gauss.reshape(row,col)

noisy = img + gauss
cv2.imshow("Gaussian",noisy)
cv2.waitKey(0)


cv2.destroyAllWindows()