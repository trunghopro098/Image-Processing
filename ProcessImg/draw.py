import cv2

IMAGE = "../Image/goodgirrl.png"
OUT_IMAGE = "../Image/goodgirrl.png"


def draw_text(image,
              text,
              x,
              y,
              color_bgr=[255, 0, 0],
              size=0.05,  # in the range of (0, 1.0)
              font_face=cv2.FONT_HERSHEY_PLAIN,
              thickness=0,  # 0: auto
              line_type=cv2.LINE_AA,
              is_copy=True):
    """
        Supported Fonts: https://docs.opencv.org/4.3.0/d6/d6e/group__imgproc__draw.html#ga0f9314ea6e35f99bb23f29567fc16e11
        Line Types: https://docs.opencv.org/4.3.0/d6/d6e/group__imgproc__draw.html#gaf076ef45de481ac96e0ab3dc2c29a777
    """
    assert size > 0

    image = image.copy() if is_copy else image  # copy/clone a new image
    if not text:  # empty text
        return image

    # https://docs.opencv.org/4.3.0/d6/d6e/group__imgproc__draw.html#ga3d2abfcb995fd2db908c8288199dba82
    (text_width, text_height), _ = cv2.getTextSize(text, font_face, 1.0, thickness)  # estimate text size

    # calculate font scale
    h, w = image.shape[:2]
    short_edge = min(h, w)
    expect_size = short_edge * size
    font_scale = expect_size / text_height

    # calc thickness
    if thickness <= 0:
        thickness = int(font_scale)
        thickness = 1 if thickness == 0 else thickness

    # calc x,y in absolute coord
    x_abs = int(x * w)
    y_abs = int(y * h)

    # docs: https://docs.opencv.org/4.3.0/d6/d6e/group__imgproc__draw.html#ga5126f47f883d730f633d74f07456c576
    cv2.putText(img=image,
                text=text,
                org=(x, y),
                fontFace=font_face,
                fontScale=font_scale,
                color=color_bgr,
                thickness=thickness,
                lineType=line_type,
                bottomLeftOrigin=False)
    return image


# def main():
#     img = cv2.imread(IMAGE)
#     img_text = draw_text(image=img,
#                          text="Hi em",
#                          x=0.70,
#                          y=0.12,
#                          size=0.05,
#                          color_bgr=[0, 0, 255],
#                          is_copy=True)
#     img_text = draw_text(image=img_text,
#                          text="Good afternoon",
#                          x=0.55,
#                          y=0.18,
#                          size=0.03,
#                          color_bgr=[0, 255, 255],
#                          is_copy=False)
#     cv2.imwrite(OUT_IMAGE, img_text)
#     print("Done drawing text @ %s" % OUT_IMAGE)
#
#
# if __name__ == "__main__":
#     main()