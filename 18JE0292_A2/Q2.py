#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 16:33:38 2022

@author: dhyeybm
"""

import numpy as np
def Pixel_adj(Im, adj, V, p):
    n4_x = [1,-1,0,0]
    n4_y = [0,0,1,-1]
    n4 = []
    for i in range(4):
        nx = p[0]+n4_x[i]
        ny = p[1]+n4_y[i]
        if V.count(Im[nx-1][ny-1]) >=1 :
            n4.append([nx,ny])
    if adj == "4-adjacency":
        return n4
    nd_x = [1,-1,1,-1]
    nd_y = [1,1,-1,-1]
    nd = []
    for i in range(4):
        nx = p[0]+nd_x[i]
        ny = p[1]+nd_y[i]
        if nx>=0 and ny>=0 and nx<len(Im) and ny<len(Im[0]) and V.count(Im[nx-1][ny-1])>=1:
            nd.append([nx,ny])
    if adj == "8-adjacency":
        return n4+nd
    madj = n4
    for q in nd:
        n4_q = Pixel_adj(Im,"4-adjacency",V,q)
        print(n4_q,n4)
        if len(list(set(n4_q)&set(n4))) == 0:
            madj.append(q)
    return madj

def find_Path(Im,P,S,V,vis,curr,adj):
    # print(P)
    if P == S:
        print(curr)
        return
    neighbors = Pixel_adj(Im, adj, V, P)
    # print(neighbors)
    for neighbor in neighbors:
        if vis[neighbor[0]-1][neighbor[1]-1] == 0:
            # print("From",P,"to ",neighbor)
            vis[neighbor[0]-1][neighbor[1]-1] = 1
            curr.append(neighbor)
            find_Path(Im,neighbor,S,V,vis,curr,adj)
            vis[neighbor[0]-1][neighbor[1]-1] = 0
            curr.pop()
    
            
    
    
    
    

Im = [[3,5, 3, 5, 2, 4, 3, 2],
[4 ,6 ,6 ,7 ,3 ,3 ,7 ,6] ,
e[6 ,3 ,0 ,3, 1, 3, 2, 3],
[5 ,4 ,2 ,1 ,2 ,3 ,6 ,7],
[2, 7, 3, 0, 0, 1, 2, 5],
[7, 4, 1, 0, 2, 3, 3, 4],
[4, 2, 7, 3, 5, 7, 2, 5],
[2, 6, 5, 4, 2, 7, 5, 6]]

P = [3,5]
S = [5,5]
V = [0,1]

print("4 Adjacency:")
vis = np.zeros((len(Im),len(Im[0])))
vis[P[0]-1][P[1]-1] = 1
curr = [P]
find_Path(Im,P,S,V,vis,curr,"4-adjacency")

print("8 Adjacency:")
vis = np.zeros((len(Im),len(Im[0])))
vis[P[0]-1][P[1]-1] = 1
curr = [P]
find_Path(Im,P,S,V,vis,curr,"8-adjacency")


print("m Adjacency:")
vis = np.zeros((len(Im),len(Im[0])))
vis[P[0]-1][P[1]-1] = 1
curr = [P]
find_Path(Im,P,S,V,vis,curr,"m-adjacency")
