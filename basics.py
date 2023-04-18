"""
Basics image IO with SciKit Image
"""

from skimage import io
import pandas as pd

# Aquisition and show image:
img = io.imread('animais/puppy.png')
io.imshow(img)

#Get Image resolution
print(img.shape)

# getting pixel values
df = pd.DataFrame(img.flatten())
filepath = 'pixel_values1.xlsx'
df.to_excel(filepath, index=False)

io.show()
