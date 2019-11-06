import cv2

img = cv2.imread('lena.jpg', -1)  # read image

print(img)

cv2.imshow('image', img)  # display image in new window
key = cv2.waitKey(0) & 0xFF  # add a delay to window. 0 - window will not disappear unless closed

if key == 27:  # press 'Esc' to exit without saving
    cv2.destroyAllWindows()  # close all windows
elif key == ord('s'):  # press 's' to save and exit
    cv2.imwrite('lena-copy.png', img)  # write image to new file
    cv2.destroyAllWindows()
