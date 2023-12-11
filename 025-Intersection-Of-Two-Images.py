import cv2
import numpy as np

# Load the two binary images you want to find the intersection of
image1 = cv2.imread('black-white-1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('black-white-2.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the images were successfully loaded
if image1 is None or image2 is None:
    print("Error: Could not open or find the images.")
else:
    # Ensure both images have the same dimensions
    if image1.shape == image2.shape:
        # Calculate the intersection using bitwise AND
        intersection = cv2.bitwise_and(image1, image2)

        # Display the original images and the intersection result
        cv2.imshow('Image 1', image1)
        cv2.imshow('Image 2', image2)
        cv2.imshow('Intersection Result', intersection)

        # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
        cv2.waitKey(0)

        # Close all OpenCV windows
        cv2.destroyAllWindows()
    else:
        print("Error: Image dimensions do not match.")
