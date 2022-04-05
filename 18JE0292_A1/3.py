import numpy as np
import cv2
src = cv2.imread("Test_Image.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", src)
cv2.waitKey(0)
n,m = src.shape

pooled = []
for i in range(0,n,3):
    row = []
    for j in range(0,m,3):
        temp = np.amax(src[i:i+3,j:j+3])
        row.append(temp)
    pooled.append(row)

pooled = np.array(pooled)
print(pooled)
cv2.imshow("Max Pooled", pooled)
cv2.waitKey(0)


cv2.destroyAllWindows()


        
    