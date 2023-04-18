from skimage import io,  color
from pylab import *

#Read image
img = io.imread('animais/puppy.png')
#Convert to YPbPr
img_ypbpr = color.rgb2ypbpr(img)
#Convert back to RGB
img_rgb = color.ypbpr2rgb(img_ypbpr)
io.imsave("animais/puppy_ypbpr.jpg", img_ypbpr)