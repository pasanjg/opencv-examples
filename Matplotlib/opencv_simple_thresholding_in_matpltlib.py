import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Thresholding - separating an object from its background
# comparing each pixel of and image with a predefined threshold value
from urllib3.connectionpool import xrange

image = cv.imread('../images/gradient.png', 0)

"""
set threshold value - 127
compared with 127,
    pixels > 127 - white (255)
    pixels < 127 - black (0)
-INVERSE is the opposite
"""
_, th1 = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(image, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(image, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(image, 127, 255, cv.THRESH_TOZERO_INV)

# cv.imshow('image', image)
# cv.imshow('th1', th1)
# cv.imshow('th2', th2)
# cv.imshow('th3', th3)
# cv.imshow('th4', th4)
# cv.imshow('th5', th5)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [image, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    # plt.xticks([]), plt.yticks([])

# cv.waitKey(0)
# cv.destroyAllWindows()

plt.show()
