#AIM: UNDERSTAND BGR AND HSV color space
import cv2
import numpy as np
width=640
height=360
mycam=cv2.VideoCapture(0)

mycam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
mycam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
mycam.set(cv2.CAP_PROP_FPS,30)

evt=0
def mouseClick(event,xpos,ypos,flag,params):
    global x,y,evt
    if event==cv2.EVENT_LBUTTONDOWN:
        print(event)
        x=xpos
        y=ypos
        evt=event
    if event==cv2.EVENT_LBUTTONUP:
        print(event)    

cv2.namedWindow('my window')
cv2.setMouseCallback('my window',mouseClick)

while True:
  ignore,frame= mycam.read()
  dummy=np.zeros([256,256,3],dtype=np.uint8)
 
  if evt==1:
   #this fetches the coordinate of the point where we clicked on the frame,
   #which is a tuple ,representing the colour
   clr= frame[x][y]
   #here we make our black image get the color 
   dummy[:,:]=clr
   cv2.imshow('dummy',dummy)
   cv2.moveWindow('dummy',width,0)
   print("BGR: ",clr)
   #evt==1 is for button down,hence once we release it ,it is no longer down. 
   #but we still want the 'if' to run,hence we make evt =0.
   evt=0

  cv2.imshow('my window',frame)
  cv2.moveWindow('my window',0,0)
  if cv2.waitKey(1) & 0xFF == ord('q'):
       break