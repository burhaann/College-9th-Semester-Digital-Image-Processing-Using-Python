import cv2

# Load the grayscale image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Define the threshold value (adjust as needed)
    threshold_value = 128

    # Perform binary thresholding
    _, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Display the original and thresholded images
    cv2.imshow('Original Image', image)
    cv2.imshow('Thresholded Image', thresholded_image)

    # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
