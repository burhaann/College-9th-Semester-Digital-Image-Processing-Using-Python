import cv2

# Load the image
image = cv2.imread('image.jpg')  # Replace with your image file path

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Define the new width and height
    new_width = 400  # Adjust as needed
    new_height = 300  # Adjust as needed

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    # Display the resized image
    cv2.imshow('Resized Image', resized_image)
    
    # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
