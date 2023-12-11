import cv2

# Load the image
image = cv2.imread('image.jpg')

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Calculate the mean value
    mean_color = cv2.mean(image)

    # Extract the mean intensity for each channel (BGR in the case of a color image)
    mean_blue, mean_green, mean_red, _ = mean_color

    # Display the mean values
    print(f"Mean Blue: {mean_blue}")
    print(f"Mean Green: {mean_green}")
    print(f"Mean Red: {mean_red}")

    # Wait for a key press indefinitely or for a specific time (e.g., 3000 milliseconds)
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
