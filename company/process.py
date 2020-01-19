import cv2
import numpy as np

def gauss(img,i):
    blur = cv2.GaussianBlur(img,(5,5),0)
    if i < 10:
        out = 'test/00'+str(i)+'_00.jpg'
    else:
        out = 'test/0'+str(i)+'_00.jpg'
    # output = 'vat_font/0'+num+'_08.jpg'
    cv2.imwrite(out,blur)
    # cv2.imshow("blur",blur)
    # cv2.waitKey(0)

def random_noise(img,dot,dotI,i):
    dotNum = dot
    [cols,rows,channel] = np.shape(img)
    for index in range(dotNum):
        x = int(np.random.uniform(0,cols))
        y = int(np.random.uniform(0,rows))
        img[x,y,0] = 255
        img[x,y,1] = 255
        img[x,y,2] = 255
    # print(type(index))
    # print(type(dotI))
    if i < 10:
        out = 'test/00'+str(i)+'_0'+dotI+'.jpg'
    else:
        out = 'test/0'+str(i)+'_0'+dotI+'.jpg'

    # out = 'vat_font/0'+i+'_0'+dotI+'.jpg'
    cv2.imwrite(out,img)
    # cv2.imshow("noise",img)
    # cv2.waitKey(0)

# img = cv2.imread("vat_font/016_01.jpg")
# gauss(img)
# random_noise(img)

for i in range(31):
    if i < 10:
        input = 'test/00'+str(i)+'_01.jpg'
    else:
        input = 'test/0'+str(i)+'_01.jpg'
    # input = 'vat_font/00'+i+'_01.jpg'
    img = cv2.imread(input)
    gauss(img,i)
    random_noise(img, 700, str(2), i)
    random_noise(img, 1000, str(3), i)
    random_noise(img, 2000, str(4), i)
    random_noise(img, 3000, str(5), i)
    # random_noise(img, 4000, str(6), i)
    # random_noise(img, 5000, str(6), i)
    # random_noise(img, 10000, str(7), i)