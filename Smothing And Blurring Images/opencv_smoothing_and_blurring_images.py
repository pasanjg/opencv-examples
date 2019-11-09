import cv2
import numpy as np
from matplotlib import pyplot as plt

# image = cv2.imread('../images/opencv-logo.png')
# image = cv2.imread('../images/Halftone_Gaussian_Blur.jpg')
# image = cv2.imread('../images/Salt_and_Pepper_noise.png')
image = cv2.imread('../images/lena.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25

homogeneous = cv2.filter2D(image, -1, kernel)  # Homogeneous filter - 2D image
blur = cv2.blur(image, (5, 5))  # Averaging - average blur

# Gaussian Blur - removes the high frequency noise of the image
gblur = cv2.GaussianBlur(image, (5, 5), 0)

# Median Blur - replaces the each pixels value with the median of its neighbouring pixels (Salt and Pepper noise)
median = cv2.medianBlur(image, 5)  # kernel size must be an odd value (except 1; 1 shows the same image)

# Bilateral Filter - removes noise while keeping the edges sharp (preserve the edges)
bilateralFilter = cv2.bilateralFilter(image, 9, 75, 75)


titles = ['Image', '2D Convolution', 'Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [image, homogeneous, blur, gblur, median, bilateralFilter]


for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    # plt.xticks([]), plt.yticks([])


plt.show()
