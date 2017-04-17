import numpy as np
import matplotlib.pyplot as plt

# Open initial image:
im_i = plt.imread("imgs/me.png")
im_i = im_i[:,:,:3]
# Open final image:
im_f = plt.imread("imgs/pug.jpeg")
im_f = im_f[:,:,:3]

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
