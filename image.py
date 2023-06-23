
from PIL import Image
#to open a image
im=Image.open("TajMahal.jpg")
#to rotate the image
im.rotate(45).show()
#to black&white
im.convert("L").show()






