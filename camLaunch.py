import cv2

print(cv2.__version__)

mycam=cv2.VideoCapture(0)
while True:
    ignore,frame=mycam.read()
    cv2.imshow('mycam',frame)
    cv2.moveWindow('mycam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
    