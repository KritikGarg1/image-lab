from numpy import *
import cv2
img = cv2.imread("Test_Image.png", cv2.IMREAD_GRAYSCALE)
(thresh, src) = cv2.threshold(img , 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Original", src)
cv2.waitKey(0)
n,m = src.shape
cnt = -1 
for i in range(n-1):
    for j in range(m-1):
        if src[0][0] == src[i][j] and src[0][1] == src[i][j+1] and src[1][0] == src[i+1][j] and src[1][1] == src[i+1][j+1]:
            cnt = cnt + 1

if cnt > 0:
    print('True,'+str(cnt))
else:
    print('False')
    
cv2.destroyAllWindows()