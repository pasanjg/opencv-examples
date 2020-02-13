import numpy as np
import cv2 as cv

"""
Reusing the code from Meanshift example
Applies Meanshift, then updates the size of the window and rotation
"""

capture = cv.VideoCapture('../videos/slow_traffic_small.mp4')

"""
take the first frame of the video
"""
ret, frame = capture.read()

"""
setup initial location of the window
"""
x, y, width, height = 300, 200, 100, 50
track_window = (x, y, width, height)

"""
setup ROI for tracking
"""
roi = frame[y: y + height, x: x + width]

hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)  # convert the ROI to HSV

mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255)))  # discard low light values
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)  # normalize the values between 0 - 255

"""
setup  the termination criteria, either 10 iterations or move by at least 1 point
"""
term_criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
cv.imshow('ROI', roi)

while 1:
    ret, frame = capture.read()
    if ret:

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # gives the back projected image
        destination = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)  # channel starts from 0

        # apply mean shift to get the new location
        ret, track_window = cv.CamShift(destination, track_window, term_criteria)
        # print(ret)

        # Draw on image
        # x, y, w, h = track_window
        # final_image = cv.rectangle(frame, (x, y), (x + w, y + h), 255, 3)

        # Draw the rotating rectangle for the points
        pts = cv.boxPoints(ret)
        # print(pts)
        pts = np.int0(pts)
        final_image = cv.polylines(frame, [pts], True, (0, 255, 0), 2)

        cv.imshow('Back Projection', destination)
        cv.imshow('Final Image', final_image)

        key = cv.waitKey(30) & 0xFF

        if key == 27:
            break
    else:
        break
