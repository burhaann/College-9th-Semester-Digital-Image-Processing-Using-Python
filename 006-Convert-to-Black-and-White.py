import cv2

# Load the color or grayscale image
image = cv2.imread('image.jpg')  # Replace with your image file path

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Convert the image to grayscale if it's a color image
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to create a binary black and white image
    _, black_and_white_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

    # Display the original and black & white images
    cv2.imshow('Original Image', image)
    cv2.imshow('Black & White Image', black_and_white_image)

    # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
