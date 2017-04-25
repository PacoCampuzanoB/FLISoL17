# ===============================================================
# Author: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro, for his
# talk in FLISoL 2017 at Instituto Tecnológico de León. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================


import numpy as np
import matplotlib.pyplot as plt

# Open initial image:
img = plt.imread("../imgs/Lenna.png")[:,:,:3]

# Show original image:
plt.imshow(img)
plt.show()

# Create a section cropped:
cropped_img = img[220:300,210:370]

# Show section:
plt.imshow(cropped_img)
plt.show()

# Save cropped image:
plt.imsave("../imgs/eyes.png", cropped_img)
