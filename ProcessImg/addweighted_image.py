import cv2

def add(image1,alpha,image2,beta,gamma):
    img = cv2.resize(image1, (368, 470))
    img1 = cv2.resize(image2, (368, 470))
    dst = cv2.addWeighted(img, alpha, img1, beta, gamma)
    return dst