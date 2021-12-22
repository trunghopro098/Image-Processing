import  cv2
import numpy as np

def tv_60(img,thresh,val):
        img = cv2.imread(img)

        height, width = img.shape[0:2]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for i in range(height):
            for j in range(width):
                if np.random.randint(100) <= thresh:
                    if np.random.randint(2) == 0:
                        gray[i, j] = min(gray[i, j] + np.random.randint(0, val+1), 255) # thêm nhiễu vào hình ảnh và các giá trị cài đặt> 255 về 255.
                    else:
                        gray[i, j] = max(gray[i, j] - np.random.randint(0, val+1), 0) # trừ nhiễu cho hình ảnh và cài đặt các giá trị <0 về 0

        return gray
        # cv2.imshow('Original', img)
        # if cv2.waitKey(1) & 0xFF == ord('a'):
        #     return 0
    # cv2.destroyAllWindows()

path = "../Images/tre.png"
# tv_60(path,30,80)