import cv2
import numpy as np

# Create a sample 2-D data (a 2-D NumPy array)
data = np.array([[128, 64, 192],
                 [32, 255, 0],
                 [0, 128, 64]], dtype=np.uint8)

# Define the file path and format (e.g., 'output_image.png')
output_file = 'output_image.png'

# Save the 2-D data as an image
cv2.imwrite(output_file, data)

print(f"Image saved to {output_file}")

