import cv2
import numpy as np

img = cv2.imread('../images/lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)  # gives a black image of 512x512

img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)  # draw line
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 5)

img = cv2.rectangle(img, (384, 100), (510, 128), (0, 255, 0), -1)  # -1 thickness will fill the rectangle
img = cv2.circle(img, (300, 458), 50, (100, 20, 45), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10, 500), font, 2, (0, 255, 255), 2, cv2.LINE_AA)  # write text

cv2.imshow('image', img)  # display image

cv2.waitKey(0)
cv2.destroyAllWindows()
