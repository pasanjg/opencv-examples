import cv2
import numpy as np

image = cv2.imread('../images/lena.jpg')

# lower resolution
# lr1 = cv2.pyrDown(image)
# lr2 = cv2.pyrDown(lr1)

# higher resolution
# hr2 = cv2.pyrUp(lr2)

layer = image.copy()  # create a copy of the image
gp = [layer]  # gaussian pyramid list

# generate 6 images lower than original
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)  # gaussian pyramid
    # cv2.imshow(str('pyrDown' + str(i + 1)), layer)

# creating the Laplacian Pyramid
layer = gp[5]
cv2.imshow('Upper Level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i - 1], gaussian_extended)  # creating the laplacian pyramid
    cv2.imshow(str(i), laplacian)

cv2.imshow('Original Image', image)
# cv2.imshow('pyrDown1 Image', lr1)
# cv2.imshow('pyrDown2 Image', lr2)
# cv2.imshow('pyrUp1 Image', hr2)

cv2.waitKey(0)
cv2.destroyAllWindows()
