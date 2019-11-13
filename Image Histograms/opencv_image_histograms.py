import numpy as np
import cv2
from matplotlib import pyplot as plt

# histogram - a graph which gives the overall intensity distribution of the image

# histogram with black, black and white, black white and gray images
imageBLACK = np.zeros((200, 200), np.uint8)  # black image
cv2.rectangle(imageBLACK, (0, 100), (200, 200), (255), -1)  # add a white rectangle to the image
cv2.rectangle(imageBLACK, (0, 50), (100, 100), (127), -1)  # add another rectangle to the image

plt.hist(imageBLACK.ravel(), 256, [0, 256])
plt.show()

# get BGR histogram
imageBGR = cv2.imread('../images/lena.jpg')  # read image in BGR mode

# split BGR image into channels
b, g, r = cv2.split(imageBGR)

cv2.imshow('ImageBGR', imageBGR)
cv2.imshow('B', b)
cv2.imshow('G', g)
cv2.imshow('R', r)


# get the histogram using matplotlib
# X-axis: pixel count, Y-axis: intensity
plt.hist(imageBGR.ravel(), 256, [0, 256])
plt.show()

plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.show()


# get histogram using cv2 calcHist
imageGRAY = cv2.imread('../images/lena.jpg', 0)  # read image in grayscale mode

hist = cv2.calcHist([imageGRAY], [0], None, [256], [0, 256])
cv2.imshow('ImageGRAY', imageGRAY)
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
