import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread('../images/road.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# get the size of the image
print(image.shape)
height = image.shape[0]
width = image.shape[1]

# defining the 3 points required for the region of interest (ROI)
# Note: pyplot marks the y axis starting from top to bottom (0, 0) is at the top left
region_of_interest_vertices = [
    (0, height),
    (width / 2, height / 2),
    (width, height)
]


# defining the function to mask the region of interest
# given the 'src image and the vertices, it will return masked image
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)  # blank matrix that matched the src
    channel_count = img.shape[2]  # retrieve the no. of color channels of the src image [2] gives the channel count
    match_mask_color = (255,) * channel_count  # create a match color with the same color channel counts
    cv2.fillPoly(mask, vertices, match_mask_color)  # fill inside the polygon. Mask everything except the ROI
    masked_image = cv2.bitwise_and(img, mask)  # create an image with AND operator where the mask matches
    return masked_image


# create the masked image
cropped_image = region_of_interest(image, np.array([region_of_interest_vertices], np.int32))

plt.imshow(cropped_image)
plt.show()
