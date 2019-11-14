import cv2
import numpy as np

# Template Matching - search a given sample inside another image

image = cv2.imread('../images/messi5.jpg')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

imageTemp = cv2.imread('../images/messi-face.jpg', 0)  # template image
w, h = imageTemp.shape[::-1]  # [::-1] get the row's and column's values in the reverse order (width and height)

# try different methods with different threshold values
# result = cv2.matchTemplate(imageGray, imageTemp, cv2.TM_CCOEFF_NORMED)  # result of matching the images
result = cv2.matchTemplate(imageGray, imageTemp, cv2.TM_CCORR_NORMED)  # result of matching the images
print(result)

# find the brighter (matching) points inside the matrix
threshold = 0.99  # result depends on the threshold and method
loc = np.where(result >= threshold)  # evaluate each and every value in result and return the matching ones
print(loc)

# loop across the loc
for pt in zip(*loc[::-1]):  # applicable for multiple meshed templates
    # draw a red rectangle around the match
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)  # (x, y, colour, thickness)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
