import cv2              #to access the camera
import os

def resize(frame,scale):
    width=int(frame.shape[1]*scale) 
    height=int(frame.shape[0]*scale)
    # shape[1] refers to width
    # shape[0] refers to height

    dim=(width,height)

    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

