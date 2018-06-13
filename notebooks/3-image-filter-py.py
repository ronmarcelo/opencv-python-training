
# coding: utf-8

# In[7]:


import cv2
import numpy as np

def apply_invert(frame):
    return cv2.bitwise_not(frame)

def apply_sepia(frame, intensity=0.5):
    blue, green, red = 20, 66, 112
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    frame_height, frame_width, frame_channel = frame.shape
    sepia_bgra = (blue, green, red, 1)
    overlay = np.full((frame_height, frame_width, 4), sepia_bgra, dtype='uint8')
    frame = cv2.addWeighted(overlay,intensity, frame, 1.0,0)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    return frame

def apply_sepia2(frame, intensity=0.5):
    blue, green, red = 255, 246, 255
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    frame_height, frame_width, frame_channel = frame.shape
    sepia_bgra = (blue, green, red, 1)
    overlay = np.full((frame_height, frame_width, 4), sepia_bgra, dtype='uint8')
    frame = cv2.addWeighted(overlay,intensity, frame, 1.0,0)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    return frame


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    invert = apply_invert(frame)
    sepia = apply_sepia(frame)
    sepia2 = apply_sepia2(frame)
    
    cv2.imshow('frame', frame)
    cv2.imshow('invert', invert)
    cv2.imshow('sepia',sepia)
    cv2.imshow('sepia2',sepia2)
    
    k = cv2.waitKey(1)
    
    if k == ord('q') or k == 27:
        cap.release()
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()

