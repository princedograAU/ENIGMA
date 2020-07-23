__author__ = 'Prince Dogra'

from PIL import Image

'''------------------------------------------------FUNCTIONS---------------------------------------------------'''

def Scaling(px):

    if(px[0]%2 == 0):
        px[0] = px[0]+1

    if(px[1] == 0):
        px[1] = px[1]+1

    if(px[2] == 0):
        px[2] = px[2]+1

    new_RGB = [px[0],px[1],px[2]]
    return(new_RGB)

'''-----------------------------------------------MAIN METHOD-------------------------------------------------'''
im = Image.open("G:/zoo.png")
pixel = im.load()

for i in range(im.size[0]):
    for j in range(im.size[1]):
        '''rgb_r = pixel[i,j][0]
        rgb_g = pixel[i,j][1]
        rgb_b = pixel[i,j][2]'''
        list = [pixel[i,j][0] ,pixel[i,j][1] ,pixel[i,j][2]]
        RGB = Scaling(list)
        pixel[i,j] = (RGB[0],RGB[1],RGB[2],255)


im.save("G:/modified.png")
im.show()