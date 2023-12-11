import cv2

# Load the color image
color_image = cv2.imread('image.jpg')  # Replace with your image file path

# Check if the image was successfully loaded
if color_image is None:
    print("Error: Could not open or find the image.")
else:
    # Convert the color image to grayscale
    grayscale_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    # Convert the color image to HSV
    hsv_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)

    # Convert the color image to LAB
    lab_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2LAB)

    # Display the original, grayscale, HSV, and LAB images
    cv2.imshow('Original Image', color_image)
    cv2.imshow('Grayscale Image', grayscale_image)
    cv2.imshow('HSV Image', hsv_image)
    cv2.imshow('LAB Image', lab_image)

    # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
