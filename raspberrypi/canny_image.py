import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50,150)
    cv2.imshow("Edge Image", edges)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()