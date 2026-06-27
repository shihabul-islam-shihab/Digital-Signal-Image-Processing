#gradient img
import cv2
import numpy as np

img = cv2.imread('image.jpg', 0)
img = cv2.resize(img, (400, 400))

grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)

img2=np.hstack((grad_x, grad_y))

cv2.imshow("Gradient X vs Gradient Y", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()



