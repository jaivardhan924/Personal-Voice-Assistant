import cv2              #to access the camera
import os
from camera import resize as rs;

def came():
    cap=cv2.VideoCapture(0)
    #0 for internal camera
    #1 for external camera

    while True:
        isTrue, frame = cap.read()
        #isTrue refers to that the frame is captured
        #imread() for picture
        #cv2.read(cap) -> 'cv2' has no attribute 'read'
        rframe=rs.resize(frame,2.0)

        f=cv2.flip(rframe,1)     
        # 0 for vertical flipping
        # 1 for horizantal flipping
        #-1 for both

        #cv2.imshow("camera",frame)

        cv2.imshow("REsized cam",f)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;

    cap.release()
    cv2.destroyAllWindows()

