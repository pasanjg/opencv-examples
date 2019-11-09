import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
Uses multi-stage algorithm to detect a wide range of edges in images
    *Noise reduction - Gaussian filter
    *Gradient calculation
    *Apply non-maximum suppression
    *Double threshold - determine potential edges
    *Edge tracking by Hysteresis - finalize the detection of edges by suppressing all other weak or not connected edges
"""

# image = cv2.imread('../images/messi5.jpg', 0)
image = cv2.imread('../images/lena.jpg', 0)
canny = cv2.Canny(image, 100, 200)

titles = ['Image', 'Canny']
images = [image, canny]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    # plt.xticks([]), plt.yticks([])

plt.show()
