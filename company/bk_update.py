"""
author:zym
target:替换白底文字的背景
"""
import cv2

img = cv2.imread("vat_text/000_02.jpg")
background = cv2.imread("bk.jpg")
#创建一个roi
rows,cols,channels = img.shape
roi = background

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
# cv2.imshow("mask",mask)
mask_inv = cv2.bitwise_not(mask)

background_and = cv2.bitwise_and(roi,roi,mask=mask)

img_and = cv2.bitwise_and(img,img,mask=mask_inv)

dst = cv2.add(background_and,img_and)
background = dst

cv2.imwrite("greenbk.jpg",background)
cv2.imshow("test",background)

cv2.waitKey(0)
cv2.destroyAllWindows()
