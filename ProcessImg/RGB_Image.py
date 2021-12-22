from PIL import Image
#sửa từng pixel cho ảnh gốc tạo ra ảnh mới.
def GRB(path,red,green,blu):
    img = Image.open(path)
    pixels = img.load()#tạo ra pixel của hình ảnh
    new_img = Image.new(img.mode, img.size)
    pixels_new = new_img.load()
    for i in range(new_img.size[0]):
        for j in range(new_img.size[1]):
            r, b, g = pixels[i,j]
            # avg = int(round((r + b + g) / 3))
            R = int(round((r+red)/2))
            if(red == 0):
                R = 0
            B = int(round((b + blu) / 2))
            if (blu == 0):
                B = 0
            G = int(round((g+green)/2))
            if(green == 0):
                G = 0

            pixels_new[i,j] = (R,G,B, 0)
    # new_img.show()
    return new_img
# GRB(10,20,100)
#https://koodibar.com/posts/xu-ly-hinh-anh-voi-python