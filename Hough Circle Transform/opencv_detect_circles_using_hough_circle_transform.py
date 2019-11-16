import cv2
import numpy as np

# image = cv2.imread('../images/smarties.png')
image = cv2.imread('../images/shapes.jpg')
output = image.copy()
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert to grayscale

image_gray = cv2.medianBlur(image_gray, 5)  # create a blurred image

# apply HoughCircles method to detect circles
circles = cv2.HoughCircles(image_gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

# convert the detected circles into an integer (to get the center coordinates and radius)
detected_circles = np.uint16(np.around(circles))

# loop through the detections
for (x, y, r) in detected_circles[0, :]:
    cv2.circle(output, (x, y), r, (0, 255, 0), 3)  # draw a circle on the output image
    cv2.circle(output, (x, y), 2, (0, 255, 255), 3)  # mark a dot at the center (radius: 2)

cv2.imshow('Circles', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
