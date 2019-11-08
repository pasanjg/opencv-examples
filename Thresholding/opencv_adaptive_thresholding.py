import cv2 as cv
import numpy as np

"""
Calculates threshold for smaller regions of the image
Gives better results with varying illuminations
"""

image = cv.imread('../images/sudoku.png', 0)
_, th1 = cv.threshold(image, 127, 255, cv.THRESH_BINARY)

# ADAPTIVE_THRESH_MEAN_C - Threshold value is the mean of the area
th2 = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

# ADAPTIVE_THRESH_GAUSSIAN_C - Threshold value is a weighted sum of the area
th3 = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow('image', image)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)

cv.waitKey(0)
cv.destroyAllWindows()
