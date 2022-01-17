import cv2
import numpy as np
import pytesseract

img_test = cv2.imread("19781743-23523624.jpg")
img_test = cv2.cvtColor(img_test,cv2.COLOR_BGR2GRAY)

cv2.imshow("Test",img_test)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(pytesseract.image_to_string(img_test,lang="fra"))