import cv2
import imutils
img = cv2.imread(r'C:\Users\VAIBHAV\OneDrive\Desktop\Sample.jpg')
resizeImg = imutils.resize(img,width=20)
cv2.imwrite("ResizedImg.jpg",resizeImg)
cv2.imshow("ResizedImg",resizeImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
