#AIM: to display rectangle and put a text on the video
import cv2

width=640
height=360
mycam=cv2.VideoCapture(0)

mycam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
mycam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
mycam.set(cv2.CAP_PROP_FPS,30)

topLeft=(160,70)
bottomRight=(450,300)
Ccolor= (0,255,0)
thickness=1


while True:
    flag,frame=mycam.read()
    cv2.rectangle(frame,topLeft,bottomRight,Ccolor,thickness)
    cv2.putText(frame,"hello world",(120,60),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2)
 
    cv2.imshow('my_cam',frame)
    cv2.moveWindow('my_cam',0,0)
    
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break


