import cv2
import numpy as np


def compression(img):
    n,m = img.shape
    out = []
    for j in range(0,m):
        prev=-1
        cnt=0
        for i in range(0,n):
            if img[i, j] == prev:
                cnt = cnt+1
            else:
                if prev!=-1:
                    out.append(prev)
                    out.append(cnt)
                cnt=1
                prev = img[i,j]
        out.append(prev)
        out.append(cnt)
    return out
                
def decompress(arr,m):
    n=0
    k = len(arr)
    for i in range(1,k,2):
        n = n+arr[i]
    #print(n)
    n = int(n/m)
    out = np.zeros([n,m],dtype=np.uint8)
    k=0
    for j in range(0,m):
        for i in range(0,n):
            if arr[k+1]==0: 
                k = k+2
            out[i,j] = arr[k]
            arr[k+1] = arr[k+1]-1
    return out





img = cv2.imread('Input1.jpg',0)
n,m = img.shape
#print(img.shape)
out = compression(img)
#print(out)
out_image = decompress(out,m)
cv2.imwrite("q1-out.jpg", out_image)
