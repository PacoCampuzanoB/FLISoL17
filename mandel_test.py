"""
Compute and plot the Mandelbrot set using matplotlib.
"""

import numpy as np
import pylab

from numba import jit

@jit
def mandel(x, y, max_iters):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    c = complex(x,y)
    z = 0j
    # c = complex(-0.001, 0.80)
    # z = complex(x,y)
    for i in range(max_iters):
        z = z*z + c
        if z.real * z.real + z.imag * z.imag >= 4:
            return 255 * i // max_iters

    return 255

@jit(nopython=True)
def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height
    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = mandel(real, imag, iters)
            image[y, x] = color

    return image

image = np.zeros((1024, 1024), dtype=np.uint8)
create_fractal(-0.555, -0.550, -0.555, -0.550, image, 300)

# Creare your figure and axes
fig, ax = pylab.subplots(1, figsize=(8,8))
# Set whitespace to 0
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

pylab.set_cmap("viridis")
pylab.imshow(image)
# Turn off axes and set axes limits
ax.axis('tight')
ax.axis('off')
#pylab.gray()
#pylab.savefig("mandel.png", dpi=600)
pylab.show()
