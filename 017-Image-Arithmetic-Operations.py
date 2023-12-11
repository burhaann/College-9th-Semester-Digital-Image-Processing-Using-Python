import cv2

# Load the images you want to use for arithmetic operations
image1 = cv2.imread('black-white-3.jpg')
image2 = cv2.imread('black-white-4.jpg')

# Check if the images were successfully loaded
if image1 is None or image2 is None:
    print("Error: Could not open or find the images.")
else:
    # Ensure both images have the same dimensions
    if image1.shape == image2.shape:
        # Perform pixel-wise addition
        add_result = cv2.add(image1, image2)

        # Perform pixel-wise subtraction
        subtract_result = cv2.subtract(image1, image2)

        # Perform pixel-wise multiplication
        multiply_result = cv2.multiply(image1, image2)

        # Perform pixel-wise division
        # Note: Avoid division by zero, and ensure the divisor image is not zero-valued
        divisor = cv2.divide(image1, image2, scale=255.0)
        
        # Display the original images and the results of addition, subtraction, multiplication, and division
        cv2.imshow('Image 1', image1)
        cv2.imshow('Image 2', image2)
        # cv2.imshow('Addition Result', add_result)
        cv2.imshow('Subtraction Result', subtract_result)
        # cv2.imshow('Multiplication Result', multiply_result)
        # cv2.imshow('Division Result', divisor)

        # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
        cv2.waitKey(0)

        # Close all OpenCV windows
        cv2.destroyAllWindows()
    else:
        print("Error: Image dimensions do not match.")
