from tkinter import messagebox
from PIL import ImageTk,Image
import cv2
def ImageGray(filename):
    if (filename.startswith('png', -3) or filename.startswith('jpg', -3) or filename.startswith('peg', -3) or filename.startswith('gif', -3)):
        img= cv2.imread(filename)#đọc ảnh
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#chuyển sang ảnh xám
        ImageGray.img1 = Image.fromarray(gray)
        return ImageGray.img1
        # imgGray = ImageTk.PhotoImage(Display(ImageGray.img1))
    else:
        # print(filename)
        messagebox.showinfo("Image processing","please choose photo !")