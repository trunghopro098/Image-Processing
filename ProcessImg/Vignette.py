import numpy as np
import cv2
import sys
def blur(nameImg,cl,rw):
    img = cv2.imread(nameImg)
    rows, cols = img.shape[:2]
    # generating vignette mask using Gaussian kernels
    kernel_x = cv2.getGaussianKernel(cols, cl)
    kernel_y = cv2.getGaussianKernel(rows, rw)
    kernel = kernel_y * kernel_x.T
    mask = 255 * kernel / np.linalg.norm(kernel)
    output = np.copy(img)

    # applying the mask to each channel in the input image
    for i in range(3):
        output[:, :, i] = output[:, :, i] * mask
    # print(output)
    return output
    # cv2.imshow('image', output)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


