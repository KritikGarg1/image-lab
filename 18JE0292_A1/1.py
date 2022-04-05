
import cv2
import numpy as np

def rotateImage(img):
    rows,cols = img.shape
    n = rows
    m = cols
    for i in range((rows+1)//2):
        for j in range((cols//2)):
            temp = img[n - 1 - j,i]
            img[n - 1 - j,i] = img[n - 1 - i,n - j - 1]
            img[n - 1 - i,n - j - 1] = img[j,n - 1 -i]
            img[j,n - 1 - i] = img[i,j]
            img[i,j] = temp
    return img

def flipImage(img):
    rows,cols = img.shape
    n = rows
    m = cols
    for i in range((rows)):
        for j in range((cols//2)):
            temp = img[i][j]
            img[i][j] = img[i][m-1-j]
            img[i][m-1-j] = temp
    return img
    

src = cv2.imread("Test_Image.png",0)

cv2.imshow("Original", src)
cv2.waitKey(0)

rotated = rotateImage(src)
print((rotated == src).all())
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)

src = cv2.imread("Test_Image.png",0)
flipped= flipImage(src)
cv2.imshow("Flipped", flipped)
cv2.waitKey(0)

cv2.destroyAllWindows()