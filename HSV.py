import cv2
import numpy as np
def nothing(x):
    print(x)


cv2.createTrackbar('L_H','trace',0,255,nothing)
cv2.createTrackbar('L_S','trace',0,255,nothing)
cv2.createTrackbar('L_V','trace',0,255,nothing)
cv2.createTrackbar('U_H','trace',255,255,nothing)
cv2.createTrackbar('U_S','trace',255,255,nothing)
cv2.createTrackbar('U_V','trace',255,255,nothing)

while(True):
    img=cv2.imread('smarties.png',1)
    cv2.namedWindow('trace')
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos('L_H','trace')
    ls=cv2.getTrackbarPos('L_S','trace')
    lv=cv2.getTrackbarPos('L_V','trace')
    uh=cv2.getTrackbarPos('U_H','trace')
    us=cv2.getTrackbarPos('U_S','trace')
    uv=cv2.getTrackbarPos('U_V','trace')

    l_b=np.array([lh,ls,lv])
    u_b=np.array([uh,us,uv])

    mask=cv2.inRange(img,l_b,u_b)
    res=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow('frame',img)
    cv2.imshow('mask',mask)
    cv2.imshow('result',res)

    k=cv2.waitKey(1)
    if(k==27):
        break
cv2.destroyWindow('trace')
cv2.destroyWindow('frame')