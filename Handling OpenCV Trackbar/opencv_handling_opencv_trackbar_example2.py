import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


# create a black image and its window
cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 10, 400, nothing)

switch = 'COLOR/GRAY'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    image = cv.imread('../images/lena.jpg')
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(image, str(pos), (50, 150), font, 2, (0, 0, 255), 2)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

    s = cv.getTrackbarPos(switch, 'image')

    #  if switch is toggled, convert to grayscale
    if s == 0:
        pass
    else:
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    image = cv.imshow('image', image)

cv.destroyAllWindows()
