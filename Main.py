import cv2
import numpy as np
import Modules as m
import time
import autopy # MOuse Helper
# import tkinter as tk


width, height = 640, 480

detector = m.handDetector(maxHands=1)


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

cap.set(3,width) # 1920
cap.set(4,height) # 1080

# # Screen Resolution
# print("Width =", screen_width)
# print("Height =", screen_height)


previous_time = 0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Find Hands LandMark

    frame = detector.findHands(frame)
    landmarks_list, bbox = detector.findPosition(frame)

    print(landmarks_list)

    # Get tip of index finger and middle finger
    if len(landmarks_list)!=0:
        # index finger
        x1,y1 = landmarks_list[8][:1]
        # Middle finger
        x2,y2 = landmarks_list[12][:1]

        print(x1,y1,x2,y2)

    # check which finger is up

    # Check if index finger is in moving mode:

    # Convert Coordinates as per screen Resolution


    # Smoothen values to avoid flickkering

    # Move Mouse

    # CHeck if we are in clicking mode: then change to clicking mode.

    # find distance between fingers

    # click mouse if distance short

    # Frame rate:

    current_time = time.time()
    fps = 1 / (current_time - previous_time)

    previous_time = current_time

    cv2.putText(frame, str(int(fps)), (20,50), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)



    # Display
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
