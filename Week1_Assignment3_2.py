# changing the red in the image to blue
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while (True):
    _ , frame = cap.read()
    frame = cv2.cvtColor( frame , cv2.COLOR_BGR2GRAY)
    thr1 = cv2.adaptiveThreshold( frame , 255 ,cv2.ADAPTIVE_THRESH_MEAN_C , \
                                  cv2.THRESH_BINARY ,9 , 3 )
    k = cv2.getGaussianKernel(3, 0)
    blur = cv2.GaussianBlur(thr1 , k.shape , 1)
    blur2 = cv2.medianBlur(blur , 5)

    

    blur3 = cv2.bilateralFilter(blur2 , 9 ,75 , 75)
    cv2.imshow("Original" , frame)
    cv2.imshow("PencilSketch1" , thr1)
    cv2.imshow("PencilSketch2" , blur2)
    cv2.imshow("PencilSketch3" , blur3)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
        
