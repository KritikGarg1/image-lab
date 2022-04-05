#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:04:07 2022

@author: dhyeybm
"""
import numpy as np
import cv2

img = cv2.imread('Input1.jpg',0)
r,c = img.shape
res = np.zeros((img.shape),dtype=np.uint8)
vis = np.zeros((img.shape),dtype=np.uint8)

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

queue = []
seed = (85,64)
queue.append(seed)
vis[seed] = 1
res[seed] = 255
while len(queue) > 0:
    x,y = queue.pop(0)
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<r and ny<c and nx>=0 and ny>=0 and vis[nx,ny] == 0 and abs(img[nx,ny].astype(int)-img[x,y])<10:
            res[nx][ny] = 255
            vis[nx][ny] = 1
            queue.append((nx,ny))
cv2.imshow("Original", img)
cv2.waitKey(0)

cv2.imshow("Result", res)
cv2.waitKey(0)

cv2.destroyAllWindows()