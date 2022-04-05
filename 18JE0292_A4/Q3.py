#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 16:49:26 2022

@author: dhyeybm
"""


import cv2
import numpy as np
import math

def dft(input_img):
    rows = input_img.shape[0]
    cols = input_img.shape[1]
    output_img = np.zeros((rows,cols),complex)
    for m in range(0,rows):
        for n in range(0,cols):
            for x in range(0,rows):
                for y in range(0,cols):
                    output_img[m][n] += input_img[x][y] * np.exp(-1j*2*math.pi*(m*x/rows+n*y/cols))
    return output_img

img = cv2.imread('img3.png',0)
cv2.imshow("Original",img)

scale_percent = 70 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
img1 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
img2 = dft(img1)
cv2_imshow("DFT",img2)
