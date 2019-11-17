import numpy as np
import cv2

"""
Shi Tomasi - Good Features To Track;
    *Similar to Harris Corner Detector but gives better results.
    *We can provide the no. of corners to detect
"""

image = cv2.imread('../images/pic1.png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find the strongest corners (as specified by maxCorners)
corners = cv2.goodFeaturesToTrack(image_gray, 50, 0.01, 10)  # 50 - maxCorners: displays the strongest 25 corners

# convert the corners into int64 (int0)
corners = np.int0(corners)

# loop through all the corners
for corner in corners:
    x, y = corner.ravel()  # find the coordinates of the corner
    cv2.circle(image, (x, y), 3, 255, -1)  # draw a dot in the detected corner

cv2.imshow('Result', image)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
