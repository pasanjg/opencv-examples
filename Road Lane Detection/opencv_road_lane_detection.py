import cv2
from matplotlib import pyplot as plt
import numpy as np


# defining the function to mask the region of interest
# input the src image and the vertices, it will return masked image
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)  # blank matrix that matched the src image
    # channel_count = img.shape[2]  # retrieve the no. of color channels of the src image [2] gives the channel count
    # match_mask_color = (255,) * channel_count  # create a match color with the same color channel counts
    match_mask_color = 255  # no need to use channel count if a grayscale image is used
    cv2.fillPoly(mask, vertices, match_mask_color)  # fill inside the polygon. Mask everything except the ROI
    masked_image = cv2.bitwise_and(img, mask)  # create an image with AND operator where the mask matches
    return masked_image


# defining the function to draw the lines on the image
# input the src image and the line vectors, it will draw the lines on the src image
def draw_lines(img, lines):
    img = np.copy(img)  # reassigning the copied image to the same variable
    # create a blank image of the original img size. [0] - width, [1] - height, 3 - no. of channels
    line_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    # loop around the line vectors to draw all the lines
    for line in lines:  # line give 4 parameters - (x, y) of first point and second point (x1, y1, x2, y2)
        for x1, y1, x2, y2 in line:
            # draw lines on the blank image to merge in the original image
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=4)

    # merge the lines to the original image
    img = cv2.addWeighted(img, 0.8, line_image, 1, 0.0)

    return img


# defining the function to return the processed result of lane detection
# input the frame to the function, it returns the detected lanes of the frame
def process(image):
    # read image from file system
    # image = cv2.imread('../images/road.png')
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # get the size of the image
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]

    # defining the 3 points required for the region of interest (ROI)
    # Note: pyplot marks the y axis starting from top to bottom (0, 0) is at the top left
    region_of_interest_vertices = [
        (0, height),
        (width / 2, height / 1.3),
        (width, height)
    ]

    # Canny edge must be detected before creating the cropped image. Otherwise, it will detect the mask edge also
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 120)

    # create the masked image with the canny image
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

    # returns the line vector of all the lines detected inside the cropped image
    detected_lines = cv2.HoughLinesP(cropped_image, rho=2, theta=np.pi / 60, threshold=50, lines=np.array([]),
                                     minLineLength=40, maxLineGap=100)

    image_with_lines = draw_lines(image, detected_lines)

    # display the cropped image with detected edges
    # plt.imshow(image_with_lines)
    # plt.show()

    return image_with_lines


cap = cv2.VideoCapture('../videos/road.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
