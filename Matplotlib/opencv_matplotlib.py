import cv2
from matplotlib import pyplot as plt

image = cv2.imread('../images/lena.jpg')
cv2.imshow('image', image)

# by default opencv reads the image in BGR format and matplotlib reads the image in RGB format
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.xticks([]), plt.yticks([])  # hides the X and Y axes
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
