#gaussian filter
import cv2
import numpy as np

img = cv2.imread('image.jpg')
img1=cv2.imread('image.jpg',0)
img=cv2.resize(img,(400,400))
img1=cv2.resize(img1,(400,400))

gauss1 = cv2.GaussianBlur(img1, (5,5), 0)
gauss2 = cv2.GaussianBlur(img, (5,5), 0)

# Convert grayscale to BGR (3-channel)
gauss1 = cv2.cvtColor(gauss1, cv2.COLOR_GRAY2BGR)

img2=np.hstack((img,gauss1,gauss2))

cv2.imshow("Original vs Gaussian gray vs gau RGB", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

