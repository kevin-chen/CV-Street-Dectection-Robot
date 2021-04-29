import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    ret,img = cap.read()
    
    blurred_img = cv2.GaussianBlur(img, (5, 5), 10)
    gray_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", gray_img)
    edge_img = cv2.Canny(img,100,200)
    cv2.imshow("Edge Image", edge_img)

    k = cv2.waitKey(10)
    if k == 27:
        break