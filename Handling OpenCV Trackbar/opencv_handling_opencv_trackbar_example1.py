import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


# create a black image and its window
image = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

# create trackbars to control BGR channels
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

# toggle switch as a trackbar (0 and 1)
switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    cv.imshow('image', image)
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

    # get trackbar positions (values)
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    # if switch is toggled, allow colour change
    if s == 0:
        image[:] = 0  # all channels black (0)
    else:
        image[:] = [b, g, r]  # apply trackbar values for channels

cv.destroyAllWindows()
