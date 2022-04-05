#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:49:08 2022

@author: dhyeybm
"""
import cv2
import numpy as np
img = cv2.imread('pout_Q3.png',0)


def con_min(data, filter_size):    
    indexer = (int)(filter_size / 2)
    new_image = data.copy()
    nrow, ncol = data.shape
    for i in range(nrow):
        for j in range(ncol):
            l=[]
            for k in range(i-indexer, i+indexer+1):
                for m in range(j-indexer, j+indexer+1):
                    if (k > -1) and (k < nrow):
                        if (m > -1) and (m < ncol):
                            l.append(data[k,m])
            l.sort()
            new_image[i,j]=l[(int)(len(l)/2)]
    return new_image
img1=con_min(img,3)
img2=con_min(img,5)
img3=con_min(img,7)

cv2.imshow('inp',img)
cv2.waitKey(0)

cv2.imshow('out1',img1)
cv2.waitKey(0)

cv2.imshow('out2',img2)
cv2.waitKey(0)

cv2.imshow('out3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
