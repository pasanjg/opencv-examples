import cv2
import numpy as np

"""
Harris Corner detection determines which corner produces very large variations when moved in
both X and Y directions
"""

image = cv2.imread('../images/chessboard.png')

cv2.imshow('Image', image)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_gray = np.float32(image_gray)  # convert to float32 before applying Corner Harris method

# blockSize is the size of neighboring pixels considered for detection
destination = cv2.cornerHarris(image_gray, 2, 3, 0.04)

# apply the dilation to get a better result
# increases the white region in the image (mask) or size of foreground object
destination = cv2.dilate(destination, None)

# color the detected window in red
image[destination > 0.01 * destination.max()] = [0, 0, 255]

cv2.imshow('Result', image)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
