#AIM: to learn about trackbars

import cv2

width=640
height=360
mycam=cv2.VideoCapture(0)

mycam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
mycam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
mycam.set(cv2.CAP_PROP_FPS,30)

#giving initial values to the parameters
xpos=int(width/2) #we are converting to int bcoz ,circle function expects an integer input
ypos=int(height/2)
myRad=3
thick=1

#the below f'ns are invoked only when we interact with the trackbars,at the beginning when there is no
#interaction we need to set inital values.

def trackfunc1(val):
    global xpos
    xpos=val
def trackfunc2(val):
    global ypos
    ypos=val
def trackfunc3(val):
    global myRad
    myRad=val
def trackfunc4(val):
    global thick
    thick=val    

cv2.namedWindow('my trackbars')        
cv2.createTrackbar('xpos','my trackbars',0,500,trackfunc1)
cv2.createTrackbar('ypos','my trackbars',0,500,trackfunc2)
cv2.createTrackbar('radius','my trackbars',0,500,trackfunc3)
cv2.createTrackbar('thickness','my trackbars',0,500,trackfunc4)

while True:
    ignore,frame=mycam.read()
    cv2.circle(frame,(xpos,ypos),myRad,(255,0,0),thick)
    cv2.resizeWindow('my trackbars',400,100)
    cv2.moveWindow('my trackbars',width,0)
    
    
    cv2.imshow('my window',frame)
    cv2.moveWindow('my window',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
         break