

#AIM: previous program modified

import cv2
import numpy as np
import time
import random

boardsize=int(input("hey,enter the board size: "))
numsquare=int(input("hey,enter the number of squares: "))
squaresize=int(boardsize/numsquare)



while True: 
  
    
    frame=np.zeros([boardsize,boardsize,3],dtype=np.uint8)

    for times in range(0,5) :
     for row in range(0,numsquare):
        for col in range(0,numsquare):
                frame[squaresize*row:squaresize*(row+1),squaresize*col:squaresize*(col+1)]=(0,random.randint(0,255),0)
             
              

             

    time.sleep(10)
    
    

       
    
    cv2.imshow('my board',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break



