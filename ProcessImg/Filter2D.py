import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../Images/abc.png')

kernel = np.ones((9, 9), np.float32) / 10
print(kernel)
dst = cv2.filter2D(img, -1, kernel)

cv2.imshow("imange",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()