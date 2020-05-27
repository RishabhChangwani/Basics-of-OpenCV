import cv2
import numpy
import matplotlib
img1=cv2.imread('try.png',1)
img= cv2.imread('try.png',0)
cv2.imshow('My_Window',img)
k = cv2.waitKey(0)
print(k)
if(k==27):
    cv2.destroyAllWindows()
    print("Hello")
elif k== ord('s'):
    print("Hello")
    cv2.imwrite('/home/rishabh/try_copy.png',img)
    cv2.destroyAllWindows()
    cv2.waitKey(2000)
    img2=cv2.imread('try_copy.png',1)
    cv2.imshow('New WIndow',img2)
    cv2.waitKey(5000)
    cv2.imshow('New Window2',img1)
    cv2.waitKey(5000)
