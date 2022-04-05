#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:46:28 2022

@author: dhyeybm
"""
import numpy as np
import math
import cv2



img = cv2.imread('Q3.png',1)
# img[:,:,2:3] = np.zeros((256,256,1))
# img[:,:,0:2] = np.zeros((256,256,2))

# print(img.shape)
cv2.imshow("Original",img)
cv2.waitKey(0)
# r = img[:,:,0:1]
# print(r.shape)
res = np.zeros(img.shape)
r,c,x = img.shape
for i in range(r):
    for j in range(c):
        if img[i][j][0] >=210:
            res[i][j][0] = 255
        elif img[i][j][0]>=125:
            res[i][j][1] = 255
        elif img[i][j][0]>=9:
            res[i][j][2] = 255
            
cv2.imshow("Segmentation",res)
cv2.waitKey(0)        
        

# cv2.destroyAllWindows()