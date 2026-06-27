#brightness enhanced    
import cv2
import numpy as np

img=cv2.imread('image.jpg')
img=cv2.resize(img,(500,500))

bright=cv2.convertScaleAbs(img, alpha=1.0, beta=50)

img2=np.hstack((img,bright))

cv2.imshow("Original vs Brightened", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

