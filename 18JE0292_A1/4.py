import numpy as np
import cv2
src = cv2.imread("Test_Image.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", src)
cv2.waitKey(0)
n,m = src.shape

for bit in range(8):
    plane = np.zeros(src.shape)
    for i in range(n):
        for j in range(m):
            plane[i][j] = (src[i][j]&(1<<bit))
    cv2.imshow('Plane'+str(bit), plane)
    cv2.waitKey(0)
            
            
cv2.destroyAllWindows()

        