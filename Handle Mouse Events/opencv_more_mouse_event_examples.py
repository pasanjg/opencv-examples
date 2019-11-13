import numpy as np
import cv2

"""
list of all the events available in the cv2 package
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
"""


def clickEvent(event, x, y, flags, param):

    # on left mouse click - connect clicked points
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x, y), 2, (0, 0, 255), -1)  # draw a red point on clicked coordinates
        points.append((x, y))  # add clicked points to a list
        if len(points) >= 2:
            cv2.line(image, points[-1], points[-2], (255, 0, 0), 1)  # draw line connecting the last 2 indices of points
        cv2.imshow('image', image)

    # on right mouse click - show colour on point
    if event == cv2.EVENT_LBUTTONDOWN:
        # extract channels from the image
        blue = image[x, y, 0]
        green = image[x, y, 1]
        red = image[x, y, 2]

        cv2.circle(image, (x, y), 2, (0, 0, 255), -1)
        myColorImage = np.zeros((512, 512, 3), np.uint8)  # new black image
        myColorImage[:] = [blue, green, red]  # fill the black image with selected color on the point
        cv2.imshow('color', myColorImage)  # show color in new window


# image = np.zeros((512, 512, 3), np.uint8)
image = cv2.imread('../images/lena.jpg')
cv2.imshow('image', image)
points = []

cv2.setMouseCallback('image', clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()
