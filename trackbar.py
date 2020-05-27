import cv2
import numpy as np
def nothing(x):
    print(x)
    
img=np.zeros((990,1890,3),np.uint8)
cv2.namedWindow('win')
cv2.createTrackbar('B','win',0,255,nothing)
cv2.createTrackbar('G','win',0,255,nothing)
cv2.createTrackbar('R','win',0,255,nothing)
cv2.createTrackbar('switch','win',0,1,nothing)

switch='O : OFF\n 1 : ON'
while(1):
    cv2.imshow('win',img)
    b=cv2.getTrackbarPos('B','win')
    g=cv2.getTrackbarPos('G','win')
    r=cv2.getTrackbarPos('R','win')
    s=cv2.getTrackbarPos('switch','win')
    if(s==1):
        img[:]=[b,g,r]
    else:
        img[:]=0
    k=cv2.waitKey(1)
    if(k==27):
        break
cv2.destroyWindow('win')
