#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:49:52 2022

@author: dhyeybm
"""

import cv2
import numpy as np

def change(img,points):
    print(points[0][0])
    m1 = (points[0][1]-points[1][1])/(points[0][0]-points[1][0])
    m2 = (points[1][1]-points[2][1])/(points[1][0]-points[2][0])
    m3 = (points[2][1]-points[3][1])/(points[2][0]-points[3][0])
    
    c1 = points[0][1]-m1*points[0][0]
    c2 = points[1][1]-m2*points[1][0]
    c3 = points[2][1]-m3*points[2][0]
    
    modified = img.copy()
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if modified[i][j]<=points[1][0]:
                modified[i][j] = m1*modified[i][j]+c1
            elif modified[i][j]>points[1][0] and modified[i][j]<=points[2][0]:
                modified[i][j] = m2*modified[i][j]+c2
            elif modified[i][j]>points[2][0] and modified[i][j]<=points[3][0]:
                modified[i][j] = m3*modified[i][j]+c3
    return modified
    
    
img = cv2.imread("image.png",0)
print(img.shape)

print("Enter defining points to be used for contrast stretching:")
# points = [[0, 0], [150, 20], [200, 200], [223, 223]]
points = []
for i in range(4):
    temp = []
    temp.append(int(input()))
    temp.append(int(input()))
    points.append(temp)
print(points)

modified = change(img,points)

cv2.imshow("Original", img)
cv2.waitKey(0)

cv2.imshow("Result", modified)
cv2.waitKey(0)

cv2.destroyAllWindows()