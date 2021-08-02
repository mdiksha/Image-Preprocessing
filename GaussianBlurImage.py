import cv2
img = cv2.imread(r'C:\Users\VAIBHAV\OneDrive\Desktop\Sample.jpg')
gaussianBlurImg = cv2.GaussianBlur(img,(25,25),0)
cv2.imwrite("GaussianBlurImg.jpg",gaussianBlurImg)
cv2.imshow("GaussianBlurImg",gaussianBlurImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
