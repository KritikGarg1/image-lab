# -*- coding: utf-8 -*-

def Pixel_adj(Im, adj, V, p):
    n4_x = [1,-1,0,0]
    n4_y = [0,0,1,-1]
    n4 = []
    for i in range(4):
        nx = p[0]+n4_x[i]
        ny = p[1]+n4_y[i]
        if V.count(Im[nx-1][ny-1]) >=1 :
            n4.append((nx,ny))
    if adj == "4-adjacency":
        return n4
    nd_x = [1,-1,1,-1]
    nd_y = [1,1,-1,-1]
    nd = []
    for i in range(4):
        nx = p[0]+nd_x[i]
        ny = p[1]+nd_y[i]
        if nx>=0 and ny>=0 and nx<len(Im) and ny<len(Im[0]) and V.count(Im[nx-1][ny-1])>=1:
            nd.append((nx,ny))
    if adj == "8-adjacency":
        return n4+nd
    madj = n4
    for q in nd:
        n4_q = Pixel_adj(Im,"4-adjacency",V,q)
        if len(list(set(n4_q)&set(n4))) == 0:
            madj.append(q)
    return madj

Im = [[3,5, 3, 5, 2, 4, 3, 2],
[4 ,6 ,6 ,7 ,3 ,3 ,7 ,6] ,
[6 ,3 ,0 ,3, 1, 3, 2, 3],
[5 ,4 ,2 ,1 ,2 ,3 ,6 ,7],
[2, 7, 3, 0, 0, 1, 2, 5],
[7, 4, 1, 0, 2, 3, 3, 4],
[4, 2, 7, 3, 5, 7, 2, 5],
[2, 6, 5, 4, 2, 7, 5, 6]]

P = [4,4]
V = [0,1]

print("4 Adjacency:")
print( Pixel_adj(Im, "4-adjacency", V, P))

print("8 Adjacency:")
print( Pixel_adj(Im, "8-adjacency", V, P))

print("m Adjacency:")
print( Pixel_adj(Im, "m-adjacency", V, P))
    