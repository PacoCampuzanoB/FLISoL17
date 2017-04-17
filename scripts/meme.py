from __future__ import unicode_literals
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
import matplotlib.pyplot as plt
import seaborn as sns

# Read images:
im_i = plt.imread("../imgs/me.png")
im_f = plt.imread("../imgs/pug.jpeg")

# Filter only 3 channels:
im_i = im_i[:,:,:3]
im_f = im_f[:,:,:3]

# Create two middle images for transition:
A = 0.7*im_i + 0.3*im_f/255.
B = 0.4*im_i + 0.6*im_f/255.

# Create four axes, returned as a 2-d array
f, axarr = plt.subplots(2, 2, figsize=(8,8))
axarr[0, 0].imshow(im_i)
axarr[0, 0].grid(False)
axarr[0, 1].imshow(A)
axarr[0, 1].grid(False)
axarr[1, 0].imshow(B)
axarr[1, 0].grid(False)
axarr[1, 1].imshow(im_f)
axarr[1, 1].grid(False)

# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
plt.setp([a.get_xticklabels() for a in axarr[1, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 0]], visible=False)
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
# f.subplots_adjust(hspace=0.0, wspace=0.0, top=0.9, bottom=0.1, right=0.9, left=0.1)
f.subplots_adjust(hspace=0.0, wspace=-0.2, top=0.8)

# Adding text:
plt.suptitle(r"\noindent When sabes programar y te programas una transición \\"
             r"de opacidad $(1-\alpha)A + \alpha B$ para dos imágenes $A$ y \\"
             r"$B$, con $\alpha \in \left[0,1\right]$ y te conviertes en un meme de pug:",
             size=24, multialignment='center')
plt.figtext(0.548, 0.096, 'This plot was created with the magic of Python.',
            color='black', weight='roman', size='x-small')

# Show and save figure:
plt.show()
f.savefig("../lecture/imgs/meme.png")
