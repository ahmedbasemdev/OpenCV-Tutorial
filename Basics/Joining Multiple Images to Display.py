import cv2
import numpy as np

# if we put 0 it will load image as gray scale
img1 = cv2.imread("../Images/lena.png")
img2 = cv2.imread("../Images/lena.png")

img1 = cv2.resize(img1, (0, 0), None, 0.5, 0.5)
img2 = cv2.resize(img2, (0, 0), None, 0.5, 0.5)

# it works only if both images have the same size and the same number of channels
hor = np.hstack((img1,img2))
ver = np.vstack((img1,img2))

cv2.imshow("Vertical", ver)
cv2.imshow('Horizontal', hor)

cv2.waitKey(0)