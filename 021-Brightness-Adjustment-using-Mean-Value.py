import cv2
import numpy as np

# Load the image
image = cv2.imread('image.jpg')

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Define the target mean value (brightness level)
    target_mean = 150*2  # You can adjust this value

    # Calculate the current mean value
    current_mean = np.mean(image)

    # Calculate the adjustment factor to achieve the target mean
    adjustment_factor = target_mean / current_mean

    # Adjust the brightness by scaling the image with the adjustment factor
    adjusted_image = np.clip(image * adjustment_factor, 0, 255).astype(np.uint8)

    # Display the original and adjusted images
    cv2.imshow('Original Image', image)
    cv2.imshow('Adjusted Image', adjusted_image)

    # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
