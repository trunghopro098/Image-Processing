import tkinter as tk
import cv2
from PIL import Image, ImageTk
from threading import Thread
def select_roi():
    # global image
    img = cv2.imread("../Images/goodgirrl.png")
    roi = cv2.selectROI(img)
    ytopL = int(roi[1])
    yBottomR = int(roi[1] + roi[3])
    XtopL =  int(roi[0])
    XBottomR = int(roi[0] + roi[2])

    print(img.shape)
    print(img.size)
    print(img.dtype)
    b,g,r = cv2.split(img)
    img= cv2.merge((b,g,r))
    imCrop = img[ytopL:yBottomR, XtopL:XBottomR]
    print(ytopL)
    print(yBottomR)
    print(XtopL)
    print(XBottomR)
    img[ytopL:yBottomR, XtopL:XBottomR] = imCrop
    cv2.imshow("image",img)
    # image = Image.fromarray(cv2.cvtColor(imCrop, cv2.COLOR_BGR2RGB))

    cv2.imshow("crop", imCrop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
select_roi()