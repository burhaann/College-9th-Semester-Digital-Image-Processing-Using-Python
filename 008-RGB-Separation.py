import cv2

# Load the color image
image = cv2.imread('rgb.jpg')  # Replace with your image file path

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Split the image into Red, Green, and Blue channels
    blue_channel, green_channel, red_channel = cv2.split(image)

    # Display the individual color channels
    cv2.imshow('Original Image', image)

    cv2.imshow('Red Channel', red_channel)
    cv2.imshow('Green Channel', green_channel)
    cv2.imshow('Blue Channel', blue_channel)

    # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
