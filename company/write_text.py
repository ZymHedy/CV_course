import cv2
import numpy as np
from PIL import Image,ImageDraw,ImageFont

#生成一个空白的背景图
def white_bk():
    img = np.zeros((64, 64, 3), np.uint8)
    img.fill(255)
    cv2.imwrite("white_img.jpg", img)
    cv2.imshow("white_img", img)
    cv2.waitKey(0)

#在空白背景上写字
def write_En(letter,img):
    #设置文本的相关参数
    fontface = cv2.FONT_HERSHEY_COMPLEX
    fontscale = 0.5
    thickness = 2
    textsize = cv2.getTextSize(letter,fontface,fontscale,thickness)
    print(textsize)
    [cols,rows,channel] = np.shape(img)
    x = int(cols/2-textsize[0][0]/2)
    y = int(rows/2+textsize[0][1]/2)
    print(x)
    print(y)
    org = (x,y)
    fontcolor = (0,0,0)#BGR
    cv2.putText(img,letter,org,fontface,fontscale,fontcolor)
    cv2.imshow("write",img)
    # cv2.imwrite("test.jpg",img)
    cv2.waitKey(0)

#添加中文文字
def write_cn(img,letter,i):
    fontface = cv2.FONT_HERSHEY_COMPLEX
    fontcolor = (0,0,0)
    fontscale = 0.5
    thickness = 2
    # textsize = cv2.getTextSize(letter, fontface, fontscale, thickness)
    textsize = 60
    [cols, rows, channel] = np.shape(img)
    x = int(cols/2 - textsize/2)
    y = int(rows/2 - textsize/2)
    print(x)
    print(y)
    pil_img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)
    fonttext = ImageFont.truetype("font/simhei.ttf",textsize,encoding='utf-8')
    draw.text((x,y),letter,fontcolor,fonttext)

    texted_img = cv2.cvtColor((np.asarray(pil_img)),cv2.COLOR_RGB2BGR)
    # cv2.imshow("chinese",texted_img)
    if i < 10:
        out = 'test/00'+str(i)+'_01.jpg'
    else:
        out = 'test/0'+str(i)+'_01.jpg'

    cv2.imwrite(out,texted_img)
    # cv2.waitKey(0)

datalist = ['中','国','石','油','天','然','气','股','份','有','限','公','司','陕','西','安','销','售'
            ,'分','硕','展','装','饰','修','工','程','汽','油','车','用','315']
lth = len(datalist)
white_img = cv2.imread("white_img.jpg")
for i,letter in enumerate(datalist):
    write_cn(white_img,letter,i)
# 中国石油 天然气股份有限公司陕西安销售分硕展装饰修工程汽油车用315
letter = '31'
