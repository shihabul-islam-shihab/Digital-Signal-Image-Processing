#color enhancement
import cv2
import numpy as np

img=cv2.imread('image.jpg')
img=cv2.resize(img,(500,500))

enhanced = cv2.convertScaleAbs(img, alpha=1.2, beta=0)

img2=np.hstack((img,enhanced))
cv2.imshow("Original vs Enhanced", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()



