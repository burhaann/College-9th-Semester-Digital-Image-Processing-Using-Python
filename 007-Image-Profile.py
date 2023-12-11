import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)  # Replace with your image file path

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Define the line position (horizontal or vertical)
    line_position = 100  # Adjust this value to your desired position

    # Draw the horizontal line profile
    horizontal_profile = image[line_position, :]

    # Draw the vertical line profile
    vertical_profile = image[:, line_position]

    # Create a figure and plot the profiles
    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    plt.title('Horizontal Line Profile')
    plt.plot(horizontal_profile)
    
    plt.subplot(122)
    plt.title('Vertical Line Profile')
    plt.plot(vertical_profile)

    # Show the plots
    plt.tight_layout()
    plt.show()
