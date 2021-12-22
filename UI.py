from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
import cv2
import numpy as np
import os
from datetime import date
from datetime import datetime
from threading import Thread
from numpy._distributor_init import filename
from ProcessImg import change_brightness
from ProcessImg import Vignette
from ProcessImg import ImageGrayProcess
from ProcessImg import addweighted_image
from ProcessImg import RGB_Image
from ProcessImg import Sepia
from ProcessImg import TV60
from ProcessImg import draw
import tkinter.ttk as CB
import random
from tkinter import filedialog

pathNew = "./Images/editnew.png";
#resize ảnh về kích thwcowcs cố định để hiển thị lên lable
def Display(name):
    width = 368
    height = 470
    use_resize = True
    if use_resize:
        # Image.resize returns a new PIL.Image of the specified size
        PIL_image_small = name.resize((width, height), Image.ANTIALIAS)
    else:
        # Image.thumbnail converts the image to a thumbnail, in place
        PIL_image_small = name
        PIL_image_small.thumbnail((width, height), Image.ANTIALIAS)
    return PIL_image_small

def Displaymini(name):
    width = 240
    height = 270
    # You may prefer to use Image.thumbnail instead
    # Set use_resize to False to use Image.thumbnail
    use_resize = True
    if use_resize:
        # Image.resize returns a new PIL.Image of the specified size
        PIL_image_small = name.resize((width, height), Image.ANTIALIAS)
    else:
        # Image.thumbnail converts the image to a thumbnail, in place
        PIL_image_small = name
        PIL_image_small.thumbnail((width, height), Image.ANTIALIAS)
    return PIL_image_small

#open file ảnh
def openfileImabe():
    global my_image
    global filename
    global name_main
    global setCondition
    filename = filedialog.askopenfilename(initialdir=r"..\XULYANH\Image",title="Select A File",filetypes=(("png files","*.png"),("all files","*.*")))
    openImg = Image.open(filename)
    my_image = ImageTk.PhotoImage(Display(openImg))#đoc file ảnh và resize
    # my_image_lable = Label(labelframe2,image=my_image).pack()
    my_image_lable.configure(image= my_image)#hiển thị ảnh lên lable
    my_image_lable.image= my_image
    setCondition = 0
    name_main=filename
# print(filename)



mask3x3 = np.ones((3, 3), dtype="float") * (1.0 / (3 * 3))
mask5x5 = np.ones((5, 5), dtype="float") * (1.0 / (5 * 5))
mask11X11 = np.ones((11, 11), dtype="float") * (1.0 / (11 * 11))
mask21X21 = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))


#tạo mặt nạ lọc theo kích thướt
arrValue = [3,5,7,9,11,13,15,17,19,21]
arrMASKVALUE = ["3x3","5x5","7X7","9X9","11X11","13X13","15X15","17X17","19X19","21X21"]
def getvaluemass():
    n = combbkenner.get()
    q = 0
    for i in range(0, len(arrMASKVALUE)):
        if (n == arrMASKVALUE[i]):
            q = i
    return q
#chuyển ảnh xám

def saveNewTmp(saveImg):
    if (os.path.exists(r".\Images\new_img.png")):
        os.remove(r".\Images\new_img.png")
        cv2.imwrite(r".\Images\new_img.png", saveImg)
    else:
        cv2.imwrite(r".\Images\new_img.png", saveImg)


def ImageGray():
        global saveImg
        saveImg = ImageGrayProcess.ImageGray(filename)#trả về ảnh đã xử lý
        imgGray = ImageTk.PhotoImage(Display(saveImg)) #resize ảnh và đọc ảnh để hiển thị
        my_image_lable2.configure(image=imgGray)
        my_image_lable2.image=imgGray
        labelframe3.configure(text="ẢNH XÁM")

#Cân bằng histogram
def HistogramBalance():
        global saveImg
        img1 = cv2.imread(filename,0)
        hist = cv2.equalizeHist(img1)#cân bằng hist
        saveImg = Image.fromarray(hist)
        ingHist = ImageTk.PhotoImage(Display(saveImg))
        my_image_lable2.configure(image=ingHist)
        my_image_lable2.image=ingHist
        labelframe3.configure(text="CÂM BẰNG HISTOGRAM")

#Phát hiện cạnh sử dụng canny
def Candy(var):
    #ẩn my_image_lable2 và canvas
        my_image_lable2.place(x=6, y=20)
        global saveImg
        img = cv2.imread(filename)# đọc ảnh
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#chuyển sang ảnh xám
        saveImg = cv2.Canny(gray, thresholdslider1.get(), thresholdslider2.get())#dò cạnh
        saveNewTmp(saveImg)
        Candy.img1 = Image.fromarray(saveImg)
        ingHist = ImageTk.PhotoImage(Display(Candy.img1))
        my_image_lable2.configure(image=ingHist)
        my_image_lable2.image=ingHist
        my_image_lable2.configure(text="ĐƯỜNG VIỀN")
        # my_image_lable2.bind("<Button-1>",get_x_and_y)
#kiểm tra ảnh đầu vào
def check_Img():
    if(filename is None):
        messagebox.showinfo("Image processing", "please choose photo !")
        return False
    else:
        if (filename.startswith('png', -3) or filename.startswith('jpg', -3) or filename.startswith('peg', -3) or filename.startswith('gif', -3)):
            return True
        else:
            messagebox.showinfo("Image processing", "please choose photo !")
            return False

#thay đổi độ sáng tối của ảnh

def Display_Change_brightness(var):#sử dụg slider nên ta truyền tham số ảo

        my_image_lable2.place(x=6, y=20)
        global saveImg
        global path_brightness


        img = cv2.imread(filename)
        saveImg = change_brightness.change_brightness(img, slider_alpha.get(), slider_beta3.get())
        # if (r"C:\Users\Administrator\PycharmProjects\XULYANH\Images\new_img.png"):
        saveNewTmp(saveImg)
        openImg_new = Image.open(r"./Images/new_img.png")
        newImg = ImageTk.PhotoImage(Display(openImg_new))
        my_image_lable2.configure(image=newImg)
        my_image_lable2.image = newImg
        labelframe3.configure(text="THAY ĐỔI ĐỘ SÁNG CỦA ẢNH")


#làm mờ 4 góc của ảnh
def Vignette1(var):
        my_image_lable2.place(x=6, y=20)
        global saveImg
        saveImg = Vignette.blur(filename,slider_Y.get(),slider_X.get())
        saveNewTmp(saveImg)
        openImg_new = Image.open(r"./Images/new_img.png")
        newImg = ImageTk.PhotoImage(Display(openImg_new))
        my_image_lable2.configure(image=newImg)
        my_image_lable2.image = newImg
        labelframe3.configure(text="LÀM MỜ 4 GÓC")
        print("đã lưu")
#tạo prj làm việc mới
def New():
    global saveImg
    global filename
    setCondition = 0
    filename = None
    openImg_new = Image.open(r"./Images/black.png")
    newImg = ImageTk.PhotoImage(Display(openImg_new))
    newImg1 = ImageTk.PhotoImage(Displaymini(openImg_new))
    my_image_lable.configure(image=newImg)
    lable_anh12.configure(image=newImg1)
    labelframe2.configure(text="NEW")
    my_image_lable2.configure(image=newImg)
    labelframe3.configure(text="NEW")
    lable_anh1.configure(image=newImg1)

#save ảnh
def save_Img():
    try:
        #lấy thời gian hiện tại khi lưu ảnh sẽ không bị trùng tên ảnh
        today = date.today()
        print("Ngay hien tai:", today)
        val = random.randint(1, 10000)
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        print("Gio hien tai =", current_time)

        if (saveImg is None):
            messagebox.showinfo("Image Processing", "Please process before saving !")
        else:
            # cú pháp tên ảnh khi lưu yyyy-mm-dd_H_M_S.png
            cv2.imwrite(r"./ProcessedImage/" + str(today) + "_" + str(current_time) + "_new_img.png", saveImg)
            messagebox.showinfo("Image Processing", "saved !")
    except(NameError):
        messagebox.showinfo("Image Processing", "Please process before saving !")
#Save as
def save_as():
    try:
        if(saveImg is None):
            messagebox.showinfo("Image Processing","Please process before saving !")
        else:
            print(type(saveImg))
            file  = filedialog.asksaveasfilename(defaultextension = ".*",initialdir ="./ProcessedImage/",title= "Save File", filetypes=(("png files","*.png"),("all files","*.*")) )
            cv2.imwrite(file,saveImg)
            messagebox.showinfo("Image Processing", "saved !")
    except(NameError):
        messagebox.showinfo("Image Processing","Please process before saving !")


#mở ảnh số 2
def opemImage2():
    global image2
    global filename2
    filename2 = filedialog.askopenfilename(initialdir=r".\XULYANH\Images",title="Select A File",filetypes=(("png files","*.png"),("all files","*.*")))
    openImg1 = Image.open(filename2)
    image2 = ImageTk.PhotoImage(Displaymini(openImg1))
    # my_image_lable = Label(labelframe2,image=my_image).pack()
    lable_anh12.configure(image=image2)
    lable_anh12.image = image2
    addweightedImag(1)


#ghép 2 ảnh
def addweightedImag(var):
    my_image_lable2.place(x=6, y=20)
    global saveImg
    try:
        img = cv2.imread(filename)
        img2 = cv2.imread(filename2)
        saveImg = addweighted_image.add(img,slider_apha1.get(),img2,slider_beta.get(),slider_gamma.get())#dst=α⋅src1+β⋅src2+γ
        # if (r"C:\Users\Administrator\PycharmProjects\XULYANH\Images\new_img.png"):
        saveNewTmp(saveImg)
        openImg_new = Image.open(r"./Images/new_img.png")
        newImg = ImageTk.PhotoImage(Display(openImg_new))
        my_image_lable2.configure(image=newImg)
        my_image_lable2.image = newImg
        labelframe3.configure(text="GHÉP ẢNH")
    except NameError:
        print(NameError)

#Chuyển đổi các hệ màu
def GRB2GRB(var):

    my_image_lable2.place(x=6, y=20)

    global saveImg
    my_image_lable2.place(x=6, y=20)
    saveImg = RGB_Image.GRB(filename,slider_RED.get(),slider_GREEN.get(),slider_BLU.get())
    os.remove(r".\Images\new_img.png")
    saveImg.save(r".\Images\new_img.png")
    saveImg = cv2.imread(r".\Images\new_img.png")#đọc ảnh bằng thư viện cv2 cho biến global saveImg để thực hiện save as
    # saveImg.show()
    openImg_new = Image.open(r".\Images\new_img.png")
    newImg = ImageTk.PhotoImage(Display(openImg_new))
    my_image_lable2.configure(image=newImg)
    my_image_lable2.image = newImg
    labelframe3.configure(text="GRB")

path = "./Images/tre.png"

#làm nhiểu ảnh
def TV_60(var):

    my_image_lable2.place(x=6, y=20)
    global saveImg
    saveImg = TV60.tv_60(filename,thresholdsliderTV60.get(),thresholdsValueTV60.get())
    saveNewTmp(saveImg)
    # saveImg.show()
    openImg_new = Image.open(r".\Images\new_img.png")
    newImg = ImageTk.PhotoImage(Display(openImg_new))
    my_image_lable2.configure(image=newImg)
    my_image_lable2.image = newImg
    labelframe3.configure(text="TV 60")

def Sepia_Img():

    my_image_lable2.place(x=6, y=20)
    global saveImg
    saveImg = Sepia.sepia(filename)
    saveNewTmp(saveImg)
    openImg_new = Image.open(r".\Images\new_img.png")
    newImg = ImageTk.PhotoImage(Display(openImg_new))
    my_image_lable2.configure(image=newImg)
    my_image_lable2.image = newImg
    labelframe3.configure(text="SEPIA")


#làm mờ background
def ROI_Img(var):
    my_image_lable2.place(x=6, y=20)
    global saveImg
    global imCrop
    global ytopL
    global yBottomR
    global XtopL
    global XBottomR
    try:
        w = arrValue[getvaluemass()] #lấy giá trị mặt nạ lọc
        # print(w)
        h = arrValue[getvaluemass()]
        x = slider_sigmaX1.get()
        y = slider_sigmaY.get()
        saveImg = cv2.imread(filename) #đọc ảnh
        b, g, r = cv2.split(saveImg)  # tách thành 3 kênh màu
        saveImg = cv2.merge((b, g, r))  # gọp kênh
        # roi = cv2.selectROI(img)
        # tọa độ của điểm ảnh
        if (roi != None):
            ytopL = int(roi[1])
            yBottomR = int(roi[1] + roi[3])
            XtopL = int(roi[0])
            XBottomR = int(roi[0] + roi[2])
            # print(ytopL)
            # print(yBottomR)
            # print(XtopL)
            # print(XBottomR)
            #cắt ảnh theo vj trí tọa độ
            imCrop = saveImg[ytopL:yBottomR, XtopL:XBottomR]
        #lưu ảnh crop
        path = "./Images/new_roi.png"
        if (os.path.exists(path)):
            os.remove(r".\Images\new_roi.png")
            cv2.imwrite(r".\Images\new_roi.png", imCrop)
        else:
            cv2.imwrite(r".\Images\new_roi.png", imCrop)
        #Hiển thị ảnh đã cắt lên giao diện
        openImg = Image.open(path)
        image3 = ImageTk.PhotoImage(Displaymini(openImg))
        label_fr_object.configure(text="OBJECT")
        lable_anh1.configure(image= image3)
        lable_anh1.image= image3

        #làm mờ ảnh gaussian
        saveImg = cv2.GaussianBlur(saveImg, ksize=(w,h), sigmaX=x, sigmaY=y)
        #gọp ảnh làm mờ
        saveImg[ytopL:yBottomR, XtopL:XBottomR] = imCrop
        #save ảnh
        saveNewTmp(saveImg)
        openImg_new1 = Image.open(r".\Images\new_img.png")#đọc ảnh và hiển thị lên tkinter
        newImg1 = ImageTk.PhotoImage(Display(openImg_new1))
        my_image_lable2.configure(image=newImg1)
        my_image_lable2.image = newImg1
        labelframe3.configure(text="ẢNH SAU CHỈNH SỬA")
        # cv2.imshow("qaa",saveImg)
        # cv2.waitKey(0)
        # print(img.shape)
        # print(img.size)
        # print(img.dtype
        # img[ytopL:yBottomR, XtopL:XBottomR] = imCrop
    except(NameError):
        print(NameError)

# hiển thị selectROI và trả về vị trí tọa độ
def roi_x_y():
    global roi
    showCrosshair = FALSE
    fromCenter = FALSE
    img = cv2.imread(filename)
    roi = cv2.selectROI("Image",img, fromCenter, showCrosshair)
    return roi

def ROI_Img_process():
    roi_x_y()
    global  thread
    if(roi):
        KERNEL.place(x=2, y=363)
        #slider_mask.place(x=60, y=340)
        combbkenner.place(x=100, y=360)
        sigmaX.place(x=2, y=410)
        slider_sigmaX1.place(x=80, y=390)
        sigmaY.place(x=2, y=450)
        slider_sigmaY.place(x=80, y=425)
        ROI_Img(1)
    # thread = Thread(target=ROI_Img, daemon=True)
    # thread.start()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        return 0


def getvaluecombbox():
    n = combb1.get()
    q = 0
    for i in range(0, len(arrMASKVALUE)):
        if (n == arrMASKVALUE[i]):
            q = i
    return q

#làm mịn
def Gaussian_smooothing(var):

    my_image_lable2.place(x=6, y=20)
    global saveImg
    ksize = arrValue[getvaluecombbox()]
    x=slider_sigmaXG.get()
    y=slider_sigmaYG.get()
    saveImg = cv2.imread(filename)  # đọc ảnh
    saveImg = cv2.GaussianBlur(saveImg, ksize=(ksize,ksize), sigmaX=x, sigmaY=y)

    saveNewTmp(saveImg)
    openImg_new = Image.open(r".\Images\new_img.png")
    newImg = ImageTk.PhotoImage(Display(openImg_new))
    my_image_lable2.configure(image=newImg)
    my_image_lable2.image = newImg
    labelframe3.configure(text="GAUSSIAN")


def Bilaterai(var):
#https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html
    my_image_lable2.place(x=6, y=20)
    global saveImg
    saveImg = cv2.imread(filename)  # đọc ảnh
    saveImg = cv2.bilateralFilter(saveImg,slider_D.get(),slider_SimaColor.get(),slider_Space.get())
    saveNewTmp(saveImg)
    openImg_new = Image.open(r".\Images\new_img.png")
    newImg = ImageTk.PhotoImage(Display(openImg_new))
    my_image_lable2.configure(image=newImg)
    my_image_lable2.image = newImg
    labelframe3.configure(text="BILATERAL")

def Mean_smoothing():

    my_image_lable2.place(x=6, y=20)
    global saveImg
    x= arrValue[getvaluecombbox()]
    saveImg = cv2.imread(filename)  # đọc ảnh
    kernel = np.ones((x,x),np.float32)/(x*x)
    saveImg = cv2.filter2D(saveImg, -1, kernel)

    saveNewTmp(saveImg)
    openImg_new = Image.open(r".\Images\new_img.png")
    newImg = ImageTk.PhotoImage(Display(openImg_new))
    my_image_lable2.configure(image=newImg)
    my_image_lable2.image = newImg
    labelframe3.configure(text="MEAN")

def Median_smoothing():

    my_image_lable2.place(x=6, y=20)
    global saveImg
    x= arrValue[getvaluecombbox()]
    saveImg = cv2.imread(filename)  # đọc ảnh
    saveImg = cv2.medianBlur(saveImg,x)

    saveNewTmp(saveImg)
    openImg_new = Image.open(r".\Images\new_img.png")
    newImg = ImageTk.PhotoImage(Display(openImg_new))
    my_image_lable2.configure(image=newImg)
    my_image_lable2.image = newImg
    labelframe3.configure(text="MEDIAN")

def Sobel_smoothing():

    my_image_lable2.place(x=6, y=20)
    global saveImg

    img = cv2.imread(filename)  # đọc ảnh
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY).astype(float)
    Edge_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    Edge_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    saveImg = np.sqrt(Edge_x ** 2 + Edge_y ** 2)

    saveNewTmp(saveImg)
    openImg_new = Image.open(r".\Images\new_img.png")
    newImg = ImageTk.PhotoImage(Display(openImg_new))
    my_image_lable2.configure(image=newImg)
    my_image_lable2.image = newImg
    labelframe3.configure(text="SOBEL")
def Laplacia_smoothing():

    my_image_lable2.place(x=6, y=20)
    global saveImg
    img = cv2.imread(filename)  # đọc ảnh
    saveImg = cv2.Laplacian(img,cv2.CV_64F)
    saveNewTmp(saveImg)
    openImg_new = Image.open(r".\Images\new_img.png")
    newImg = ImageTk.PhotoImage(Display(openImg_new))
    my_image_lable2.configure(image=newImg)
    my_image_lable2.image = newImg
    labelframe3.configure(text="LAPLACIA")

def Sketch_smoothing(var):

    my_image_lable2.place(x=6, y=20)
    global saveImg
    ksize = arrValue[getvaluecombbox()]
    img = cv2.imread(filename)  # đọc ảnh
    blurr = cv2.GaussianBlur(img, (ksize, ksize), 0)#làm mờ
    saveImg = cv2.divide(img, blurr, scale=slider_Scale.get())#làm nổi bật cạnh của hình
    saveNewTmp(saveImg)
    openImg_new = Image.open(r".\Images\new_img.png")
    newImg = ImageTk.PhotoImage(Display(openImg_new))
    my_image_lable2.configure(image=newImg)
    my_image_lable2.image = newImg
    labelframe3.configure(text="LAPLACIA")


# ẩn frame
def hide_all_framupgrade():
    labelframeSmothing.place_forget()
    labelframeNoise.place_forget()
def smoothing():
    hide_all_framupgrade()
    labelframeSmothing.place(x= 0,y=80)
    R1.place(x=60, y=5)
    R2.place(x=60, y=35)
    R3.place(x=60, y=65)
    R4.place(x=230, y=5)
    R5.place(x=230, y=35)
    R6.place(x=230, y=65)
def Noise1():
    hide_all_framupgrade()
    labelframeNoise.place(x= 0,y=80)
    R11.place(x=60, y=5)
    R22.place(x=60, y=35)
    R33.place(x=60, y=65)
    R44.place(x=230, y=5)
    R55.place(x=230, y=35)
    R66.place(x=230, y=65)

#phần con của smoothing và detect edges
# ẩn fram
def hide_fr():
    labelframeGaussian.place_forget()
    labelframeBilateral.place_forget()
    labelframeMean.place_forget()
    labelframeMedian.place_forget()
    labelframeGradient.place_forget()
    labelframeSobel.place_forget()
    labelframeLaplacia.place_forget()
def gaussian():
    hide_fr()
    labelframeGaussian.place(x= 1, y= 230)
    sigmaXG.place(x=5, y = 40)
    slider_sigmaXG.place(x=70,y= 20 )
    sigmaYG.place(x= 5,y=90 )
    slider_sigmaYG.place(x= 70,y= 70)

def Bilataral():
    hide_fr()
    labelframeBilateral.place(x= 1, y= 230)
    labSD.place(x= 5,y= 30)
    slider_D.place(x= 90,y=10)
    labSimaColor.place(x=5, y = 80)
    slider_SimaColor.place(x=90,y= 60 )
    labSigmaSpace.place(x= 5,y=130 )
    slider_Space.place(x= 90,y= 110)
def Mean():
    hide_fr()
    labelframeMean.place(x= 1, y= 230)
    Mean_smoothing()
def Median():
    hide_fr()
    labelframeMedian.place(x= 1, y= 230)
    Median_smoothing()

def Gradient():
    hide_fr()
    labelframeGradient.place(x= 1, y= 230)
    labScale.place(x= 5,y= 30)
    slider_Scale.place(x=70,y= 10 )
    Sketch_smoothing(1)
def Sobel():
    hide_fr()
    labelframeSobel.place(x= 1, y= 230)
    Sobel_smoothing()

def Laplacia():
    hide_fr()
    labelframeLaplacia.place(x= 1, y= 230)
    Laplacia_smoothing()

#Hiển thị và ẩn các frame menu
def hide_all_frame():
    labelframeCollage.pack_forget()
    labelframe_gray.pack_forget()
    labelframeCHANGEBRIGTHNESS.pack_forget()
    labelframeIMAGESMOOTHING.pack_forget()
    labelframeBlurbackgruond.pack_forget()
    labelframeDraw.pack_forget()

def Pro_Img_Gray():
    hide_all_frame()
    if(check_Img()):
        labelframe_gray.pack(fill="both", expand=1)
        labanhxam.place(x=15, y=5)
        btnGRAY.place(x=200, y=5)
        labhistogram.place(x=15, y=50)
        btnHistogram.place(x=200, y=50)

        labSepia.place(x=15, y=95)
        btnSepia.place(x=200, y=95)

        labhistogram2.place(x=15, y=145)
        threshold1.place(x=15, y=193)
        threshold2.place(x=15, y=239)
        thresholdslider1.place(x=95, y=175)
        thresholdslider2.place(x=95, y=220)

        labTV60 .place(x=15, y=280)
        thresholdTV60.place(x=15, y=317)
        ValueTV60.place(x=15, y=363)

        thresholdsliderTV60.place(x=95, y=295)
        thresholdsValueTV60.place(x=95, y=340)


def Pro_Img_Brightness():
    hide_all_frame()
    if(check_Img()):
        labelframeCHANGEBRIGTHNESS.pack(fill="both", expand=1)
        lab.place(x=1, y=20)
        slider_alpha.place(x=40, y=0)
        lab1.place(x=1, y=60)
        slider_beta3.place(x=40, y=40)
        lab_fourDark.place(x=1, y=90)
        labCl.place(x=1, y=130)
        slider_X.place(x=40, y=105)
        larow.place(x=1, y=175)
        slider_Y.place(x=40, y=150)
        lab_RGB.place(x=1,y=210)
        labR.place(x=1,y=250)
        slider_RED.place(x= 40, y = 230)

        labG.place(x=1,y=290)
        slider_GREEN.place(x= 40, y = 270)

        labB.place(x=1,y=330)
        slider_BLU.place(x= 40, y = 310)


def Pro_Img_Smoothing():
    hide_all_frame()
    if(check_Img()):
        labelframeIMAGESMOOTHING.pack(fill="both", expand=1)
        labmask.place(x=1, y=7)
        combb1.place(x=60, y=7)
        R_Smoothing.place(x=1,y = 45)
        R_Noise.place(x=170, y=45)
            # labSigmax.place(x=1, y=53)
            # slider_sigmaX.place(x=60, y=30)
            # labSigmay.place(x=1, y=93)
            # slider_sigmay.place(x=60, y=70)


def Pro_Collage_Img():
    hide_all_frame()
    labelframe2.configure(text="ẢNH THỨ NHÁT")
    labelframeCollage.pack(fill="both", expand=1)
    if(check_Img()):
        labapha1.place(x=2, y=363)
        slider_apha1.place(x=60, y=340)
        labbeta.place(x=2, y=410)
        slider_beta.place(x=60, y=390)
        labgamma.place(x=2, y=450)
        slider_gamma.place(x=60, y=425)





#vẽ text lên ảnh
def drawtext(text,x,y,size,b,g,r):
    global saveImg

    img = cv2.imread(filename)
    saveImg = draw.draw_text(img, text=text,
                             x=x,
                             y=y,
                             size=size,
                             color_bgr=[b, g, r],
                             is_copy=False)
    saveNewTmp(saveImg)
    openImg_new = Image.open(r".\Images\new_img.png")
    newImg = ImageTk.PhotoImage(Display(openImg_new))
    my_image_lable2.configure(image=newImg)
    my_image_lable2.image = newImg
    labelframe3.configure(text="DRAW TEXT IMAGE")
    my_image_lable2.bind("<Button-1>", get_x_and_y)
    setCondition = 1
    print("commit thử 1 lần ")


def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y
    print(lasx, lasy)

def process_draw():
    # my_image_lable.bind("<Button-1>", get_x_and_y)
    text= textInput.get()
    x= lasx
    y = lasy
    size = slider_textsizepen.get()
    b= slider_BLU_p.get()
    g = slider_GREEN_p.get()
    r = slider_RED_p.get()
    if(text == ''):
        messagebox.showinfo("Image Processing", "Input text !")
    else:
        drawtext(text,x,y,size,b,g,r)

def DrawImg():
    hide_all_frame()
    labelframeDraw.pack(fill="both", expand=1)
    my_image_lable.bind("<Button-1>", get_x_and_y)
    my_image_lable2.place(x=6, y=20)
    labtextpencolor.place(x=10,y=10)
    labtextpencolorB.place(x= 10,y= 40)
    slider_BLU_p.place(x= 100, y = 18)

    labtextpencolorG.place(x=10, y=80)
    slider_GREEN_p.place(x=100,y= 58)

    labtextpencolorR.place(x=10, y=120)
    slider_RED_p.place(x=100,y= 98)

    labtextsizepen.place(x=10,y=160)
    slider_textsizepen.place(x= 100, y= 140)

    labtextinput.place(x= 10, y= 200)
    textInput.place(x= 65, y = 200)
    btnDraw.place(x=100, y=240)


def Blur_background():
    if(check_Img()):
        hide_all_frame()
        labelframeBlurbackgruond.pack(fill="both", expand=1)
def Apply():
    global  filename
    messagebox.showinfo("Image Processing", "Apply success !")
    img = cv2.imread(r".\Images\new_img.png")
    if (os.path.exists(r".\Images\img_tmp.png")):
        os.remove(r".\Images\img_tmp.png")
        cv2.imwrite(r".\Images\img_tmp.png", img)
    else:
        cv2.imwrite(r".\Images\img_tmp.png", img)
    filename = r".\Images\img_tmp.png"

def Reset_Image():
    global filename
    messagebox.showinfo("Image Processing", "Reset success !")
    filename=name_main
    openImg_new = Image.open(filename)
    newImg = ImageTk.PhotoImage(Display(openImg_new))
    my_image_lable2.configure(image=newImg)
    my_image_lable2.image = newImg


app = Tk()

app.title("VKU.UDN.VN-KHOA CÔNG NGHỆ THÔNG TIN - TRUYỀN THÔNG ĐẠI HỌC VIỆT-HÀN")
app.geometry('1180x580+100+20')
app.resizable(False, False)
# app.config(bg="black")
# la = Label(app, background="black", width="1135", height=630).pack()
# image2 =Image.open('logoVKU.png')
# reder = ImageTk.PhotoImage(image2)
# img = Label(app, image= reder,bg="black").place(x=0, y=0)
#Tạo menu
menubar = Menu(app)
app.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New",command=New)
filemenu.add_command(label="Open",command=openfileImabe)
filemenu.add_command(label="Save",command=save_Img)
filemenu.add_command(label="Save as...",command=save_as)
filemenu.add_command(label="Close")
filemenu.add_separator()

Gray = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Gray", menu=Gray)
Gray.add_command(label="Process gray image",command=Pro_Img_Gray)
Gray.add_separator()


Brightness = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Brightness", menu=Brightness)
Brightness.add_command(label="Process brightness image",command=Pro_Img_Brightness)
Brightness.add_separator()


Smoothing = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Smoothing", menu=Smoothing)
Smoothing.add_command(label="Process brightness image",command=Pro_Img_Smoothing)
Smoothing.add_separator()

Graphcut = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Graphcut", menu=Graphcut)
Graphcut.add_command(label="Collage",command=Pro_Collage_Img)
Graphcut.add_separator()
Graphcut.add_command(label="Blur Background",command=Blur_background)
Graphcut.add_separator()


Draw = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Draw", menu=Draw)
Draw.add_command(label="Draw Image",command=DrawImg)
Draw.add_separator()


# Noise = Menu(menubar,tearoff=0)
# menubar.add_cascade(label="Noise", menu=Noise)
# Noise.add_separator()

Editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit", menu=Editmenu)
Editmenu.add_separator()

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_separator()




# Khung xử lý
frame=LabelFrame(app,text="IMAGE PROCESSING",fg = '#F7961E',font= "Time 8 bold",width=348,
             height=520,highlightcolor="yellow",
             highlightbackground="red",highlightthickness=1)
frame.place(x = 5, y = 5)

#xử lý ảnh xám
labelframe_gray=LabelFrame(frame,text="GRAY",fg = 'red',font= "Time 8 bold",width=344,
             height=506,highlightcolor="yellow",
             highlightbackground="red")
labanhxam = Label(labelframe_gray,text="Grayscale image conversion : ",fg= "red",font= "Time 10")
# labanhxam.place(x=15,y=5)
btnGRAY=Button(labelframe_gray,text= "Image Gray",command=ImageGray,width =13,bg ="#B9BCC1",fg = "white",font="Time 8 bold")
# btnGRAY.place(x=200,y=5)
labhistogram = Label(labelframe_gray,text="Balance Histogram : ",fg= "red",font= "Time 10")
# labhistogram.place(x=15,y=50)
btnHistogram =Button(labelframe_gray,text= "Histogram",command=HistogramBalance,width =13,bg ="#AB2365",fg = "white",font="Time 8 bold")
# btnHistogram.place(x=200,y=50)
labSepia = Label(labelframe_gray,text="Sepia Image : ",fg= "red",font= "Time 10")
# labanhxam.place(x=15,y=5)
btnSepia=Button(labelframe_gray,text= "Sepia Image",command=Sepia_Img,width =13,bg ="#662507",fg = "white",font="Time 8 bold")
# btnGRAY.place(x=200,y=5)
labhistogram2 = Label(labelframe_gray,text="Canny Edge Detection :",fg= "red",font= "Time 10 bold")
threshold1 = Label(labelframe_gray,text="Threshold 1 :",fg= "red",font= "Time 10")
# threshold1.place(x=15,y=148)
threshold2 = Label(labelframe_gray,text="Threshold 2 :",fg= "red",font= "Time 10")
# threshold2.place(x=15,y=194)
thresholdslider1 = Scale(labelframe_gray,from_= 50,to=200, length = 230,resolution=5,orient = HORIZONTAL,activebackground="red",troughcolor="yellow",command=Candy)
thresholdslider1.set(100)
# thresholdslider1.place(x= 95, y = 130)
thresholdslider2 = Scale(labelframe_gray,from_= 50,to=300, length = 230,resolution=5,orient = HORIZONTAL,activebackground="red",troughcolor="yellow",command=Candy)
thresholdslider2.set(200)
# thresholdslider2.place(x= 95, y = 175)
#TV60
labTV60 = Label(labelframe_gray,text="TV 60 :",fg= "red",font= "Time 10 bold")

thresholdTV60 = Label(labelframe_gray,text="Threshold :",fg= "red",font= "Time 10")
# threshold1.place(x=15,y=148)
ValueTV60 = Label(labelframe_gray,text="Value :",fg= "red",font= "Time 10")
# threshold2.place(x=15,y=194)
thresholdsliderTV60 = Scale(labelframe_gray,from_= 0,to=100, length = 230,resolution=1,command=TV_60,orient = HORIZONTAL,activebackground="red",troughcolor="#A5A5AE")
thresholdsliderTV60.set(30)
# thresholdslider1.place(x= 95, y = 130)
thresholdsValueTV60 = Scale(labelframe_gray,from_= 0,to=255, length = 230,resolution=10,command=TV_60,orient = HORIZONTAL,activebackground="red",troughcolor="#A5A5AE")
thresholdsValueTV60.set(80)
# thresholdslider2.place(x= 95, y = 175)

btn_apply =Button(labelframe_gray,text= "Apply",command=Apply,width =14,bg ="red",fg = "white",font="Time 8 bold")
btn_apply.place(x=40,y=400)
reset =Button(labelframe_gray,text= "Reset",command=Reset_Image,width =14,bg ="green",fg = "white",font="Time 8 bold")
reset.place(x=185,y=400)

#Cân bằng độ sáng
labelframeCHANGEBRIGTHNESS=LabelFrame(frame,text="BRIGTHNESS",fg = 'red',font= "Time 8 bold",width=344,
             height=506,highlightcolor="yellow",
             highlightbackground="red")
lab = Label(labelframeCHANGEBRIGTHNESS,text="Alpha : ",fg= "red",font= "Time 8 bold")
# lab.place(x=1,y=20)
slider_alpha = Scale(labelframeCHANGEBRIGTHNESS,from_= 0,to=2, length = 250,resolution=0.1,orient = HORIZONTAL,command=Display_Change_brightness,activebackground="red",troughcolor="yellow")
slider_alpha.set(0.8)
# slider_alpha.place(x= 40, y = 0)
lab1 = Label(labelframeCHANGEBRIGTHNESS,text="Beta : ",fg= "red",font= "Time 8 bold")
# lab1.place(x=1,y=60)
slider_beta3 = Scale(labelframeCHANGEBRIGTHNESS,from_= 0,to=50, length = 250,resolution=2,orient = HORIZONTAL,command=Display_Change_brightness,fg= "black",bg="#F0F0F0",activebackground="red",troughcolor="yellow",)
slider_beta3.set(25)
# slider_beta.place(x= 40, y = 40)
#four dark
lab_fourDark = Label(labelframeCHANGEBRIGTHNESS,text="FOUR DARK CORNERS ",fg= "red",font= "Time 8 bold")
# lab_fourDark.place(x=1,y=90)
labCl = Label(labelframeCHANGEBRIGTHNESS,text="X : ",fg= "red",font= "Time 8 bold")
# labCl.place(x=1,y=130)
slider_X = Scale(labelframeCHANGEBRIGTHNESS,from_= 0,to=500, length = 250,resolution=10, command=Vignette1,orient = HORIZONTAL,activebackground="yellow",troughcolor="black")
slider_X.set(100)
# slider_X.place(x= 40, y = 105)
larow = Label(labelframeCHANGEBRIGTHNESS,text="Y : ",fg= "red",font= "Time 8 bold")
# larow.place(x=1,y=175)
slider_Y = Scale(labelframeCHANGEBRIGTHNESS,from_= 0,to=500, length = 250,resolution=10, command=Vignette1,orient = HORIZONTAL,activebackground="yellow",troughcolor="black")
slider_Y.set(150)
# slider_Y.place(x= 40, y = 150)
#RGB
lab_RGB = Label(labelframeCHANGEBRIGTHNESS,text="CHANGE THE COLOR OF THE PHOTO ",fg= "red",font= "Time 8 bold")
# lab_RGB.place(x=1,y=180)
# labCl.place(x=1,y=210)
# slider_X.place(x= 40, y = 200)
labR = Label(labelframeCHANGEBRIGTHNESS,text="RED : ",fg= "red",font= "Time 8 bold")
slider_RED = Scale(labelframeCHANGEBRIGTHNESS,from_= 0,to=255, length = 250,resolution=5, command=GRB2GRB,orient = HORIZONTAL,activebackground="yellow",troughcolor="red")
slider_RED.set(100)

labG = Label(labelframeCHANGEBRIGTHNESS,text="GREEN : ",fg= "red",font= "Time 8 bold")
slider_GREEN = Scale(labelframeCHANGEBRIGTHNESS,from_= 0,to=255, length = 250,resolution=5, command=GRB2GRB,orient = HORIZONTAL,activebackground="yellow",troughcolor="green")
slider_GREEN.set(100)

labB = Label(labelframeCHANGEBRIGTHNESS,text="BLUE : ",fg= "red",font= "Time 8 bold")
slider_BLU = Scale(labelframeCHANGEBRIGTHNESS,from_= 0,to=255, length = 250,resolution=5, command=GRB2GRB,orient = HORIZONTAL,activebackground="yellow",troughcolor="blue")
slider_BLU.set(100)

btn_apply1 =Button(labelframeCHANGEBRIGTHNESS,text= "Apply",command=Apply,width =14,bg ="red",fg = "white",font="Time 8 bold")
btn_apply1.place(x=40,y=380)
reset1 =Button(labelframeCHANGEBRIGTHNESS,text= "Reset",command=Reset_Image,width =14,bg ="green",fg = "white",font="Time 8 bold")
reset1.place(x=185,y=380)
#frame ghép ảnh
labelframeCollage=LabelFrame(frame,text="COLLAGE",fg = 'red',font= "Time 8 bold",width=344,
             height=506,highlightcolor="yellow",
             highlightbackground="red")
#ảnh 2
label_fr_anhgoc_1=LabelFrame(labelframeCollage,text="ẢNH THỨ HAI",fg = '#F7961E',font= "Time 8 bold",width=260,
             height=300,highlightcolor="yellow",cursor = "target",bg="black",
             highlightbackground="white",highlightthickness=1)
label_fr_anhgoc_1.place(x = 60, y = 5)


btna2 =Button(labelframeCollage,text= "Choose image",command= opemImage2,width =12,bg ="black",fg = "white",font="Time 8 bold")
btna2.place(x=20,y=310)

lable_anh12 = Label(label_fr_anhgoc_1,bg="black")
lable_anh12.place(x=6,y=0)
#
labapha1 = Label(labelframeCollage,text=" Alpha : ",fg= "red",font= "Time 8 bold")
# labapha1.place(x=2,y=363)
slider_apha1 = Scale(labelframeCollage,from_= 0,to=1, length = 260,resolution=0.1,command=addweightedImag,orient = HORIZONTAL,activebackground="yellow",troughcolor="black")
slider_apha1.set(0.8)
# slider_apha1.place(x= 60, y = 340)
# #beta
labbeta = Label(labelframeCollage,text=" Beta : ",fg= "red",font= "Time 8 bold")
# labbeta.place(x=2,y=410)
slider_beta = Scale(labelframeCollage,from_= 0,to=1, length = 260,resolution=0.1,command=addweightedImag,orient = HORIZONTAL,activebackground="yellow",troughcolor="black")
slider_beta.set(0.3)
# slider_beta.place(x= 60, y = 390)
labgamma = Label(labelframeCollage,text=" gamma : ",fg= "red",font= "Time 8 bold")
# labgamma.place(x=2,y=450)
slider_gamma = Scale(labelframeCollage,from_= 0,to=1, length = 260,resolution=0.1,command=addweightedImag,orient = HORIZONTAL,activebackground="yellow",troughcolor="black")
slider_gamma.set(0)
# slider_gamma.place(x= 60, y = 425)
btn_apply3 =Button(labelframeCollage,text= "Apply",command=Apply,width =12,bg ="red",fg = "white",font="Time 8 bold")
btn_apply3.place(x=130,y=310)
reset3 =Button(labelframeCollage,text= "Reset",command=Reset_Image,width =12,bg ="green",fg = "white",font="Time 8 bold")
reset3.place(x=240,y=310)

#Làm ghép ảnh làm mờ gausian
labelframeBlurbackgruond =LabelFrame(frame,text="BLUR BACKGROUND",fg = 'red',font= "Time 8 bold",width=344,
             height=506,highlightcolor="yellow",
             highlightbackground="red")
label_fr_object =LabelFrame(labelframeBlurbackgruond,text="SELECTED OBJECT",fg = '#F7961E',font= "Time 8 bold",width=260,
             height=300,highlightcolor="yellow",cursor = "target",bg="black",
             highlightbackground="white",highlightthickness=1)
label_fr_object.place(x = 40, y = 5)

btnobj =Button(labelframeBlurbackgruond,text= "select object",command= ROI_Img_process,width =16,bg ="black",fg = "white",font="Time 8 bold")
btnobj.place(x=100,y=310)
lable_anh1 = Label(label_fr_object,bg="black")
lable_anh1.place(x=6,y=0)
combbkenner = CB.Combobox(labelframeBlurbackgruond, width = 15, height = 3, font = "Time 8 bold",state = "readonly")
combbkenner['values'] = (arrMASKVALUE)
combbkenner.current(3)


KERNEL = Label(labelframeBlurbackgruond,text=" FILTER MASK : ",fg= "red",font= "Time 8 bold")
# labapha1.place(x=2,y=363)
slider_mask = Scale(labelframeBlurbackgruond,from_= 0,to=21,command=ROI_Img, length = 260,resolution=1,orient = HORIZONTAL,activebackground="yellow",troughcolor="black")
slider_mask.set(3)
# slider_apha1.place(x= 60, y = 340)
# #beta
sigmaX  = Label(labelframeBlurbackgruond,text=" SIGMAX : ",fg= "red",font= "Time 8 bold")
# labbeta.place(x=2,y=410)
slider_sigmaX1 = Scale(labelframeBlurbackgruond,from_= 0,to=20,command=ROI_Img, length = 240,resolution=1,orient = HORIZONTAL,activebackground="yellow",troughcolor="black")
slider_sigmaX1.set(4)
# slider_beta.place(x= 60, y = 390)
sigmaY = Label(labelframeBlurbackgruond,text=" SIGMAY : ",fg= "red",font= "Time 8 bold")
# labgamma.place(x=2,y=450)
slider_sigmaY = Scale(labelframeBlurbackgruond,from_= 0,to=20, command=ROI_Img,length = 240,resolution=1,orient = HORIZONTAL,activebackground="yellow",troughcolor="black")
slider_sigmaY.set(4)

btn_apply4 =Button(labelframeBlurbackgruond,text= "Apply",command=Apply,width =14,bg ="red",fg = "white",font="Time 8 bold")
btn_apply4.place(x=40,y=450)
reset4 =Button(labelframeBlurbackgruond,text= "Reset",command=Reset_Image,width =14,bg ="green",fg = "white",font="Time 8 bold")
reset4.place(x=185,y=450)

# làm mịn ảnh
labelframeIMAGESMOOTHING=LabelFrame(frame,text="UPGRADE",fg = 'red',font= "Time 8 bold",width=348,
             height=500,highlightcolor="yellow",
             highlightbackground="red")
labmask = Label(labelframeIMAGESMOOTHING,text="MASK : ",fg= "red",font= "Time 8 bold")

combb1 = CB.Combobox(labelframeIMAGESMOOTHING, width = 18, height = 3, font = "Time 9 bold",state = "readonly")
combb1['values'] = (arrMASKVALUE)
combb1.current(1)

labSigmax = Label(labelframeIMAGESMOOTHING,text="SIGMAX :",fg= "#5FD496",font= "Time 11 bold")

slider_sigmaX = Scale(labelframeIMAGESMOOTHING,from_= 0,to=10, length = 230,resolution=1,orient = HORIZONTAL)

labSigmay = Label(labelframeIMAGESMOOTHING,text="SIGMAX :",fg= "#5FD496",font= "Time 11 bold")

slider_sigmay = Scale(labelframeIMAGESMOOTHING,from_= 0,to=10, length = 230,resolution=1,orient = HORIZONTAL)
#https://docs.opencv.org/3.4.3/d4/d86/group__imgproc__filter.html#ga9d7064d478c95d60003cf839430737ed
#https://aicurious.io/posts/2018-09-29-loc-anh-image-filtering/
#https://www.stdio.vn/computer-vision/xu-ly-anh-voi-opencv-loc-so-trong-anh-kjcgL1
labelframeGaussian=LabelFrame(labelframeIMAGESMOOTHING,text="GAUSSIAN",fg = 'red',font= "Time 8 bold",width=340,
             height=160,highlightcolor="yellow",
             highlightbackground="red")
labelframeSmothing=LabelFrame(labelframeIMAGESMOOTHING,text="SMOOTHING",fg = 'red',font= "Time 8 bold",width=340,
             height=140,highlightcolor="yellow",
             highlightbackground="red")

value=IntVar()
R_Smoothing = Radiobutton(labelframeIMAGESMOOTHING,command= smoothing, text="SMOOTHING",variable=value,activeforeground="red",highlightcolor="red",selectcolor="white",value=1,fg= "red",font= "Time 9 bold")
R_Noise = Radiobutton(labelframeIMAGESMOOTHING, text="DETECT EDGES",command=Noise1,variable=value,activeforeground="red",highlightcolor="red",selectcolor="white",value=2, fg= "red",font= "Time 9 bold")

btn_apply2 =Button(labelframeIMAGESMOOTHING,text= "Apply",command=Apply,width =14,bg ="red",fg = "white",font="Time 8 bold")
btn_apply2.place(x=40,y=430)
reset2 =Button(labelframeIMAGESMOOTHING,text= "Reset",command=Reset_Image,width =14,bg ="green",fg = "white",font="Time 8 bold")
reset2.place(x=185,y=430)

var = IntVar()
R1 = Radiobutton(labelframeSmothing, text="GAUSSIAN",command=gaussian,variable=var,activeforeground="red",highlightcolor="red",selectcolor="yellow",value=1, font="Time 8 bold",fg= "blue" )

R2 = Radiobutton(labelframeSmothing, text="MEAN",command=Mean,variable=var,activeforeground="red",highlightcolor="red",selectcolor="yellow",value=2, font="Time 8 bold",fg= "blue")

R3 = Radiobutton(labelframeSmothing, text="MEDIAN", variable=var,command=Median,activeforeground="red",highlightcolor="red",selectcolor="yellow",value=3, font="Time 8 bold",fg= "blue")

R4 = Radiobutton(labelframeSmothing, text="BILATERAL ",command=Bilataral, variable=var,activeforeground="red",highlightcolor="red",selectcolor="yellow",value=4, font="Time 8 bold",fg= "blue")

R5 = Radiobutton(labelframeSmothing, text="Nonfunction", variable=var,activeforeground="red",highlightcolor="red",selectcolor="yellow",value=5, font="Time 8 bold",fg= "blue")

R6 = Radiobutton(labelframeSmothing, text="Nonfunction ", variable=var,activeforeground="red",highlightcolor="red",selectcolor="yellow",value=6, font="Time 8 bold",fg= "blue")

sigmaXG  = Label(labelframeGaussian,text=" SIGMAX : ",fg= "red",font= "Time 8 bold")

slider_sigmaXG = Scale(labelframeGaussian,from_= 0,to=20, length = 240,resolution=1,command=Gaussian_smooothing,orient = HORIZONTAL,activebackground="yellow",troughcolor="black")
slider_sigmaXG.set(4)

sigmaYG = Label(labelframeGaussian,text=" SIGMAY : ",fg= "red",font= "Time 8 bold")

slider_sigmaYG = Scale(labelframeGaussian,from_= 0,to=20,length = 240,resolution=1,command=Gaussian_smooothing,orient = HORIZONTAL,activebackground="yellow",troughcolor="black")
slider_sigmaYG.set(6)

labelframeNoise=LabelFrame(labelframeIMAGESMOOTHING,text="FIND IMAGE EDGES",fg = 'red',font= "Time 8 bold",width=340,
             height=140,highlightcolor="yellow",
             highlightbackground="red")

var1 = IntVar()
R11 = Radiobutton(labelframeNoise, text="SKETCH",command=Gradient,variable=var1,activeforeground="red",highlightcolor="red",selectcolor="yellow",value=1, font="Time 8 bold",fg= "blue" )
R22 = Radiobutton(labelframeNoise, text="SOBEL",command=Sobel, variable=var1,activeforeground="red",highlightcolor="red",selectcolor="yellow",value=2, font="Time 8 bold",fg= "blue")
R33 = Radiobutton(labelframeNoise, text="LAPLACIAN",command=Laplacia, variable=var1,activeforeground="red",highlightcolor="red",selectcolor="yellow",value=3, font="Time 8 bold",fg= "blue")
R44 = Radiobutton(labelframeNoise, text="Nonfunction", variable=var1,activeforeground="red",highlightcolor="red",selectcolor="yellow",value=4, font="Time 8 bold",fg= "blue")
R55 = Radiobutton(labelframeNoise, text="Nonfunction", variable=var1,activeforeground="red",highlightcolor="red",selectcolor="yellow",value=5, font="Time 8 bold",fg= "blue")
R66 = Radiobutton(labelframeNoise, text="Nonfunction", variable=var1,activeforeground="red",highlightcolor="red",selectcolor="yellow",value=6, font="Time 8 bold",fg= "blue")


# bilateral
labelframeBilateral=LabelFrame(labelframeIMAGESMOOTHING,text="BILATERAL",fg = 'red',font= "Time 8 bold",width=340,
             height=180,highlightcolor="yellow",
             highlightbackground="red")
labSD = Label(labelframeBilateral,text="Diameter : ",fg= "#5FD496",font= "Time 9 bold")
slider_D = Scale(labelframeBilateral,from_= 0,to=30, length = 220,resolution=1,command=Bilaterai,activebackground="yellow",orient = HORIZONTAL)
slider_D.set(9)
labSimaColor = Label(labelframeBilateral,text="Sigmacolor :",fg= "#5FD496",font= "Time 9 bold")
slider_SimaColor = Scale(labelframeBilateral,from_= 0,to=100, length = 220,resolution=5,command=Bilaterai,activebackground="yellow",orient = HORIZONTAL)
slider_SimaColor.set(75)
labSigmaSpace = Label(labelframeBilateral,text="Sigmaspace :",fg= "#5FD496",font= "Time 9 bold")
slider_Space = Scale(labelframeBilateral,from_= 0,to=100, length = 220,resolution=5,command=Bilaterai,activebackground="yellow",orient = HORIZONTAL)
slider_Space.set(75)
#mean
labelframeMean=LabelFrame(labelframeIMAGESMOOTHING,text="MEAM",fg = 'red',font= "Time 8 bold",width=340,
             height=180,highlightcolor="yellow",
             highlightbackground="red")
#MEDIAN
labelframeMedian=LabelFrame(labelframeIMAGESMOOTHING,text="MEDIAM",fg = 'red',font= "Time 8 bold",width=340,
             height=180,highlightcolor="yellow",
             highlightbackground="red")
#MEDIAN
labelframeGradient=LabelFrame(labelframeIMAGESMOOTHING,text="SKETCH",fg = 'red',font= "Time 8 bold",width=340,
             height=180,highlightcolor="yellow",
             highlightbackground="red")
labScale = Label(labelframeGradient,text="Scale :",fg= "red",font= "Time 9 bold")
slider_Scale = Scale(labelframeGradient,from_= 0,to=255, length = 220,resolution=10,command=Sketch_smoothing,activebackground="red",orient = HORIZONTAL)
slider_Scale.set(230)




#MEDIAN
labelframeSobel=LabelFrame(labelframeIMAGESMOOTHING,text="SOBEL",fg = 'red',font= "Time 8 bold",width=340,
             height=180,highlightcolor="yellow",
             highlightbackground="red")
#MEDIAN
labelframeLaplacia=LabelFrame(labelframeIMAGESMOOTHING,text="LAPLACIA",fg = 'red',font= "Time 8 bold",width=340,
             height=180,highlightcolor="yellow",
             highlightbackground="red")

#
labelframe=LabelFrame(frame,text="CÁC CHỨC NĂNG CHÍNH",fg = '#F7961E',font= "Time 8 bold",width=345,
             height=520,highlightcolor="yellow",
             highlightbackground="red",highlightthickness=1)



# Khung ảnh gốc
labelframe2=LabelFrame(app,text="ẢNH GỐC",fg = '#F7961E',font= "Time 8 bold",width=390,
             height=527,highlightcolor="yellow",cursor = "target",bg="black",
             highlightbackground="white",highlightthickness=1)
labelframe2.place(x = 358, y = 5)
my_image_lable = Label(labelframe2,bg="black")
my_image_lable.place(x=6,y=20)

# Khung ảnh sau chỉnh sửa
labelframe3=LabelFrame(app,text="NEW",fg = '#F7961E',font= "Time 8 bold",width=390,
             height=527,highlightcolor="yellow",bg="black",
             highlightbackground="white",highlightthickness=1)
labelframe3.place(x = 753, y = 5)
my_image_lable2 = Label(labelframe3,bg="black")
# my_image_lable2.place(x=6, y=20)

# draw immge
labelframeDraw=LabelFrame(frame,text="DRAW",fg = 'red',font= "Time 8 bold",width=344,
             height=506,highlightcolor="yellow",
             highlightbackground="red")
btnDraw =Button(labelframeDraw,text= "DRAW",command=process_draw,width =13,bg ="#AB2365",fg = "white",font="Time 8 bold")
textInput = Entry(labelframeDraw,width = 40,fg= "red")
labtextinput = Label(labelframeDraw,text=" TEXT : ",fg= "red",font= "Time 8 bold")
labtextpencolor = Label(labelframeDraw,text=" PEN COLLOR : ",fg= "red",font= "Time 8 bold")


labtextpencolorR = Label(labelframeDraw,text="COLLOR RED : ",fg= "red",font= "Time 7 bold")
slider_RED_p = Scale(labelframeDraw,from_= 0,to=255, length = 210,resolution=5,orient = HORIZONTAL,activebackground="yellow",troughcolor="red")
slider_RED_p.set(150)

labtextpencolorG = Label(labelframeDraw,text="COLLOR GREEN : ",fg= "green",font= "Time 7 bold")
slider_GREEN_p = Scale(labelframeDraw,from_= 0,to=255, length = 210,resolution=5, orient = HORIZONTAL,activebackground="yellow",troughcolor="green")
slider_GREEN_p.set(100)

labtextpencolorB = Label(labelframeDraw,text="COLLOR BLUE: ",fg= "blue",font= "Time 7 bold")
slider_BLU_p = Scale(labelframeDraw,from_= 0,to=255, length = 210,resolution=5, orient = HORIZONTAL,activebackground="yellow",troughcolor="blue")
slider_BLU_p.set(50)
labtextsizepen = Label(labelframeDraw,text=" SIZE PEN : ",fg= "red",font= "Time 8 bold")
slider_textsizepen = Scale(labelframeDraw,from_= 0,to=1, length = 210,resolution=0.05, orient = HORIZONTAL,activebackground="yellow",troughcolor="blue")
slider_textsizepen.set(0.05)

btn_apply5 =Button(labelframeDraw,text= "Apply",command=Apply,width =14,bg ="red",fg = "white",font="Time 8 bold")
btn_apply5.place(x=40,y=450)
reset5 =Button(labelframeDraw,text= "Reset",command=Reset_Image,width =14,bg ="green",fg = "white",font="Time 8 bold")
reset5.place(x=185,y=450)
# btnHistogram.place(x=200,y=50)
# canvas.bind("<Button-1>", get_x_and_y)
# canvas.bind("<B1-Motion>", draw_smth)



app.mainloop()
