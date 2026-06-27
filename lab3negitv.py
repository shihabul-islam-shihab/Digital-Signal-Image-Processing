#negative image
import cv2
import numpy as np

img=cv2.imread('image.jpg', 0)
img=cv2.resize(img,(400,400))
neg=255-img

img2=np.hstack((img,neg))

cv2.imshow("Original vs Negative", img2)

cv2.waitKey(0)  
cv2.destroyAllWindows()