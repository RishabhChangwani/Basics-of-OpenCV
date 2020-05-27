import cv2
import numpy as np

img=cv2.imread('mask.jpeg',1)
rows,cols,channels=img.shape
roi=img[0:rows,0:cols]
img2gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

add=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('add',add)
cv2.imshow('mask',mask)
#cv2.imshow('bgr2gray',img2gray)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()