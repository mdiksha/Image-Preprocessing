import cv2
import numpy
path = r"C:\Users\VAIBHAV\OneDrive\Desktop\Sample.jpg"
img = cv2.imread(path)
cv2.imshow("DM Logo",img)
cv2.imwrite("DMlogo.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
