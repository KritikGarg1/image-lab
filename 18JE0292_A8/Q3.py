#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:45:52 2022

@author: dhyeybm
"""
import cv2
import numpy as np

img=cv2.imread("Input3.png",0)

def local(img):
    avg=0;
    r,c=img.shape
    for i in range(r):
        for j in range(c):
            avg=0
            for tx in range(15):
                for ty in range(15):
                    if(i+tx>=r or j+ty>=c):
                        avg+=0
                    else:
                        avg+=img[i+tx][j+ty]
            avg=avg//(15*15)
            T=avg-5
            if(img[i][j]<T):
                img[i][j]=0
            else:
                img[i][j]=255
                
    return img

img1=local(img)

cv2.imshow("output",img1)
cv2.waitKey(0)