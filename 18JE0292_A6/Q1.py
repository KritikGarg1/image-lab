#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:10:15 2022

@author: dhyeybm
"""
import numpy as np
import math
import cv2

def erosion(img,struct):
    res = np.zeros(img.shape,np.uint8)
    r,c = img.shape
    for i in range(1,r-2):
        for j in range(1,c-2):
            res[i][j] = 1
            for ii in range(-1,3):
                for jj in range(-1,3):
                    res[i][j] = res[i][j]&((~struct[1+ii][1+jj])|img[i+ii][j+jj])
            res[i][j] = res[i][j]*255
    return res

def dilation(img,struct):
    res = np.zeros(img.shape,np.bool_)
    img = img.astype(np.bool_)
    r,c = img.shape
    for i in range(1,r-2):
        for j in range(1,c-2):
            res[i][j] = 0
            for ii in range(-1,3):
                for jj in range(-1,3):
                    res[i][j] = res[i][j]|((struct[1+ii][1+jj])&img[i+ii][j+jj])
            # res[i][j] = res[i][j]*255
    res = res.astype(np.uint8)
    res = np.multiply(res,255)
    return res
                    
                    
                    
                    
img = cv2.imread('Q1_sample.png',0)
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Original",img)
cv2.waitKey(0)

struct = np.ones((4,4),np.uint8)
res1 = erosion(img,struct)
res2 = dilation(img,struct)

cv2.imshow("Erosion",res1)
cv2.waitKey(0)

cv2.imshow("Dilation",res2)
cv2.waitKey(0)

cv2.destroyAllWindows()
