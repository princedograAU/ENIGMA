__author__ = 'Prince Dogra'
import math

from PIL import Image

def ret_nearest_value(a):
    if a%8==0:
        return(a)
    else:
        return(a-(a%8))


im = Image.open("G:\zoo.png")
print(im.format, im.size)
new_x = ret_nearest_value(im.size[0])
new_y = ret_nearest_value(im.size[1])
im2 = im.crop((0,0,new_x,new_y))
im2.save("G:\zoo1.png")
print(im2.size)
im2.show()
