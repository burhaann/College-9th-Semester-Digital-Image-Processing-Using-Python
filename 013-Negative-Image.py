import cv2

# Load the image
image = cv2.imread('image.jpg')

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Obtain the negative image
    negative_image = cv2.bitwise_not(image)

    # Display the original and negative images
    cv2.imshow('Original Image', image)
    cv2.imshow('Negative Image', negative_image)

    # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
