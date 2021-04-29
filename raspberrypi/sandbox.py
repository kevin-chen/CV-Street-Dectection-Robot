import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    ret,img = cap.read()
    blurred_img = cv2.GaussianBlur(img, (5, 5), 10)
    sobel_x = cv2.Sobel(blurred_img, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(blurred_img, cv2.CV_64F, 0, 1, ksize=5)
    gradient_magnitude_image = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
    cv2.imshow("Not Gradient Magnitude", img)
    k = cv2.waitKey(10)
    if k == 27:
        break