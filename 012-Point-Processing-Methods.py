import cv2
import numpy as np

# Load the image
image = cv2.imread('image.jpg')

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Adjust Brightness
    brightness_factor = 50  # Positive for brighter, negative for darker
    brightened_image = cv2.convertScaleAbs(image, beta=brightness_factor)

    # Contrast Stretching
    min_pixel_value = 50
    max_pixel_value = 200
    contrast_stretched_image = np.uint8(np.clip((image - min_pixel_value) * (255.0 / (max_pixel_value - min_pixel_value)), 0, 255))

    # Invert Colors
    inverted_image = cv2.bitwise_not(image)

    # Display the original, brightened, contrast-stretched, and inverted images
    cv2.imshow('Original Image', image)
    cv2.imshow('Brightened Image', brightened_image)
    cv2.imshow('Contrast-Stretched Image', contrast_stretched_image)
    cv2.imshow('Inverted Image', inverted_image)

    # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
