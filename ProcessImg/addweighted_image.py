import cv2

def add(image1,alpha,image2,beta,gamma):
    #https://docs.opencv.org/3.4/d5/dc4/tutorial_adding_images.html
    #sử dụng addWeighted thì ảnh phải cùng kích thước của 2 ảnh
    img = cv2.resize(image1, (368, 470))
    img1 = cv2.resize(image2, (368, 470))
    dst = cv2.addWeighted(img, alpha, img1, beta, gamma)
    #alpha beta thay đổi độ tương phản của tường ảnh tương ứng trong khoản 0 đến 1
    return dst