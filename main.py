from PIL import Image, ImageFilter

with Image.open("logika.png") as original:
    # original.show()
    grey = original.convert("L")
    grey.save("grey.png")
    grey.show()

    rotated_img = original.transpose(Image.ROTATE_90)
    rotated_img.save("rotated.png")

    blur = original.filter(ImageFilter.GaussianBlur(5))
    blur.save("blur.png")