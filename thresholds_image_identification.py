## We have a picture and need to track how many specific footballs
## exist in a random image. Do: Image Blur / Build a binary image.
## Then do Thresholding:
## - simple thresholding
## - adaptive thresholding
## - Otzu Thresholding
## - InRange
## - Canny

import cv2

# Import and Preview Image
image = cv2.imread('/Users/konstantinosgyftodimos/Documents/OpenCV_Projects/Images and Figures/footballs.jpeg')
cv2.imshow('input image',image)
cv2.waitKey(-1)

# Convert to GrayScale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale version',gray)
cv2.waitKey(-1)

# Apply Gaussian Blur kernel - (11x11) to GrayScale Image
blurred = cv2.GaussianBlur(gray, (11,11), None, )
cv2.imshow('blurred version', blurred)
cv2.waitKey(-1)

# Simple Threshold: Make White backround into Black
ret, thresh1 = cv2.threshold(blurred, 235, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Simple Threshold', thresh1)
cv2.waitKey(-1)

# Adaptive Threshold: Same, but it doesnt need to give input number and play with it
thresh2 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
cv2.imshow('Adaptive Threshold', thresh2)
cv2.waitKey(-1)

# Find Contours, Find how many White Footballs exist in the Black image
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('There are:', len(contours), 'footballs in the image')

# Draw Contours, Draw around the Footballs and number them!
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow('Draw Contours', image)
cv2.waitKey(-1)
