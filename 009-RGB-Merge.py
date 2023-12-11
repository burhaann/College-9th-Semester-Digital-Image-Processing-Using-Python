import cv2
import numpy as np

# Read the color image from a file
image = cv2.imread('rgb.jpg')

# Split the color image into its R, G, and B channels
blue_channel, green_channel, red_channel = cv2.split(image)

# Display the individual color channels
# cv2.imshow('Red Channel', red_channel)
# cv2.imshow('Green Channel', green_channel)
# cv2.imshow('Blue Channel', blue_channel)

# Generate the color image by merging the R, G, and B channels
color_image = cv2.merge([blue_channel, green_channel, red_channel])

# Display the color image
cv2.imshow('Color Image', color_image)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()