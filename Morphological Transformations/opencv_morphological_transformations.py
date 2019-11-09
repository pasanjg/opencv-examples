import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
Operations based on the image shape
"""

image = cv2.imread('../images/smarties.png', cv2.IMREAD_GRAYSCALE)  # reading image in grayscale - 0
_, mask = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY_INV)  # binary image using a threshold

# 5x5 square shape to apply on the image
kernel = np.ones((5, 5), np.uint8)

# morphological transformation methods
dilation = cv2.dilate(mask, kernel, iterations=2)  # increases the white region in the image or size of foreground object
erosion = cv2.erode(mask, kernel, iterations=1)  # erodes away the boundaries of foreground object
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)  # erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  # Dilation followed by Erosion
morph_gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)  # the difference between dilation and erosion of an image
top_hat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)  # the difference between input image and Opening of the image

titles = ['Image', 'Mask', 'Dilation', 'Erosion', 'Opening', 'Closing', 'Gradient', 'TopHat']
images = [image, mask, dilation, erosion, opening, closing, morph_gradient, top_hat]

# plotting 8 images
for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')  # plot with 2 rows and 8 columns
    plt.title(titles[i])  # set titles
    # plt.xticks([]), plt.yticks([])  # remove the X and Y axes

plt.show()
