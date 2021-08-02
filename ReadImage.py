import cv2
import numpy

path = r'C:\Users\VAIBHAV\OneDrive\Desktop\Sample2.jpg'
img = cv2.imread(path)
print(img.shape)
print(img.size)
print(img.dtype)
