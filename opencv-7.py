import cv2
import time


width=640
height=360
mycam=cv2.VideoCapture(0)

mycam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
mycam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
mycam.set(cv2.CAP_PROP_FPS,30)

while True:
    ignore,frame=mycam.read()

    ROIframe=frame[150:210,280:370]
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)

    frame[150:210,280:370]=ROIframe
    #for camera feed
    cv2.imshow('my_cam',frame)
    cv2.moveWindow('my_cam',0,0)
    
    #to make the slice move from one end to the other
    cv2.imshow('frame',frame[150:210,280:370])
    cv2.moveWindow('frame',0,0)
    time.sleep(6)    

    cv2.imshow('frame',frame[150:210,280:370])
    cv2.moveWindow('frame',580,0)
    time.sleep(6)    

    cv2.imshow('frame',frame[150:210,280:370])
    cv2.moveWindow('frame',0,280)
    time.sleep(6)    

    cv2.imshow('frame',frame[150:210,280:370])
    cv2.moveWindow('frame',580,280)
    time.sleep(6)    

        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    