import numpy as np
import cv2 as cv

#  Background Subtraction - Generates the foreground mask of a moving object in a static scene (still camera)
# i.e. The binary image containing the pixels belonging to the moving objects

capture = cv.VideoCapture('../videos/vtest.avi')
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))

# gaussian mixture based background and foreground segmentation algorithm
# fgbg = cv.bgsegm.createBackgroundSubtractorMOG()  # not working in OpenCV 4.x

# fgbg = cv.createBackgroundSubtractorMOG2()  # other option
fgbg = cv.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=False)  # with noise reduced

# combines statistical background image estimation and pre pixel biasing
# fgbg = cv.createBackgroundSubtractorGMG()  # not working with OpenCV 4.x

# fgbg = cv.createBackgroundSubtractorKNN(detectShadows=False)

while True:
    ret, frame = capture.read()
    if frame is None:
        break

    fgMask = fgbg.apply(frame)  # create the foreground mask by applying the subtractor

    # To get the better results with reduced noise
    # fgMask = cv.morphologyEx(fgMask, cv.MORPH_OPEN, kernel) # required for GMG method

    cv.imshow('Video', frame)
    cv.imshow('Video Mask', fgMask)

    key = cv.waitKey(30)
    if key == 'q' or key == 27:
        break

capture.release()
cv.destroyAllWindows()
