import cv2
import numpy

path =r'C:\Users\VAIBHAV\OneDrive\Desktop\Sample2.jpg'
img = cv2.imread(path)
grayImg = cv2.imread(path,0)

# Second method to convert into gray image
# grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imwrite("GrayImage.jpg",grayImg)
cv2.imshow("OriginalImage",img)
cv2.imshow("GrayScaleImage",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
