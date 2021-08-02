import cv2
import time

cam = cv2.VideoCapture(0)
time.sleep(1)

_,img = cam.read()
cv2.imwrite("ImagefromCamera.jpg",img)
cam.release()

cv2.imshow("ImagefromCamera",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
