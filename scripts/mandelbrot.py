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
import pylab

def mandel(x, y, max_iters):
    c = complex(x,y)
    z = 0j
    for i in range(max_iters):
        z = z*z + c
        if z.real * z.real + z.imag * z.imag >= 4:
            return 255 * i // max_iters

    return 255

def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width  = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height
    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag  = min_y + y * pixel_size_y
            color = mandel(real, imag, iters)
            image[y, x] = color

    return image

# Create fractal image:
image = np.zeros((600, 600), dtype=np.uint8)
create_fractal(-2., 2., -2., 2., image, 30)
# create_fractal(-0.555, -0.550, -0.555, -0.550, image, 100)
# create_fractal(-0.74877, -0.74872, 0.065053, 0.065103, image, 1000)

# Create your figure and axes:
fig, ax = pylab.subplots(1, figsize=(1,1))

# Set whitespace to 0:
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

# Set colormap and display image:
pylab.set_cmap("magma")
pylab.imshow(image)

# Turn off axes and set axes limits:
ax.axis('tight')
ax.axis('off')

# Save figure and show:
pylab.savefig("../imgs/mini_mandel.png", dpi=600)
pylab.show()
