import cv2
import numpy
import matplotlib

cap= cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out=cv2.VideoWriter('output.mp4',fourcc, 20,(640,480),0)
while(cap.isOpened()):
    ret,frame=cap.read()
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    out.write(frame)
    if (cv2.waitKey(1) == 27):
        break

cap.release()
cv2.destroyAllWindows