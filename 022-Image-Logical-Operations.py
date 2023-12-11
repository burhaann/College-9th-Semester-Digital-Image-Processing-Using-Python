import cv2
import numpy as np

# Load two images of the same size
image1 = cv2.imread('black-white-1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('black-white-3.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the images were successfully loaded
if image1 is None or image2 is None:
    print("Error: Could not open or find the images.")
else:
    # Perform bitwise AND operation
    and_result = cv2.bitwise_and(image1, image2)

    # Perform bitwise OR operation
    or_result = cv2.bitwise_or(image1, image2)

    # Perform bitwise XOR operation
    xor_result = cv2.bitwise_xor(image1, image2)

    # Perform bitwise NOT operation on the first image
    not_result = cv2.bitwise_not(image1)

    # Display the original images and the results of logical operations
    cv2.imshow('Image 1', image1)
    cv2.imshow('Image 2', image2)
    # cv2.imshow('AND Result', and_result)
    cv2.imshow('OR Result', or_result)
    # cv2.imshow('XOR Result', xor_result)
    # cv2.imshow('NOT Result (Image 1)', not_result)

    # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
