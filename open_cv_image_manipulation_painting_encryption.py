# In this script i will put a hidden message inside
# Mona lisa (encrypt it) and then decrypt it !!!!!!

import cv2
import numpy as np
import random

## IMPORT MONA LISA IMAGE

# - cv2.imread
# we get 3 values RGB for every pixel in a row
image = cv2.imread('/Users/konstantinosgyftodimos/Documents/OpenCV - Projects/Images and Figures/monalisa.png')
print(image)

# show actual image
# - cv2.imshow
# and tell how long its going to show the image
# - cv2.waitkey
cv2.imshow('output',image)
cv2.waitKey(2000) # in miliseconds, if i put "-1" it stays open!

# turn image to grayscale and output it
# cv2.cvtColor
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray)
cv2.imshow('output',gray)
cv2.waitKey(2000)

## CREATE IMAGES, GRAYSCALE, COLORED, BINARY

# Create an image with zero values with numpy
image = np.zeros((100, 100), dtype='uint8')
print(image)
cv2.imshow('output', image)
cv2.waitKey(2000)

# GRAYSCALE: Put random values in the created gray image
for row in range(100):
    for col in range(100):
        number = int(random.random() * 255)
        print(row, col, number)
        image[row][col] = number

cv2.imshow('output', image)
cv2.waitKey(2000)

# COLORED: Create another image and put RGB color values
image = np.zeros((100, 100, 3), dtype='uint8')

for row in range(100):
    for col in range(100):
        red = int(random.random() * 255)
        green = int(random.random() * 255)
        blue = int(random.random() * 255)
        image[row][col] = [red, green, blue]

cv2.imshow('output', image)
cv2.waitKey(2000)

# BINARY: Create Binary Image either completelly black: 0 or completelly white: 255
image = np.zeros((100, 100), dtype='uint8')

for row in range(100):
    for col in range(100):
        white_or_black= int(random.choice([0, 255]))
        image[row][col] = white_or_black

cv2.imshow('output', image)
cv2.waitKey(2000)

## ENCODING A SECRET MESSAGE IN THE MONA LISA PAINTING

image = cv2.imread('/Users/konstantinosgyftodimos/Documents/OpenCV - Projects/Images and Figures/monalisa.png')
cv2.imshow('input',image)
cv2.waitKey(2000)

#row 501 of the image
row = image[501]
print(row)

#hidden message
message = 'Coffee Nisos Gia Ena Psema' * 3
#print(message)

#ord command gives a number for each character
column_count = 0
for character in message:
    #print(character,ord(character))
    image[501][column_count]=[ord(character),ord(character),ord(character)]
    column_count = column_count + 1
print(image[501])
#now i can see the original row and the updated (encrypted) row

cv2.imshow('output',image)
cv2.waitKey(2000)

#save the image with cv2.imwrite :)
cv2.imwrite('/Users/konstantinosgyftodimos/Documents/OpenCV - Projects/Images and Figures/our_little_secret.png', image)


## DECODE THE ENCODED MESSAGE
#
# image = cv2.imread('/Users/konstantinosgyftodimos/Documents/pythonProject/Images and Figures/monalisa.png')
# cv2.imshow('input',image)
# cv2.waitKey(2000)
#
# message = ''
# print(image[501])
# for col in image [501]:
#   message = message + chr(col[0])
#
# print(message)
