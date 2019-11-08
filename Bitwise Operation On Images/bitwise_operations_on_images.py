import cv2
import numpy as np

image1 = np.zeros((250, 500, 3), np.uint8)
image1 = cv2.rectangle(image1, (200, 0), (300, 100), (255, 255, 255), -1)
image2 = cv2.imread('../images/image_1.png')

'''
logical operators affecting images
    0 - black
    1 - white
'''

bitAnd = cv2.bitwise_and(image2, image1)
bitOr = cv2.bitwise_or(image2, image1)
bitXor = cv2.bitwise_xor(image2, image1)
bitNot = cv2.bitwise_not(image2, image1)

cv2.imshow('image1', image1)
cv2.imshow('image2', image2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot', bitNot)

cv2.waitKey(0)
cv2.destroyAllWindows()
