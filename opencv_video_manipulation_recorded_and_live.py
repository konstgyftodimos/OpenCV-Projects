## Take existing video, do manipulations and create a new video
## Manipulations: Put time-lapsed time in the video

import cv2
import numpy as np
import random
from datetime import datetime as dt

# # Access video from a file
# # video is a bunch of images, press "space" to go to next frame!
# # put a white line in a row of a video!
# vs = cv2.VideoCapture('/Users/konstantinosgyftodimos/Documents/OpenCV - Projects/Images and Figures/GH010365.MP4')
#
# while True:
#     grabbed, frame = vs.read()
#     if grabbed == False:
#         print('end of video!!!')
#     else:
#         # now put a white line  in the 100th row of the video
#         frame[100] = [155,155,155]
#         #frame[500] = [155,155,155]
#         cv2.imshow('output', frame)
#         cv2.waitKey(-1)

# Access to live camera and write a message!
vs = cv2.VideoCapture(0)

original_fps = int(vs.get(cv2.CAP_PROP_FPS))
original_width = int(vs.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(vs.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(original_fps, original_width, original_height)

# Record Live Video
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
writer = cv2.VideoWriter("/Users/konstantinosgyftodimos/Documents/OpenCV - Projects/Images and Figures/live_video.avi", fourcc, original_fps, (original_width, original_height), True)

start_time = dt.now()
print(start_time)

while True:
    grabbed, frame = vs.read()
    now_time = dt.now()
    if grabbed == False:
        print('end of video!!!')
    else:
        delta_time = str((now_time - start_time).total_seconds())
        print(delta_time)
        message = delta_time + ".. seconds have elapsed"
        cv2.putText(frame, message, (30,30),cv2.FONT_HERSHEY_COMPLEX, 1, (1, 255, 1),1)
        cv2.imshow('output', frame)
        cv2.waitKey(1)
        writer.write(frame)
