#AIM: to make a checkerboard(sqaure)
#boardsize: one side is asked from user
#numsqaures: number of squares on one side is asked from user

import cv2
import numpy as np

boardsize=int(input("hey,enter the board size: "))
numsquare=int(input("hey,enter the number of squares: "))
squaresize=int(boardsize/numsquare)

darkcolor= (255,0,0)
lightcolor= (0,255,0)
nowcolor= darkcolor

while True: 
    frame=np.zeros([boardsize,boardsize,3],dtype=np.uint8)
    
    for row in range(0,numsquare):
        for col in range(0,numsquare):
            frame[squaresize*row:squaresize*(row+1),squaresize*col:squaresize*(col+1)]=nowcolor
             
            #here we are toggling between light and dark color, as we need alternate colors for the checkerboard 
            if nowcolor==darkcolor:
                nowcolor=lightcolor
            else :
                nowcolor=darkcolor    

    #here we get stripes instead of squares
    #hence we need to flip the color before going to the next row
        if nowcolor==darkcolor:
                nowcolor=lightcolor
        else :
                nowcolor=darkcolor    

    cv2.imshow('my board',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break



