#AIM:to track 2 or more objects based on its colour

import cv2
import numpy as np

width=320
height=180
mycam=cv2.VideoCapture(0)

mycam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
mycam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
mycam.set(cv2.CAP_PROP_FPS,30)

def track1(val):
  global hueL1  
  hueL1=val
def track2(val):
  global hueU1  
  hueU1=val

def track1_1(val):
  global hueL2  
  hueL2=val
def track2_1(val):
  global hueU2  
  hueU2=val


def track3(val):
  global satL  
  satL=val    
def track4(val):
  global satU  
  satU=val
def track5(val):
  global valL 
  valL=val
def track6(val):
  global valU  
  valU=val  

hueL1=10
hueU1=10

hueL2=10
hueU2=10

satL=10
satU=10
valL=10
valU=10


cv2.namedWindow('my trackbars')
cv2.createTrackbar('hueL1','my trackbars',0,179,track1)
cv2.createTrackbar('hueU1','my trackbars',0,179,track2)

cv2.createTrackbar('hueL2','my trackbars',0,179,track1_1)
cv2.createTrackbar('hueU2','my trackbars',0,179,track2_1)

cv2.createTrackbar('satL','my trackbars',0,255,track3)
cv2.createTrackbar('satU','my trackbars',0,255,track4)
cv2.createTrackbar('valL','my trackbars',0,255,track5)
cv2.createTrackbar('valU','my trackbars',0,255,track6)

while True:
    ignore,frame=mycam.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    cv2.resizeWindow('my trackbars',500,300)
    cv2.moveWindow('my trackbars',width,0)

    lower_bound1=np.array([hueL1,satL,valL])
    upper_bound1=np.array([hueU1,satU,valU])
    
    mymaskA=cv2.inRange(hsv_frame,lower_bound1,upper_bound1)

    lower_bound2=np.array([hueL2,satL,valL])
    upper_bound2=np.array([hueU2,satU,valU])

    mymaskB=cv2.inRange(hsv_frame,lower_bound2,upper_bound2)
    
    actual_mask=cv2.add(mymaskA,mymaskB)
    cv2.resize(actual_mask,(300,400))
    cv2.imshow('actual_mask',actual_mask)
    cv2.moveWindow('actual_mask',0,height)

    cv2.imshow('my window',frame)
    cv2.moveWindow('my window',0,0)

    if cv2.waitKey(1) &0xff == ord('q'):
        break
     