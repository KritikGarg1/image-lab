#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:57:29 2022

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
    res = np.subtract(img,res)
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
                
def boundary_filling(image_file, level):
  x, y = image_file.shape
  now = np.zeros(shape=(x, y), dtype=np.uint8)
  # now = image_file
  now[int(np.round(x//2))][int(np.round(y//2))] = 255
  
  next = cv2.bitwise_and(dilation(now, level), cv2.bitwise_not(image_file))
  
  while (next == now).all() == 0:
      now = next.copy()
      next = cv2.bitwise_and(dilation(now,level),cv2.bitwise_not(image_file))

  return cv2.bitwise_or(now, image_file)
        
        
    

img = cv2.imread('Q2_sample.png',0)
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Original",img)
cv2.waitKey(0)

struct = np.ones((3,3),np.uint8)
res1 = erosion(img,struct)

res2 = boundary_filling(res1,struct)

cv2.imshow("Erosion",res1)
cv2.waitKey(0)
cv2.imshow("Boundary Filled",res2)
cv2.waitKey(0)

cv2.destroyAllWindows()