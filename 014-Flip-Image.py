import cv2

# Load the image
image = cv2.imread('image.jpg')

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Flip the image both horizontally and vertically
    flipped_image = cv2.flip(image, -1)  # -1 flips both horizontally and vertically

    # Display the original and flipped images
    cv2.imshow('Original Image', image)
    cv2.imshow('Flipped Image', flipped_image)

    # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
