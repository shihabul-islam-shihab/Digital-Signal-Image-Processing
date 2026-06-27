#average filtering
import cv2
import numpy as np  

img=cv2.imread('image.jpg')
img=cv2.resize(img,(500,500))   

avg = cv2.blur(img, (5,5))

img2=np.hstack((img,avg))

cv2.imshow("Original vs Average Filter", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()