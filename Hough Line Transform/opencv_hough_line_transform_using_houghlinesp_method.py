import cv2
import numpy as np

"""
Hough Line Transform basics
-Representation of a line in an image
    *Standard Hough Transform (HoughLines method)
    *Probabilistic Hough Line Transform (HoughLinesP method)
"""

# HoughLinesP method
# Does not take all points into consideration. Instead, it take only the randoms of set of the points
# which is sufficient for the line detection

# image = cv2.imread('../images/sudoku.png')
image = cv2.imread('../images/road.png')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cannyEdges = cv2.Canny(imageGray, 50, 150, apertureSize=3)
cv2.imshow('CannyEdges', cannyEdges)

"""
*line segments shorter than 100 are rejected
*lines which has a gap less than 10 are treated as one line
"""
lines = cv2.HoughLinesP(cannyEdges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# This method does not take much calculation. But gives a better result than the standard method

cv2.imshow('ImageLines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
