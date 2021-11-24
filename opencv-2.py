#this program gives error

import cv2
import numpy as np

while True:
    frame=np.zeros([256,256,3],dtype=np.uint8)
    
    val=255
    x=0,y=32
    a=0,b=32
    flag=1
    for i in range(0,8):
        x=0,y=32
        for j in range(0,8) :
            if flag==1 :
             frame[a:b,x:y]=(val,val,val)
            else :
             frame[a:b,x:y]=(0,0,0)
            x=y
            y=y+32
            flag=flag*-1
        a=b
        b=b+32

    cv2.imshow('mycam',frame)
    cv2.moveWindow('mycam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q') :
        break