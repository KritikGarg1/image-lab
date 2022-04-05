#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:38:18 2022

@author: dhyeybm
"""

import cv2
import numpy as np

img = cv2.imread('Input2.png',0)
cv2.imshow('Original',img)
cv2.waitKey(0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])

L = hist.shape[0]
# print(hist.shape)
a = np.zeros(L)
b = np.zeros(L)
a[0] = hist[0]
b[0] = 0
for k in range(1,L,1):
  a[k] = a[k-1] + hist[k]
  b[k] = b[k-1] + k*hist[k]

u = b[L-1]/a[L-1]
c = 0
d = -1
t = -1
for k in range(0,L):
  c = np.square(b[k]-u*a[k])/(a[k]*(a[L-1]-a[k]))
  if d<c:
    d = c
    t = k

# print(t)
# x = 0
# cv2_imshow(img)
row,col = img.shape
y = np.zeros(img.shape)
for i in range(row):
  for j in range(col):
    # x = max(x,img[i][j])
    if img[i][j]>=t:
      y[i][j] = 255
# print(x)
cv2.imshow("Result",y)