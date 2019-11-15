import cv2
import numpy as np

"""
Hough Line Transform basics
-Representation of a line in an image
    *Standard Hough Transform (HoughLines method)
    *Probabilistic Hough Line Transform (HoughLinesP method)
"""

# HougLines method

image = cv2.imread('../images/sudoku.png')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cannyEdges = cv2.Canny(imageGray, 50, 150, apertureSize=3)
cv2.imshow('CannyEdge', cannyEdges)
# get hough lines from an edge detected image
lines = cv2.HoughLines(cannyEdges, 1, np.pi / 180, 200)

for line in lines:
    # rho - distance from the coordinate (0, 0)
    # theta - line rotation angle in radians
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho

    # x1 stores the round off value of (r * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # y1 stores the round off value of (r * sin(theta) + 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    # x2 stores the round off value of (r * cos(theta) + 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the round off value of (r * cos(theta) - 1000 * sin(theta))
    y2 = int(y0 - 1000 * (a))

    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# This method take a lot of computation but doesn't give a better result
# Better result can be obtained by the HoughLinesP method

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
