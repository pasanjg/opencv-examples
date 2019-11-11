import cv2
import numpy as np

image = cv2.imread('../images/opencv-logo.png')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # binary image

# apply threshold to the binary image
ret, threshold = cv2.threshold(imageGray, 127, 255, 0)


"""
    contours -  returns a list of contours of the image. Each individual is a numpy array of (x, y) boundary points
                joining the coordinates will give the boundary of the contour
    hierarchy - optional output vector containing information about image topology
"""
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("No of contours: " + str(len(contours)))
print(contours[0])  # display contour at index 0

# draw contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)  # -1 draws all the contours [index of contour]


cv2.imshow('Image', image)
cv2.imshow('Image Gray', imageGray)
cv2.waitKey(0)
cv2.destroyAllWindows()
