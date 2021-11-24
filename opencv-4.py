#AIM: this is an alternate solution to previous checkerboard program

import cv2
import numpy as np

boardsize=int(input("hey,enter the board size: "))
numsquare=int(input("hey,enter the number of squares: "))
squaresize=int(boardsize/numsquare)

x=255
y=0


while True: 
  
    
    frame=np.zeros([boardsize,boardsize,3],dtype=np.uint8)
    
    for row in range(0,numsquare):
        for col in range(0,numsquare):
            frame[squaresize*row:squaresize*(row+1),squaresize*col:squaresize*(col+1)]=(x,y,0)
             
            x,y=y,x 

        x,y=y,x     

    
    cv2.imshow('my board',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break



