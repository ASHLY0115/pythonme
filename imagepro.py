from PIL import Image
#open Image
im = Image.open("taj Mahal.jpg")

#image rotate & show
im.rotate(45).show()
im.convert("L").show()