#histogram of grayscale image
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

plt.hist(img.ravel(), 256, [0, 256])
plt.ylim(0, 90000)  # Adjust the y-axis limit as needed

plt.title('Histogram of Grayscale Image')
plt.show() 


