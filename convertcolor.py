"""
converte an image in a diferente format color
use the following functions:
• rgb2hsv
• hsv2rgb
• rgb2xyz
• xyz2rgb
• rgb2grey
• grey2rgb
• rgb2yuv
• yuv2rgb
• rgb2lab
• lab2rgb
• rgb2yiq
• yiq2rgb
• rgb2ypbpr
• ypbpr2rgb
"""

from skimage import io, color, data
from pylab import *


#Read image:

img = io.imread("animais/puppy.png")

# Convert to HSV
img_hsv = color.rgb2hsv(img)
#Back to rgb
img_rgb = color.hsv2rgb(img_hsv)

# #Show images
# figure(0)
# io.imshow(img_hsv)
# figure(1)
# io.imshow(img_rgb)

#Convert to xyz
img_xyz = color.rgb2xyz(img)
img_rgb = color.xyz2rgb(img_xyz)
figure(0)
io.imshow(img_xyz)
figure(1)
io.imshow(img_rgb)


io.show()
