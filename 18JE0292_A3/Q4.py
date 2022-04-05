#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 16:00:27 2022

@author: dhyeybm
"""
import cv2
import numpy as np
img = cv2.imread('cameraman.png',0)

cv2.imshow("Original", img)
cv2.waitKey(0)

nrow,ncol = img.shape
img1 = np.zeros((nrow,ncol))
img2 = np.zeros((nrow,ncol))

for i in range(nrow):
    for j in range(ncol):
        if img[i,j] >= 100 and img[i,j]<=200:
            img1[i,j] = 255
            img2[i,j] = 0
        else:
            img1[i,j] = 0
            img2[i,j] = 255


cv2.imshow('out1',img1)
cv2.waitKey(0)

cv2.imshow('out2',img2)
cv2.waitKey(0)

cv2.destroyAllWindows()

