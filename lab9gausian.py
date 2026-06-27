#gaussian filter
import cv2
import numpy as np

img = cv2.imread('image.jpg')
img=cv2.resize(img,(600,600))

gauss = cv2.GaussianBlur(img, (5,5), 0)

nimg=np.hstack((img,gauss))

cv2.imshow("Original vs Gaussian Filter", nimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

