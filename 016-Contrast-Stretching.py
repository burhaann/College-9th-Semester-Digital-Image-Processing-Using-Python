import cv2
import numpy as np

# Load the grayscale image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Define the minimum and maximum pixel values for stretching
    min_pixel_value = 50  # Adjust as needed
    max_pixel_value = 200  # Adjust as needed

    # Perform contrast stretching
    stretched_image = np.uint8(np.clip((image - min_pixel_value) * (255.0 / (max_pixel_value - min_pixel_value)), 0, 255))

    # Display the original and stretched images
    cv2.imshow('Original Image', image)
    cv2.imshow('Contrast-Stretched Image', stretched_image)

    # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
