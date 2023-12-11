import cv2

# Load an image from file
image = cv2.imread('image.jpg')  # Replace 'your_image_file.jpg' with the actual file path

if image is not None:
    # Display the image
    cv2.imshow('Digital Image', image)
    
    # Wait for a key press indefinitely
    cv2.waitKey(0)
    
    # Close all OpenCV windows
    cv2.destroyAllWindows()
else:
    print("Image not found or cannot be loaded.")
