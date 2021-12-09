
#AIM;color detection
#here we test for the color :blue
import cv2

evt=0
def mouseClick(event,xpos,ypos,flags,param):
    global x,y,evt
    if event==cv2.EVENT_LBUTTONDOWN:
        print(event)
        x=xpos
        y=ypos
        evt=event

cv2.namedWindow('my window')
cv2.setMouseCallback('my window',mouseClick)
#not sure
clr=(0,0,0)

while True:
    
    image=cv2.imread('images/images/BC.png')
   # image=cv2.resize(image,400,300)
    #HSV value range for these colors
    
    blueLower=(100,180,150)
    blueUpper=(110,220,255)

    yellowLower=(25,180,150)
    yellowUpper=(35,220,255)

    greenLower=(65,60,150)
    greenUpper=(75,75,255)

    frame=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    if evt==1:
      clr=frame[x][y]
      print(clr)
    
      if((clr[0]>blueLower[0] and clr[0]<=blueUpper[0]) and (clr[1]>blueLower[1] and clr[1] <= blueUpper[1])
      and (clr[2]>blueLower[2] and clr[2]<=blueUpper[2])):
            print("blue")
      else:
          print('none')      
      evt=0

    cv2.imshow('my window',image)
    cv2.moveWindow('my window',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
         break
