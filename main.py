from PIL import Image, ImageOps
import numpy as np
from numpy import asarray
from otsu import OtsuThresholder
import matplotlib.pyplot as plt
from skimage.filters import threshold_local

if __name__ == "__main__":
    image = Image.open("images/image1.png")
    imageOriginal = asarray(image)
    
    image = ImageOps.grayscale(image)
    image = asarray(image)

    Otsu = OtsuThresholder(image)
    threshold = Otsu.Otsu()

    block_size = 35
    adaptive_thresh = threshold_local(image, block_size, offset=10)
    binary_adaptive = image > adaptive_thresh

    binary = image > threshold
    binary = binary.astype(int)

    fig, axes = plt.subplots(ncols=3, figsize=(8, 2.5))
    ax = axes.ravel()
    ax[0] = plt.subplot(1, 3, 1, adjustable='box')
    ax[1] = plt.subplot(1, 3, 2)
    ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0], adjustable='box')

    ax[0].imshow(image, cmap=plt.cm.gray)
    ax[0].set_title('Original')
    ax[0].axis('off')

    ax[1].hist(image.ravel(), bins=256)
    ax[1].set_title('Histogram')
    ax[1].axvline(threshold, color='r')

    ax[2].imshow(binary, cmap=plt.cm.gray)
    ax[2].set_title('Thresholded')
    ax[2].axis('off')

    plt.show()
   
    #binaryImage.show()
    

    



    