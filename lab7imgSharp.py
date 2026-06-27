#image Sharpening
import cv2
import numpy as np

img = cv2.imread('image.jpg')
img=cv2.resize(img,(500,500))

kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
sharpened = cv2.filter2D(img, -1, kernel)

img2=np.hstack((img,sharpened))

cv2.imshow("Original vs Sharpened", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()