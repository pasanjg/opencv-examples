import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('../images/messi5.jpg', 0)  # 0 - read image in grayscale
# image = cv2.imread('../images/sudoku.png', 0)  # 0 - read image in grayscale

# Gradient methods
# Laplacian gradient
lap = cv2.Laplacian(image, cv2.CV_64F, ksize=3)  # CV_64F - 64bit float, supports the negative numbers
lap = np.uint8(np.absolute(lap))  # convert into an unsigned int

# Sobel Gradient
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
canny = cv2.Canny(image, 100, 200)

# convert to an unsigned int
sobelX = np.uint8(np.absolute(np.absolute(sobelX)))
sobelY = np.uint8(np.absolute(np.absolute(sobelY)))

# combine X and Y
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['Image', 'Laplacian', 'SobelX', 'SobelY', 'Sobel Combined', 'Canny']
images = [image, lap, sobelX, sobelY, sobelCombined, canny]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    # plt.xticks([]), plt.yticks([])

plt.show()
