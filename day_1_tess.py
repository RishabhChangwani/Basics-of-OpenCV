import pytesseract
import cv2
img=cv2.imread('/home/rishabh/Pictures/Project/DHT22.jpg',1)
img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
print(pytesseract.image_to_string(img))
#print(pytesseract.image_to_boxes(img))
cv2.imshow('win',img)
cv2.waitKey(0)
cv2.destroyWindow('win')