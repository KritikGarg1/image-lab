#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 15:09:31 2022

@author: dhyeybm
"""

import cv2
import numpy as np
def find_edge(img,filter_x,filter_y,filter_name):
    x,y = img.shape
    g_x = np.zeros((x,y))
    g_y = np.zeros((x,y))
    dx = [0,0,0,1,1,1,2,2,2]
    dy = [0,1,2,0,1,2,0,1,2]
    for i in range(1,x-1):
        for j in range(1,y-1):
            for idx in range(9):
                g_x[i,j] = g_x[i,j] + img[i+dx[idx]-1,j+dy[idx]-1]*filter_x[dx[idx],dy[idx]]
                g_y[i,j] = g_y[i,j] + img[i+dx[idx]-1,j+dy[idx]-1]*filter_y[dx[idx],dy[idx]]
    g =  np.round(np.sqrt(np.add(np.square(g_x),np.square(g_y))))
   
    # print(g_x)
    # print(g_y)
    # print(g)
    g_x = np.abs(g_x)
    g_y = np.abs(g_y)
    
    g = g.astype('uint8')
    g_x = g_x.astype('uint8')
    g_y = g_y.astype('uint8')
    # print(g)
    cv2.imshow(filter_name+" X",g_x)
    cv2.waitKey(0)
    
    cv2.imshow(filter_name+" Y",g_y)
    cv2.waitKey(0)
    
    # print(g)
    cv2.imshow(filter_name+" Sum",g)    
    cv2.waitKey(0)
    
img = cv2.imread('img1.png', 0)
cv2.imshow("Original", img)
cv2.waitKey(0)
img = img.astype('int')
sobel_x = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sobel_y = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
find_edge(img,sobel_x,sobel_y,"Sobel")

prewitt_x = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
prewitt_y = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
find_edge(img,prewitt_x,prewitt_y,"Prewitt")

cv2.destroyAllWindows()
    
        
    
            
            
    