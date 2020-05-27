import cv2
from datetime import datetime
cap=cv2.VideoCapture(0)
now= str(datetime.now())
while(cap.isOpened):
    now= str(datetime.now())
    ret,frame= cap.read()
    #frame=cv2.cvtColor(frame, cv2.COLOR_BGR)
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.putText(frame,now,(0,470),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
    cv2.imshow('frame',frame)
    if(cv2.waitKey(1)==27):
        break
cap.release()
cv2.destroyWindow('frame')
