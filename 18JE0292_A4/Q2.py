#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 16:09:11 2022

@author: dhyeybm
"""

import cv2
import numpy as np
def find_edge(img,filter_x,filter_name):
    x,y = img.shape
    g_x = np.zeros((x,y))
    dx = [0,0,0,1,1,1,2,2,2]
    dy = [0,1,2,0,1,2,0,1,2]
    for i in range(1,x-1):
        for j in range(1,y-1):
            for idx in range(9):
                g_x[i,j] = g_x[i,j] + img[i+dx[idx]-1,j+dy[idx]-1]*filter_x[dx[idx],dy[idx]]
    g =  np.subtract(img,g_x)
    cv2.imshow(filter_name,g_x)
    cv2.waitKey(0)
    
    cv2.imshow(filter_name+" Difference",g)    
    cv2.waitKey(0)
    
img = cv2.imread('img2.png', 0)
cv2.imshow("Original", img)
cv2.waitKey(0)
print(img.shape)
laplacian = np.array([[0,1,0],[1,-4,1],[0,1,0]])
find_edge(img,laplacian,"Laplacian")

advanced= np.array([[1,1,1],[1,-8,1],[1,1,1]])
find_edge(img,advanced,"Advanced Laplacian")

cv2.destroyAllWindows()
    
        
    
            
            
    