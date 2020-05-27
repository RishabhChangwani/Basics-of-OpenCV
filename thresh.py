import cv2
import numpy as np

img=cv2.imread('col.jpg',1)

#retval,threshold=cv2.threshold(img,220,150,cv2.THRESH_BINARY_INV)
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#retval2,threshold2=cv2.threshold(grayscaled,200,0,cv2.THRESH_TRUNC+cv2.THRESH_OTSU)
th2=cv2.adaptiveThreshold(grayscaled,240,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,0.75)
th3=cv2.adaptiveThreshold(grayscaled,240,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,1)

cv2.imshow('Gaus',th3)
#cv2.imshow('Grayscaled',grayscaled)
#cv2.imshow('thresh2',threshold2)
cv2.imshow('Orignal',img)
cv2.imshow('Mean_C',th2)
#cv2.imshow('thresh',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()