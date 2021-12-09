#AIM : to display the - hue and saturation,hue and value 
# hue: left ot right,, saturation,value: top to bottom 
import cv2
import numpy as np

dummy=np.zeros([256,180,3],dtype=np.uint8)
dummy2=dummy
# hue and saturation
for i in range(0,255,1):
    for j in range (0,180,1):
        dummy[i][j]=(j,i,255)
# right now dummy is a HSV image
# but for the pc to interpret the colors ,we need BGR:
dummy=cv2.cvtColor(dummy,cv2.COLOR_HSV2BGR)

# hue and value
for i in range(0,255,1):
    for j in range (0,180,1):
        dummy2[i][j]=(j,255,i)

dummy2=cv2.cvtColor(dummy2,cv2.COLOR_HSV2BGR)

while True:
    cv2.imshow('dummy',dummy)   
    cv2.moveWindow('dummy',0,0)

    cv2.imshow('dummy2',dummy2)   
    cv2.moveWindow('dummy2',0,300)


    if cv2.waitKey(1) & 0xFF == ord('q'):
       break     

