import numpy as np
import matplotlib.pyplot as plt

def rgb2gray(rgb):
    return rgb[...,:3] @ [0.299, 0.587, 0.114]

def sobelX(img):
    i, j = img.shape
    diff = img[:,1:j] - img[:,0:j-1]
    return np.column_stack((diff, np.zeros(i)))

def sobelY(img):
    i, j = img.shape
    diff = img[1:i,:] - img[0:i-1,:]
    return np.column_stack((diff.T, np.zeros(i))).T

def gradient(img):
    return (diff_X(img)[:,:]**2 + diff_Y(img)[:,:]**2)**0.5

img = rgb2gray(plt.imread("imgs/Lenna.png"))
print(img.shape)
fig = plt.figure(figsize=(7,7))
plt.set_cmap('bone')

# First:
plt.subplot(221)
plt.imshow(img)
plt.title('Original image')
plt.axis('off')

# Second:
plt.subplot(222)
plt.imshow(gradient(img))
plt.title('Gradient')
plt.axis('off')

# Third:
plt.subplot(223)
plt.imshow(sobelX(img))
plt.title('Diff X')
plt.axis('off')

# Fourth:
plt.subplot(224)
plt.imshow(sobelY(img))
plt.title('Diff Y')
plt.axis('off')

# plt.savefig("../lecture/imgs/derivatives.png")
plt.show()
