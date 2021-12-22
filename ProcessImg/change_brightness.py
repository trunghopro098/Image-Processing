import numpy as np
import cv2
import sys
def change_brightness(img, alpha, beta):
    # a*f(x,y)+b
    img_new = np.asarray(alpha*img + beta, dtype=int)   # dtype theo mặt định kiểu dử liệu đầu vào và áp dụng cho mảng kết quả. A nhập dử liệu theo bất hình thức nào
    img_new[img_new>255] = 255
    img_new[img_new<0] = 0
    # print(img_new)
    return img_new
def Display_Change_brightness():
    alpha = 1
    beta = 35
    if len(sys.argv) == 3:
        alpha = float(sys.argv[1])
        beta = int(sys.argv[2])
    img = cv2.imread(r"C:\Users\Administrator\PycharmProjects\XULYANH\Images\dosang.png")
    img_new =change_brightness(img,alpha,beta)
    cv2.imwrite("../qqq.png", img_new)