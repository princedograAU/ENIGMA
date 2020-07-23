__author__ = 'Prince Dogra'

from PIL import Image

im = Image.new('RGBA',(1358,768), (255,140,20,255))
im.load()
px = im.load()

for i in range(im.size[0]):
    for j in range(im.size[1]):
       px[i,j] = (px[i,j][0],px[i,j][1],px[i,j][2],255)


im.save("G:\my.png")
im.show()