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
    for i in range(1,r-1):
        for j in range(1,c-1):
            res[i][j] = 1
            for ii in range(-1,2):
                for jj in range(-1,2):
                    res[i][j] = res[i][j]&((~struct[1+ii][1+jj])|img[i+ii][j+jj])
            res[i][j] = res[i][j]*255
    return res

def dilation(img,struct):
    res = np.zeros(img.shape,np.bool_)
    img = img.astype(np.bool_)
    r,c = img.shape
    for i in range(1,r-1):
        for j in range(1,c-1):
            res[i][j] = 0
            for ii in range(-1,2):
                for jj in range(-1,2):
                    res[i][j] = res[i][j]|((struct[1+ii][1+jj])&img[i+ii][j+jj])
            # res[i][j] = res[i][j]*255
    res = res.astype(np.uint8)
    res = np.multiply(res,255)
    return res

def segmentation(img,dilated,thresh):
    res = np.zeros(img.shape,np.uint8)
    r,c = img.shape
    for i in range(r):
        for j in range(c):
            if dilated[i][j] > thresh:
                res[i][j] = img[i][j]
    return res

img = cv2.imread('Q2.png',0)
cv2.imshow("Original",img)
cv2.waitKey(0)
ret, img_bin = cv2.threshold(img, 107, 255, cv2.THRESH_BINARY)
struct = np.ones((3,3),np.uint8)

cv2.imshow("Binary",img_bin)
cv2.waitKey(0)

res1 = erosion(img_bin, struct)
res2 = dilation(res1, struct)

cv2.imshow("Eroded",res1)
cv2.waitKey(0)

cv2.imshow("Dilated",res2)
cv2.waitKey(0)

res = segmentation(img,res2,107)
cv2.imshow("Extracted Flower",res)
cv2.waitKey(0)