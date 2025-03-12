# Import the OpenCV library
import cv2

# Read the image file
image = cv2.imread('mustang.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform edge detection using the Canny algorithm
edges = cv2.Canny(gray_image, 100, 200)

# Resize the edges image to match the original image size
edges_resized = cv2.resize(edges, (image.shape[1], image.shape[0]))

# Display the original image
cv2.imshow('Original Image', image)

# Display the edge-detected image
cv2.imshow('Edge Detection', edges_resized)

# Wait for any key press to close the windows
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
