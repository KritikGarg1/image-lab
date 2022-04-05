#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:12:19 2022

@author: dhyeybm
"""
import numpy as np
# import cv2

cnt = 1

def getRegions(mat,x_start,x_end,y_start,y_end):
    global cnt
    print(x_start,x_end,y_start,y_end)
    mn = np.amin(mat[x_start:x_end,y_start:y_end])
    mx = np.amax(mat[x_start:x_end,y_start:y_end])
    if mx-mn<=3:
        regions[x_start:x_end,y_start:y_end] = cnt
        cnt=cnt+1
    else:
        getRegions(mat,x_start,(x_start+x_end)//2,y_start,(y_start+y_end)//2)
        getRegions(mat,(x_start+x_end)//2,x_end,y_start,(y_start+y_end)//2)
        getRegions(mat,x_start,(x_start+x_end)//2,(y_start+y_end)//2,y_end)
        getRegions(mat,(x_start+x_end)//2,x_end,(y_start+y_end)//2,y_end)
        
        
    
    
    

mat = np.array([[5,6,6,6,7,7,6,6],[6,7,6,7,5,5,4,7],[6,6,4,4,3,2,5,6],[5,4,5,4,2,3,4,6],
               [1,3,2,3,3,2,4,7],[0,0,1,0,2,2,5,6],[1,1,0,1,0,3,4,4],[1,0,1,0,2,3,5,6]])

r,c = mat.shape
regions = np.zeros(mat.shape)

getRegions(mat,0,r,0,c)
print(regions)
