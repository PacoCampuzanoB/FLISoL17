# ===============================================================
# Author: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro, for his
# talk in FLISoL 2017 at Instituto Tecnológico de León. Any
# explicit usage of this script or its contents must be granted
# by the author. You can contact him via email or Twitter.
# ===============================================================


import numpy as np
import matplotlib.pyplot as plt

# Open image:
img = plt.imread("../imgs/Lenna.png")[:,:,:3]

# Print image matrix:
print(img)

# Show image:
plt.imshow(img)
plt.axis('Off')
plt.show()
