import cv2
import numpy as np

image = cv2.imread('../images/shapes.jpg')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find threshold
_, threshold = cv2.threshold(imageGray, 240, 255, cv2.THRESH_BINARY)

# find contours
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# iterate over all the contours
for contour in contours:
    # approximates polygonal curves with a specific precision
    # arcLength() calculates a contour's perimeter
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(image, [approx], 0, (0, 0, 0), 3)  # draw contours on the original image
    # display the shape name
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5  # offset for y coordinate

    if len(approx) == 3:
        cv2.putText(image, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 4:
        x1, y1, w, h = cv2.boundingRect(approx)  # get coordinates and the width and height
        aspectRatio = float(w)/h

        if 0.95 <= aspectRatio <= 1.05:  # if the aspect ratio is in between ... (Not an ideal situation)
            cv2.putText(image, "Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(image, "Rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 5:
        cv2.putText(image, "Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 10:
        cv2.putText(image, "Star", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    else:
        cv2.putText(image, "Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

cv2.imshow('Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
