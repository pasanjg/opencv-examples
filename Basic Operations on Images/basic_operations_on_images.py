import numpy as np
import cv2

image = cv2.imread('../images/messi5.jpg')
logo = cv2.imread('../images/opencv-logo.png')

print(image.shape)  # returns s tuple of no. of rows, columns and channels
print(image.size)  # returns the no of pixels accessed
print(image.dtype)  # returns the datatype obtained

b, g, r = cv2.split(image)  # splits the channels of the image
image = cv2.merge((b, g, r))  # merges the channels of the image

'''
Coordinates of the ball: (ROI - Region Of Interest)
    Upper Left -  X: 280  Y: 340
    Lower Right - X: 330  Y: 390
'''
ball = image[280:340, 330:390]
image[273:333, 100:160] = ball  # where you want to place the ball (copy)

# images must be resized to same before adding
image = cv2.resize(image, (512, 512))
logo = cv2.resize(logo, (512, 512))

# dst = cv2.add(image, logo)  # add two images with same weight
dst = cv2.addWeighted(image, 0.9, logo, 0.1, 0)  # add two images with specific weight (image - dominant)

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
