import cv2
import numpy as np

# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture('../videos/vtest.avi')

ret, frame1 = capture.read()
ret, frame2 = capture.read()

while capture.isOpened():

    diff = cv2.absdiff(frame1, frame2)  # absolute difference between frame1 and frame 2
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # convert the frame to grayscale mode
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # gaussian blur the grayscale image
    _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)  # get the threshold
    dilated = cv2.dilate(threshold, None, iterations=3)  # dilate the threshold image to fill in all the holes
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # find out the contours

    # draw all the contours on the original frame
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)  # define the coordinates and width and height in each contour

        if cv2.contourArea(contour) < 900:  # neglect when area < 900
            continue

        # if the area in greater than 900, rectangle will appear around the moving object (contour)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Feed', frame1)
    frame1 = frame2
    ret, frame2 = capture.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
capture.release()
