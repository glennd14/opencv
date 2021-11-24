#AIM: to analyse mouseclicks and draw a circle
import cv2
width=640
height=360
mycam=cv2.VideoCapture(0)

mycam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
mycam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
mycam.set(cv2.CAP_PROP_FPS,30)

evt=0
#job of this function is to identify the event and do the necessary action
#every event has a number assosciated to it ,eg :leftbutton clicked down is: 1
def mouseClick(event,xpos,ypos,ignore1,ignore2):
    #we are making these global because if we directly use event,xpos,ypos inside while ,it wont know that these 
    #variables even exist. this is because these variables are local to the function definition called mouseClick
    #therefore we use the keyword called 'global' to make them a global variable
    global evt,x,y
    

    if event==cv2.EVENT_LBUTTONDOWN:
        print("leftbutton down value:",event)
        print("xpos,ypos : ",xpos,ypos)
        evt=event
        x=xpos
        y=ypos
        
    if event==cv2.EVENT_RBUTTONUP:
        print("rightbutton up value:",event)
        print("xpos,ypos : ",xpos,ypos)
        evt=event
        x=xpos
        y=ypos
      

cv2.namedWindow('mycam')
#the  below function keeps looking for any activity on the specified window
#if any event is observed ,then the 'mouseclick' function is called 
cv2.setMouseCallback('mycam',mouseClick)

while True:
    ignore,frame=mycam.read()
    
    if evt==1:
     cv2.circle(frame,(x,y),15,(255,0,0),2)
    if evt==5:
     cv2.circle(frame,(x,y),15,(0,255,0),2)

    cv2.imshow('mycam',frame)
    cv2.moveWindow('mycam',0,0)

    if cv2.waitKey(1) &0xFF == ord('q'):
        break

