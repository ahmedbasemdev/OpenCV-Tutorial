import cv2
import numpy as np

img = cv2.imread('../Images/card.jpeg')
width, height = 250, 350
pts1 = np.float32([[80, 2], [185, 25], [1, 130], [140, 175]])
pts2 = np.float32([[0, 0], [width, 0], [0,height], [width, height]])

# it will allow us to ger prespictve transofrmer
matrix = cv2.getPerspectiveTransform(pts1,pts2)
output_img = cv2.warpPerspective(img,matrix,(width,height))


for idx in range(0, 4):
    cv2.circle(img, (int(pts1[idx][0]), int(pts1[idx][1])), 10, (0, 255, 0), cv2.FILLED)


cv2.imshow("Origian Image", img)
cv2.imshow("Output Image", output_img)

cv2.waitKey(0)

#### Explaination ####

# we need to need 3 point norners of
# image to convert it to 2D
