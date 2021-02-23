## We will now track the number of black balls
## in a video, similar to the previous script in which
## we recognized the number of footballs in an image !!!

import cv2

# Access video from a file
# video is a bunch of images, press "space" to go to next frame!
# put a white line in a row of a video!
vs = cv2.VideoCapture('/Users/konstantinosgyftodimos/Documents/OpenCV_Projects/Images and Figures/live_video_balls_recognition.mp4')


while True:
    grabbed, frame = vs.read()
    if grabbed == False:
        print('end of video!!!')
    else:
        #play normal input video!
        cv2.imshow('input video', frame)
        cv2.waitKey(1)
        #play grayscale video!
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('grayscale video', gray)
        cv2.waitKey(1)
        #play blurred video!
        blurred = cv2.GaussianBlur(frame, (25, 25), None, )
        cv2.imshow('blurred version', blurred)
        cv2.waitKey(1)
        #play video with simple threshold!
        ret, thresh1 = cv2.threshold(blurred, 25, 255, cv2.THRESH_BINARY_INV)
        cv2.imshow('Simple Threshold', thresh1)
        cv2.waitKey(1)
        # #find contours
        # contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # #draw contours
        # cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
        # cv2.imshow('Draw Contours', frame)
        # cv2.waitKey(1)
