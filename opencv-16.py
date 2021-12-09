#AIM:understanding contours

import cv2
import numpy as np

width=320
height=180
mycam=cv2.VideoCapture(0)

mycam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
mycam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
mycam.set(cv2.CAP_PROP_FPS,30)

def track1(val):
  global hueL  
  hueL=val
def track2(val):
  global hueU  
  hueU=val
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

hueL=105
hueU=120
satL=46
satU=188
valL=170
valU=255


cv2.namedWindow('my trackbars')
cv2.createTrackbar('hueL','my trackbars',105,179,track1)
cv2.createTrackbar('hueU','my trackbars',120,179,track2)
cv2.createTrackbar('satL','my trackbars',46,255,track3)
cv2.createTrackbar('satU','my trackbars',188,255,track4)
cv2.createTrackbar('valL','my trackbars',170,255,track5)
cv2.createTrackbar('valU','my trackbars',255,255,track6)

while True:
    ignore,frame=mycam.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    cv2.resizeWindow('my trackbars',500,300)
    cv2.moveWindow('my trackbars',width+30,0)

    lower_bound=np.array([hueL,satL,valL])
    upper_bound=np.array([hueU,satU,valU])
    mymask=cv2.inRange(hsv_frame,lower_bound,upper_bound)

    #applying contours on the mask.
    contours,ignore=cv2.findContours(mymask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame,contours,-1,(0,0,255),3)
    for contour in contours:
      area=cv2.contourArea(contour)
      if area>200:
        #cv2.drawContours(frame,[contour],0,(0,0,255),3)
        x,y,w,h=cv2.boundingRect(contour) #return supper left corner,height,width of rectangle
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)


    
    my_small_mask=cv2.resize(mymask,(300,200))
    cv2.imshow('my_small_mask',my_small_mask)
    cv2.moveWindow('my_small_mask',0,height+100)
    
    myobject=cv2.bitwise_and(frame,frame,mask=mymask)

    my_small_object=cv2.resize(myobject,(300,200))
    cv2.imshow('my_small_object',my_small_object)
    cv2.moveWindow('my_small_object',305,height+100)

    cv2.imshow('my window',frame)
    cv2.moveWindow('my window',0,0)

    if cv2.waitKey(1) &0xff == ord('q'):
        break
     