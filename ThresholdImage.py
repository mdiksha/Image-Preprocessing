import cv2
img = cv2.imread(r'C:\Users\VAIBHAV\OneDrive\Desktop\Sample.jpg')
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threshImg = cv2.threshold(grayImg,120,255,cv2.THRESH_BINARY)[1]

cv2.imwrite("ThresholdImg.jpg",threshImg)
cv2.imshow("ThresholdImg",threshImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
