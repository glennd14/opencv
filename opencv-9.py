# AIM: to make region of interest using the mouse
# mouse is dragged from one point to another ,the area covered by mouse(ROI), is shown in a separate window

import cv2
              
width=640
height=360
mycam=cv2.VideoCapture(0)

mycam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
mycam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
mycam.set(cv2.CAP_PROP_FPS,30)

#here we set evt to zero bcoz inside the while if we have not done any mouse click ,then there will be no event<
#and when we check for evt==4, program wont know what to do.
evt=0
def mouseClick(event,xpos,ypos,ignore1,ignore2):
     global evt,rowstart,columnstart,rowend,columnend
     if event==cv2.EVENT_LBUTTONDOWN :
        print("leftbutton down value: ",event)
        print("xpos,ypos: ",xpos,ypos)
        evt=event
        rowstart=xpos
        columnstart=ypos

     if event==cv2.EVENT_LBUTTONUP :
        print("leftbutton up value: ",event)
        print("xpos,ypos: ",xpos,ypos)    
        evt=event
        rowend=xpos
        columnend=ypos
     # this is when we move the mouse from bottom left to top right   
     if rowstart>rowend and columnstart>columnend :
          rowstart,rowend=rowend,rowstart
          columnstart,columnend=columnend,columnstart 
   

cv2.namedWindow('mainWindow')
cv2.setMouseCallback('mainWindow',mouseClick)

while True:
     ignore,frame=mycam.read()
     
     
     if evt == 4:
          cv2.rectangle(frame,(rowstart,columnstart),(rowend,columnend),(255,0,0),2)
          ROIframe= frame[columnstart:columnend,rowstart:rowend]
          cv2.imshow('ROIframe',ROIframe)
          cv2.moveWindow('ROIframe',650,0)
     
     
     cv2.imshow('mainWindow',frame)
     cv2.moveWindow('mainWindow',0,0)
     
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break
