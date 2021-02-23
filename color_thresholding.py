## In this script color thresholding takes place, where we want to find how many BLUE balls exist in the picture!

import cv2

# Import and Preview Image with BLUE balls
image = cv2.imread('/Users/konstantinosgyftodimos/Documents/OpenCV_Projects/Images and Figures/threshold_red_ball.png')
print(image)
mean_value = cv2.mean(image)
print(mean_value)

lab_image = cv2.cvtColor(image,cv2.COLOR_BGR2Lab)
lab_value = cv2.mean(lab_image)
print(lab_value)

# Import and Preview Image with ALL balls
image = cv2.imread('/Users/konstantinosgyftodimos/Documents/OpenCV_Projects/Images and Figures/threshold_color_balls.jpg')
cv2.imshow('input image',image)
cv2.waitKey(-1)

# This time we are not removing the color, but we are adding blurr
blurred = cv2.GaussianBlur(image, (15,15), None, )
cv2.imshow('blurred version', blurred)
cv2.waitKey(-1)

# inRange creates a binary image in a range (similar to threshold but in a range)
# Remember we want the blue balls ;)

# blue ball should become white and everything else should become black
binary=cv2.inRange(blurred, (165, 0, 0), (255, 175, 155))
cv2.imshow('output',binary)
cv2.waitKey(-1)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('There are:', len(contours), 'Blue Balls in the image')

# Draw Contours, Draw around the Footballs and number them!
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow('Draw Contours', image)
cv2.waitKey(-1)

