import cv2
import numpy as np

while True:
    frame=np.zeros([256,256,3],dtype=np.uint8)
    frame[:,:125]=(255,125,40)
    frame[:,125:]=(0,0,255)

    cv2.imshow('mycam',frame)
    cv2.moveWindow('mycam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q') :
        break