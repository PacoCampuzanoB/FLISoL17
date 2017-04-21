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

# Open initial image:
im_i = plt.imread("../imgs/me.png")[:,:,:3]

# Open final image:
im_f = plt.imread("../imgs/pug.jpeg")[:,:,:3]

# Mid states:
A = 0.7*im_i + 0.3*im_f/255.
B = 0.4*im_i + 0.6*im_f/255.

# Four axes, returned as a 2-d array
f, axarr = plt.subplots(2, 2, figsize=(8,8))
axarr[0,0].imshow(im_i)
axarr[0,1].imshow(A)
axarr[1,0].imshow(B)
axarr[1,1].imshow(im_f)

plt.show()
