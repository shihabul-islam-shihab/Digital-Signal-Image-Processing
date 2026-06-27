#median filtering
import cv2
import numpy as np   

img=cv2.imread('image.jpg')
img=cv2.resize(img,(500,500))

median = cv2.medianBlur(img, 5)

img2=np.hstack((img,median))

cv2.imshow("Original vs Median Filter", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

